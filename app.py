import cv2
import mediapipe as mp
from flask import Flask, render_template, Response
from Funciones.condicionales import condicionalesLetras
from Funciones.normalizacionCords import obtenerAngulos
from flask_socketio import SocketIO

from flask import jsonify, request

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

nuevo_contenido = ''

app = Flask(__name__)
socketio = SocketIO(app)

# Configuración del socket para recibir el texto de la consola
@socketio.on('console')
def handle_console(data):
    socketio.emit('console', data, broadcast=True)

def gen_frames():
    cap = cv2.VideoCapture(0)

    with mp_hands.Hands(
            max_num_hands=2,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as hands:
        while True:
            success, frame = cap.read()

            if not success:
                break

            height, width, _ = frame.shape
            frame = cv2.flip(frame, 1)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(frame_rgb)
            if results.multi_hand_landmarks is not None:
                angulosid = obtenerAngulos(results, width, height)[0]

                dedos = []
                if angulosid[5] > 125:
                    dedos.append(1)
                else:
                    dedos.append(0)

                if angulosid[4] > 150:
                    dedos.append(1)
                else:
                    dedos.append(0)

                for id in range(0, 4):
                    if angulosid[id] > 90:
                        dedos.append(1)
                    else:
                        dedos.append(0)

                TotalDedos = dedos.count(1)
                dedos, nuevo_contenido2 = condicionalesLetras(dedos, frame)

                global nuevo_contenido
                nuevo_contenido = nuevo_contenido2


                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        mp_drawing.draw_landmarks(
                            frame,
                            hand_landmarks,
                            mp_hands.HAND_CONNECTIONS,
                            mp_drawing_styles.get_default_hand_landmarks_style(),
                            mp_drawing_styles.get_default_hand_connections_style())

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame.flags.writeable = False
            results = hands.process(frame)

            frame.flags.writeable = True
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()
    cv2.destroyAllWindows()


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/actualizar_parrafo')
def actualizar_parrafo():
  return nuevo_contenido



@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    socketio.run(app, debug=True)

