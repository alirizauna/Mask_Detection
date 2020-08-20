import os

import numpy as np
import requests
import cv2
import sys
from PyQt5.QtWidgets import  QWidget, QLabel, QApplication
from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
from PyQt5 import  QtGui
from PyQt5 import QtCore


faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml") #Yüz tespiti yapan sınıflandırıcı
maskCascade = cv2.CascadeClassifier("Resources/haarcascade_mask.xml") #maske tespiti yapan sınıflandırıcı
maskeli_liste=[]  #maskeli yüzleri tutan liste
maskesiz_liste=[] #maskesiz yüzleri tutan liste

os.chdir('C:\\')   # C dizininde screen adlı dosya yoksa bu dosyayı oluşturur
url = 'C:\\screen'
if os.path.exists(url) == False:
    os.mkdir('screen')


def dosya_sayilari():  #maskeli ve maskesiz dosyası yoksa oluşturur ve dosyalar varsa bu dosyalardaki eleman sayılarını döndürür
    os.chdir('C:\\screen')
    url = 'C:\\screen' + '\\' + 'Maskeli'
    if os.path.exists(url) == False:
        os.mkdir('Maskeli')
    os.chdir('C:\\screen\\Maskeli')
    c = len(os.listdir()) + 1

    os.chdir('C:\\screen')
    url = 'C:\\screen' + '\\' + 'Maskesiz'
    if os.path.exists(url) == False:
        os.mkdir('Maskesiz')
    os.chdir('C:\\screen\\Maskesiz')
    c2 = len(os.listdir()) + 1
    return c,c2



def yuz_tespit(img,c1,c2):   #yüz tespit eden uygulama c1,c2=maskeli,maskesiz dosyasındaki eleman sayıları

    faces = faceCascade.detectMultiScale(img, 1.1, 4) #img görüntüsünde tespit edilen yüzler faces dizisine atılır,
    gecit_kontrol = False
    maske_varmı = False
    yuz_kontrol=False
    cv2.line(img, (0, 70), (1000, 70), (0, 255, 0), 2)  #eşik aralığını çizer
    cv2.line(img, (0, 80), (1000, 80), (0, 255, 0), 2)
    for (x,y,w,h) in faces: #her yüzün koordinat ve boyutları için
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)  #yüzün konumuna dikdörtgenler çizilir
        yuz_kontrol=True
        gecit_kontrol = False
        maske_varmı = False

        cv2.waitKey(1)


        if y > 70 and y < 80: ##yüz,belirlenen çizik aralığındaysa


            gecit_kontrol=True

        maske_varmı=maskeBul(img, x, y, h, w)  #yüzün koordinatları ve boyutları verilerek maske  kontrol edilir
        if(maske_varmı)==True and gecit_kontrol==True: #maske varsa ve yüz eşik aralığındaysa
            myScreenshot = img[y:y + h, x:x + w]  #fotoğraf kırpılır

            os.chdir('C:\\screen') #maskeli dosyası yoksa oluşturulur ve fotoğraf dosyaya atılır
            url = 'C:\\screen' + '\\' + 'Maskeli'

            if os.path.exists(url) == False:
                os.mkdir('Maskeli')

            cv2.imwrite('C:\\screen\\' + 'Maskeli' + '\ekran' + str(
                c1) + '.jpg', myScreenshot)
            dosya_adi='C:\\screen\\' + 'Maskeli' + '\ekran' + str(
                c1) + '.jpg'
            maskeli_liste.append(dosya_adi) #fotoğrafın konumu listeye atılır
            if len(maskeli_liste) == 1:  #listede tek eleman varsa sağ taraftaki ilk kutuya fotoğraf basılır

                ex.label5.setPixmap(QtGui.QPixmap(maskeli_liste.__getitem__(len(maskeli_liste) - 1)))

            # birden fazla  varsa son eleman ilk kutuya basılır diğerleri bir aşağı kayar
            elif len(maskeli_liste) == 2: #birden fazla  varsa son eleman ilk kutuya basılır diğerleri bir aşağı kayar

                ex.label5.setPixmap(QtGui.QPixmap(maskeli_liste.__getitem__(len(maskeli_liste) - 1)))
                ex.label6.setPixmap(QtGui.QPixmap(maskeli_liste.__getitem__(len(maskeli_liste) - 2)))


            elif len(maskeli_liste) == 3:
                ex.label5.setPixmap(QtGui.QPixmap(maskeli_liste.__getitem__(len(maskeli_liste) - 1)))
                ex.label6.setPixmap(QtGui.QPixmap(maskeli_liste.__getitem__(len(maskeli_liste) - 2)))
                ex.label7.setPixmap(QtGui.QPixmap(maskeli_liste.__getitem__(len(maskeli_liste) - 3)))

            elif len(maskeli_liste) >= 4:

                ex.label5.setPixmap(QtGui.QPixmap(maskeli_liste.__getitem__(len(maskeli_liste) - 1)))
                ex.label6.setPixmap(QtGui.QPixmap(maskeli_liste.__getitem__(len(maskeli_liste) - 2)))
                ex.label7.setPixmap(QtGui.QPixmap(maskeli_liste.__getitem__(len(maskeli_liste) - 3)))
                ex.label8.setPixmap(QtGui.QPixmap(maskeli_liste.__getitem__(len(maskeli_liste) - 4)))




        if (maske_varmı) ==False and gecit_kontrol==True: #aynı işlemler eşik aralığındayken yüzde maske yoksa maskesiz klasörü için yapılır ve sağ taraftaki kutular doldurulur
            myScreenshot = img[y:y + h, x:x + w]
            dosya_adi='C:\\screen\\' + 'Maskesiz' + '\ekran' + str(
                c2) + '.jpg'
            os.chdir('C:\\screen')
            url = 'C:\\screen' + '\\' + 'Maskesiz'
            if os.path.exists(url) == False:
                os.mkdir('Maskesiz')

            cv2.imwrite(
                'C:\\screen\\' + 'Maskesiz' + '\ekran' + str(
                    c2) + '.jpg', myScreenshot)
            maskesiz_liste.append(dosya_adi)
            if len(maskesiz_liste)==1:

                ex.label1.setPixmap(QtGui.QPixmap(maskesiz_liste.__getitem__(len(maskesiz_liste)-1)))

            elif len(maskesiz_liste)==2:

                ex.label1.setPixmap(QtGui.QPixmap(maskesiz_liste.__getitem__(len(maskesiz_liste) - 1)))
                ex.label2.setPixmap(QtGui.QPixmap(maskesiz_liste.__getitem__(len(maskesiz_liste) - 2)))


            elif len(maskesiz_liste)==3:
                ex.label1.setPixmap(QtGui.QPixmap(maskesiz_liste.__getitem__(len(maskesiz_liste) - 1)))
                ex.label2.setPixmap(QtGui.QPixmap(maskesiz_liste.__getitem__(len(maskesiz_liste) - 2)))
                ex.label3.setPixmap(QtGui.QPixmap(maskesiz_liste.__getitem__(len(maskesiz_liste) - 3)))

            elif len(maskesiz_liste)>=4:
                ex.label1.setPixmap(QtGui.QPixmap(maskesiz_liste.__getitem__(len(maskesiz_liste) - 1)))
                ex.label2.setPixmap(QtGui.QPixmap(maskesiz_liste.__getitem__(len(maskesiz_liste) - 2)))
                ex.label3.setPixmap(QtGui.QPixmap(maskesiz_liste.__getitem__(len(maskesiz_liste) - 3)))
                ex.label4.setPixmap(QtGui.QPixmap(maskesiz_liste.__getitem__(len(maskesiz_liste) - 4)))




    if gecit_kontrol==True and maske_varmı==True:
        return 1,1
    if gecit_kontrol == True and maske_varmı == False:
        return 1, 0
    if gecit_kontrol==False and maske_varmı==True:
        return 0,1
    if gecit_kontrol==False and maske_varmı==False:
        return 0,0




def maskeBul(img1, x, y, w, h):   # verilen koordinat ve boyutlarda maske bulan fonksiyon

    contours = maskCascade.detectMultiScale(img1, 1.1, 4)  # tespit edilen maskeleri contours dizisine atar
    maske_varmi = False

    for (x1,y1,w1,h1) in contours: #tespit edilen her maskenin koordinat ve boyutları için

            if abs(x-x1) < (w)*0.1  and abs(y-y1)<(h)*0.1  : # maske koordinatları yüz koordinatlarına çok yakınsa


                cv2.rectangle(img1, (int(x1), int(y1+(h1/2))), (x + w, y + h), (233, 213, 21), 3)  # maske koordinatı yüz koordinatına .ok yakın olduğu için  maske için genişliğin yarısı kadar dikdörtgen çizer
                maske_varmi = True


    return maske_varmi      #maske varsa true yoksa false döndürür



class Thread(QThread):  #pencerenin ortasında webcam görüntüsü oluşturan sınıf
    changePixmap = pyqtSignal(QImage)


    def run(self):
        url = 'http://192.168.43.1:8080/shot.jpg' #anlık ekran görüntülerinin alınacağı adres
        cap = cv2.VideoCapture(0) #webcam referansı alınır
        c,c2=dosya_sayilari()  #maskeli,maskesiz dosyalarındaki eleman sayısı alınır ve sayaç olarak kullanılır.
        while True:
            #ret, frame = cap.read() #webcamden okunur

            if True: #okuma başarılıysa
                #frame nesnesi opencv için hazır hale getirilir
                img_resp = requests.get(url)
                img_array = np.array(bytearray(img_resp.content), dtype=np.uint8)
                frame = cv2.imdecode(img_array, -1)

                frame = cv2.flip(frame, 1) #ayna görüntüsü olması için x ekseninde ters döndürülür

                b, b2 = yuz_tespit(frame, c,c2)  #yüz tespiti sorgulanır , b=yüz varsa ve eşikten geçtiyse 1 döner,maske varsa b2 1 döner yoksa 0 döner
                if b==1:  #yüz tespit edilip eşikten geçtiyse
                    if b2==1:  #maske varsa maske sayacını bir  arttır (örnek: son dosya ekran3 ise sıradaki elemanın ekran4 olması için)
                        c = 1 + c
                    else:
                        c2 = 1 + c2  ##maske yoksa maskesiz sayacını bir  arttır (örnek: son dosya ekran3 ise sıradaki elemanın ekran4 olması için)






                    #alttaki 5 satır numpyarray tipindeki frame nesnesini widgetın ortasında  gösterir
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
                p = convertToQtFormat.scaled(1280, 960, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)
                cv2.waitKey(1)




class App(QWidget): #ana ekranda gözüken pencereyi oluşturan sınıf
    def __init__(self):
        super().__init__()
        [...]
        self.initUI()

    @pyqtSlot(QImage)
    def setImage(self, image):
        self.label.setPixmap(QPixmap.fromImage(image))

    def initUI(self):  #pencere için gerekli ayarlar verilir ve fotoğraflar için gerekli konum ayarlamaları yapılır
        self.setWindowTitle("Maske Tespit")
        self.setGeometry(0, 0, 2160, 1440)
        self.move(0,0)

        self.label = QLabel(self)
        self.label.setGeometry(QtCore.QRect(300, 10, 1280, 960))

        self.label1 = QLabel(self)
        self.label1.move(10, 10)
        self.label1.resize(220, 220)
        self.label1.setMaximumSize(480,480)
        self.label1.setScaledContents(True)

        self.label2 = QLabel(self)
        self.label2.move(10,260)
        self.label2.resize(220, 220)

        self.label2.setScaledContents(True)



        self.label3 = QLabel(self)
        self.label3.move(10, 510)
        self.label3.resize(220, 220)
        self.label3.setMaximumSize(480,480)
        self.label3.setScaledContents(True)

        self.label4 = QLabel(self)
        self.label4.move(10, 760)
        self.label4.resize(220, 220)
        self.label4.setMaximumSize(480, 480)
        self.label4.setScaledContents(True)

        self.label5 = QLabel(self)
        self.label5.move(1650, 10)
        self.label5.resize(220, 220)
        self.label5.setMaximumSize(480, 480)
        self.label5.setScaledContents(True)

        self.label6 = QLabel(self)
        self.label6.move(1650, 260)
        self.label6.resize(220, 220)

        self.label6.setScaledContents(True)

        self.label7 = QLabel(self)
        self.label7.move(1650, 510)
        self.label7.resize(220, 220)

        self.label7.setMaximumSize(480, 480)
        self.label7.setScaledContents(True)

        self.label8 = QLabel(self)
        self.label8.move(1650, 760)
        self.label8.resize(220, 220)

        self.label8.setMaximumSize(480, 480)
        self.label8.setScaledContents(True)


        #pencerenin orta kısmında webcam görüntüsü olması için
        th = Thread(self)
        th.changePixmap.connect(self.setImage)
        th.start()
        self.show()



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = App()  #pencere oluşturan nesne tanımlanır

    sys.exit(app.exec_())  #pencere kapatılana kadar program çalışır


