# Detecção do QRCode
from datetime import datetime
start_time = datetime.now()
import cv2
import numpy as np # NumPy é uma Python library usada para trabalhar com arrays.
from pyzbar.pyzbar import decode


cap = cv2.VideoCapture(0)


while True:
    success, img = cap.read()

    # code = decode(img) #vai me dar todas as infos da imagem como largura, altura, tipo, etc
    for barcode in decode(img):
        # print(barcode.data)
        myData = barcode.data.decode('utf-8')  # faz a leitura do QR Code

        end_time = datetime.now()
        print('Duration: {}'.format(end_time - start_time)) #Mede a diferença entre tempo de início e tempo final

        print(myData)
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(0,69,255),5) # parâmetros da "moldura" do QR Code, com parâmetros das linhas
        pts2 = barcode.rect
        cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,69,255),2)

    cv2.imshow('Result',img)
    key=cv2.waitKey(1)
    if key ==27: # APERTA 'ESC' PARA FECHAR O CÓDIGO
        break

