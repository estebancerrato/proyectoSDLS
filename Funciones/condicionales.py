import cv2

def condicionalesLetras(dedos, frame):
    font = cv2.FONT_HERSHEY_SIMPLEX
    nuevo_contenido = ''
    if dedos == [1, 1, 0, 0, 0, 0]:
            cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
            cv2.putText(frame, 'A', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
            print("A")
            nuevo_contenido = 'A'

    elif dedos == [0, 0, 0, 0, 0, 0]:
            cv2.rectangle(frame, (0, 0), (100, 100), (255, 255,255), -1)
            cv2.putText(frame, 'E', (20, 80), font, 3, (0,0,0),2,cv2.LINE_AA)
            print("E")
            nuevo_contenido = 'E'

    elif dedos == [0, 0, 1, 0, 0, 0]:
            cv2.rectangle(frame, (0, 0), (100, 100), (255, 255,255), -1)
            cv2.putText(frame, 'I', (20, 80), font, 3, (0,0,0),2,cv2.LINE_AA)
            print("I")
            nuevo_contenido = 'I'

    elif dedos == [1, 0, 1, 0, 0, 0]:
            cv2.rectangle(frame, (0, 0), (100, 100), (255, 255,255), -1)
            cv2.putText(frame, 'O', (20, 80), font, 3, (0,0,0),2,cv2.LINE_AA)
            print("O")
            nuevo_contenido = 'O'

    elif dedos == [0, 0, 1, 0, 0, 1]:
            cv2.rectangle(frame, (0, 0), (100, 100), (255, 255,255), -1)
            cv2.putText(frame, 'U', (20, 80), font, 3, (0,0,0),2,cv2.LINE_AA)
            print("U")
            nuevo_contenido = 'U'

    # abecedario
    elif dedos == [0, 0, 1, 1, 1, 1]:
            cv2.rectangle(frame, (0, 0), (100, 100), (255, 255,255), -1)
            cv2.putText(frame, 'B', (20, 80), font, 3, (0,0,0),2,cv2.LINE_AA)
            print("B")
            nuevo_contenido = 'B'
        # if dedos ==[1,0,1,0,0,0]:
        #     cv2.rectangle(frame,(0,0),(100,100),(255,255,255), -1)
        #     cv2.putText(frame,'C',(20,80),font,3,(0,0,0),2,cv2.LINE_AA)
        #     print("C")
    elif dedos == [0, 0, 0, 0, 0, 1]:
            cv2.rectangle(frame, (0, 0), (100, 100), (255, 255,255), -1)
            cv2.putText(frame, 'D', (20, 80), font, 3, (0,0,0),2,cv2.LINE_AA)
            print("D")
            nuevo_contenido = 'D'
    elif dedos == [1, 1, 0, 0, 1, 1]:
            cv2.rectangle(frame, (0, 0), (100, 100), (255, 255,255), -1)
            cv2.putText(frame, 'K', (20, 80), font, 3, (0,0,0),2,cv2.LINE_AA)
            print("K")
            nuevo_contenido = 'K'
    elif dedos == [1, 1, 0, 0, 0, 1]:
            cv2.rectangle(frame, (0, 0), (100, 100), (255, 255,255), -1)
            cv2.putText(frame, 'L', (20, 80), font, 3, (0,0,0),2,cv2.LINE_AA)
            print("L")
            nuevo_contenido = 'L'
    elif dedos == [0, 1, 0, 1, 1, 1]:
            cv2.rectangle(frame, (0, 0), (100, 100), (255, 255,255), -1)
            cv2.putText(frame, 'W', (20, 80), font, 3, (0,0,0),2,cv2.LINE_AA)
            print("W")
            nuevo_contenido = 'W'
    elif dedos == [0, 1, 0, 0, 1, 1]:
            cv2.rectangle(frame, (0, 0), (100, 100), (255, 255,255), -1)
            cv2.putText(frame, 'N', (20, 80), font, 3, (0,0,0),2,cv2.LINE_AA)
            print("N")
            nuevo_contenido = 'N'
    elif dedos == [1, 1, 1, 0, 0, 0]:
            cv2.rectangle(frame, (0, 0), (100, 100), (255, 255,255), -1)
            cv2.putText(frame, 'Y', (20, 80), font, 3, (0,0,0),2,cv2.LINE_AA)
            print("Y")
            nuevo_contenido = 'Y'
    elif dedos == [1, 1, 1, 1, 1, 0]:
            cv2.rectangle(frame, (0, 0), (100, 100), (255, 255,255), -1)
            cv2.putText(frame, 'F', (20, 80), font, 3, (0,0,0),2,cv2.LINE_AA)
            print("F")
            nuevo_contenido = 'F'
    elif dedos == [0, 1, 1, 1, 1, 1]:
            cv2.rectangle(frame, (0, 0), (100, 100), (255, 255,255), -1)
            cv2.putText(frame, 'P', (20, 80), font, 3, (0,0,0),2,cv2.LINE_AA)
            print("P")
            nuevo_contenido = 'P'
    elif dedos == [0, 1, 0, 0, 1, 1]:
            cv2.rectangle(frame, (0, 0), (100, 100), (255, 255,255), -1)
            cv2.putText(frame, 'V', (20, 80), font, 3, (0,0,0),2,cv2.LINE_AA)
            print("V")
            nuevo_contenido = 'V'
    elif dedos == [1, 1, 1, 1, 1, 1]:
            cv2.rectangle(frame, (0, 0), (280, 100), (255, 255,255), -1)
            cv2.putText(frame, 'HOLA', (20, 80), font, 3, (0,0,0),2,cv2.LINE_AA)
            print("HOLA")
            nuevo_contenido = 'HOLA'

#     else:
#         nuevo_contenido = ''
    return dedos, nuevo_contenido
