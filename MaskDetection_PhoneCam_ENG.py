import os

import cv2
import sys

import numpy as np
import requests
from PyQt5.QtWidgets import  QWidget, QLabel, QApplication
from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
from PyQt5 import  QtGui
from PyQt5 import QtCore


faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml") #Face detection classifier
maskCascade = cv2.CascadeClassifier("Resources/haarcascade_mask.xml") #mask detection classifier
masked_face_list=[]  #list holding masked faces
unmasked_face_list=[] #list holding unmasked faces

os.chdir('C:\\')   #Creates this file if there is no file named screen in directory C
url = 'C:\\screen'
if os.path.exists(url) == False:
    os.mkdir('screen')


def number_of_files():  #Creates if there is no masked and unmasked file. If there are files, it returns the number of elements in these files.
    os.chdir('C:\\screen')
    url = 'C:\\screen' + '\\' + 'Masked face'
    if os.path.exists(url) == False:
        os.mkdir('Masked face')
    os.chdir('C:\\screen\\Masked face')
    c = len(os.listdir()) + 1

    os.chdir('C:\\screen')
    url = 'C:\\screen' + '\\' + 'Unmasked face'
    if os.path.exists(url) == False:
        os.mkdir('Unmasked face')
    os.chdir('C:\\screen\\Unmasked face')
    c2 = len(os.listdir()) + 1
    return c,c2



def face_detection(img,c1,c2):   #face detection application c1,c2=Number of elements in masked, unmasked file

    faces = faceCascade.detectMultiScale(img, 1.1, 4) #Faces detected in img image are thrown into faces array,
    gate_control = False
    mask_check = False
    face_control=False
    cv2.line(img, (0, 70), (1000, 70), (0, 255, 0), 2)  #Draws the threshold range
    cv2.line(img, (0, 80), (1000, 80), (0, 255, 0), 2)
    for (x,y,w,h) in faces: #for coordinates and dimensions of each face
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)  #rectangles are drawn in the position of the face
        face_control=True
        gate_control = False
        mask_check = False

        cv2.waitKey(1)


        if y > 70 and y < 80: ##if the face is within the specified scratch range


            gate_control=True

        mask_check=find_mask(img, x, y, h, w)  #The mask is checked by giving the coordinates and dimensions of the face
        if(mask_check)==True and gate_control==True: #if there is a mask and the face is within the threshold
            myScreenshot = img[y:y + h, x:x + w]  #photo is cropped

            os.chdir('C:\\screen') #If there is no masked file it is created and the photo is thrown into the file
            url = 'C:\\screen' + '\\' + 'Masked face'

            if os.path.exists(url) == False:
                os.mkdir('Masked face')

            cv2.imwrite('C:\\screen\\' + 'Masked face' + '\ekran' + str(c1) + '.jpg', myScreenshot)
            file_name='C:\\screen\\' + 'Masked face' + '\ekran' + str(c1) + '.jpg'
            masked_face_list.append(file_name) #the location of the photo is added to the list
            if len(masked_face_list) == 1:  #If there is only one element in the list, the photo is printed in the first box on the right.

                ex.label5.setPixmap(QtGui.QPixmap(masked_face_list.__getitem__(len(masked_face_list) - 1)))

            # If there is more than one, the last element is pressed in the first box, the others scroll down one
            elif len(masked_face_list) == 2: #If there is more than one, the last element is pressed in the first box, the others scroll down one

                ex.label5.setPixmap(QtGui.QPixmap(masked_face_list.__getitem__(len(masked_face_list) - 1)))
                ex.label6.setPixmap(QtGui.QPixmap(masked_face_list.__getitem__(len(masked_face_list) - 2)))


            elif len(masked_face_list) == 3:
                ex.label5.setPixmap(QtGui.QPixmap(masked_face_list.__getitem__(len(masked_face_list) - 1)))
                ex.label6.setPixmap(QtGui.QPixmap(masked_face_list.__getitem__(len(masked_face_list) - 2)))
                ex.label7.setPixmap(QtGui.QPixmap(masked_face_list.__getitem__(len(masked_face_list) - 3)))

            elif len(masked_face_list) >= 4:

                ex.label5.setPixmap(QtGui.QPixmap(masked_face_list.__getitem__(len(masked_face_list) - 1)))
                ex.label6.setPixmap(QtGui.QPixmap(masked_face_list.__getitem__(len(masked_face_list) - 2)))
                ex.label7.setPixmap(QtGui.QPixmap(masked_face_list.__getitem__(len(masked_face_list) - 3)))
                ex.label8.setPixmap(QtGui.QPixmap(masked_face_list.__getitem__(len(masked_face_list) - 4)))




        if (mask_check) ==False and gate_control==True: #the same operations are done for the unmasked folder if there is no mask on the face while in the threshold range and the boxes on the right are filled.
            myScreenshot = img[y:y + h, x:x + w]
            file_name='C:\\screen\\' + 'Unmasked face' + '\ekran' + str(c2) + '.jpg'
            os.chdir('C:\\screen')
            url = 'C:\\screen' + '\\' + 'Unmasked face'
            if os.path.exists(url) == False:
                os.mkdir('Unmasked face')

            cv2.imwrite('C:\\screen\\' + 'Unmasked face' + '\ekran' + str(c2) + '.jpg', myScreenshot)
            unmasked_face_list.append(file_name)
            if len(unmasked_face_list)==1:

                ex.label1.setPixmap(QtGui.QPixmap(unmasked_face_list.__getitem__(len(unmasked_face_list) - 1)))

            elif len(unmasked_face_list)==2:

                ex.label1.setPixmap(QtGui.QPixmap(unmasked_face_list.__getitem__(len(unmasked_face_list) - 1)))
                ex.label2.setPixmap(QtGui.QPixmap(unmasked_face_list.__getitem__(len(unmasked_face_list) - 2)))


            elif len(unmasked_face_list)==3:
                ex.label1.setPixmap(QtGui.QPixmap(unmasked_face_list.__getitem__(len(unmasked_face_list) - 1)))
                ex.label2.setPixmap(QtGui.QPixmap(unmasked_face_list.__getitem__(len(unmasked_face_list) - 2)))
                ex.label3.setPixmap(QtGui.QPixmap(unmasked_face_list.__getitem__(len(unmasked_face_list) - 3)))

            elif len(unmasked_face_list)>=4:
                ex.label1.setPixmap(QtGui.QPixmap(unmasked_face_list.__getitem__(len(unmasked_face_list) - 1)))
                ex.label2.setPixmap(QtGui.QPixmap(unmasked_face_list.__getitem__(len(unmasked_face_list) - 2)))
                ex.label3.setPixmap(QtGui.QPixmap(unmasked_face_list.__getitem__(len(unmasked_face_list) - 3)))
                ex.label4.setPixmap(QtGui.QPixmap(unmasked_face_list.__getitem__(len(unmasked_face_list) - 4)))




    if gate_control==True and mask_check==True:
        return 1,1
    if gate_control == True and mask_check == False:
        return 1, 0
    if gate_control==False and mask_check==True:
        return 0,1
    if gate_control==False and mask_check==False:
        return 0,0




def find_mask(img1, x, y, w, h):   # function finding a mask in given coordinates and dimensions

    contours = maskCascade.detectMultiScale(img1, 1.1, 4)  # assigns detected masks to the contours array
    Is_it_masked = False

    for (x1,y1,w1,h1) in contours: #for the coordinates and dimensions of each mask detected

            if abs(x-x1) < (w)*0.1  and abs(y-y1)<(h)*0.1  : # if the mask coordinates are too close to the face coordinates


                cv2.rectangle(img1, (int(x1), int(y1+(h1/2))), (x + w, y + h), (233, 213, 21), 3)  # Draws a rectangle half the width for the mask because the mask coordinate is close to the face coordinate
                Is_it_masked = True


    return Is_it_masked      #returns true if mask exists otherwise false



class Thread(QThread):  #the classroom in the middle of the window that creates a webcam
    changePixmap = pyqtSignal(QImage)


    def run(self):
        cap = cv2.VideoCapture(0) #webcam reference is taken
        c,c2=number_of_files()  #The number of elements in the masked and unmasked files is taken and used as a counter
        while True:
            ret, frame = cap.read() #read from webcam
            url = 'http://192.168.43.1:8080/shot.jpg' # address to take snapshots
            if ret: #if reading is successful

                img_resp = requests.get(url)
                img_array = np.array(bytearray(img_resp.content), dtype=np.uint8)
                frame = cv2.imdecode(img_array, -1)
                frame = cv2.flip(frame, 1) #Inverted on the x-axis to be a mirror image

                b, b2 = face_detection(frame, c,c2)  #Face detection is queried, b = 1 if there is a face and it has passed the threshold, b2 returns 1 if there is a mask, 0 if there is no
                if b==1:  #if the face is detected and crossed the threshold
                    if b2==1:  # Increase the counter of the mask by one if there is a mask (example: if the last file is screen3, the next element is screen4
                        c = 1 + c
                    else:
                        c2 = 1 + c2  ##If there is no mask, increase the unmasked counter by one (example: if the last file is screen3, the next element is screen4)






                    #the bottom 5 lines display the frame object of type numpy array in the middle of the widget.
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
                p = convertToQtFormat.scaled(1280, 960, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)
                cv2.waitKey(1)




class App(QWidget): #the class that created the window that appears on the main screen
    def __init__(self):
        super().__init__()
        [...]
        self.initUI()

    @pyqtSlot(QImage)
    def setImage(self, image):
        self.label.setPixmap(QPixmap.fromImage(image))

    def initUI(self):  #The necessary settings for the window are made and the necessary position adjustments are made for the photos
        self.setWindowTitle("mask detection")
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


        #for to have a webcam view  in the middle  of the window
        th = Thread(self)
        th.changePixmap.connect(self.setImage)
        th.start()
        self.show()



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = App()  #the object that creates the window is defined

    sys.exit(app.exec_())  #the program runs until the window is closed


