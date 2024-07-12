import cv2
import mediapipe as mp

# inicializar opencv e mediapipe
webcam = cv2.VideoCapture(0)  # Indentificando a camera por opencv 1   4 5 6 7 8 9
reconhecimento_rosto = mp.solutions.face_detection  # criando a classe de reconhecimento
reconhecedor_rosto = reconhecimento_rosto.FaceDetection()  # criando o reconhecedor
desenho = mp.solutions.drawing_utils  # iniciando o desenhador

while True:
    # Ler informações da webcam
    verificador, frame = webcam.read()  # Verificador recebe um True ou False se a conseguiu ler a camera ou não
    # Frame recebe a informação da webcam
    if not verificador:
        break

    # Reconhecer os rostos
    lista_rostos = reconhecedor_rosto.process(frame)  # Processa o frame para ver se existe algum rosto

    if lista_rostos.detections:  # Setiver rostos na detecção
        for rosto in lista_rostos.detections:  # Para cada rosto na detecção
            desenho.draw_detection(frame, rosto)  # Desenha dentro do frame o rosto

    cv2.imshow("Janela", frame)

    # Quando apertar ESC(tecla 27), para o loop
    if cv2.waitKey(5) == 27:
        break

webcam.release()  # Libera a camera
cv2.destroyAllWindows()  # Desliga as janelas
