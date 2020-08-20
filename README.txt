SETUP:
Since the Mask_Detection file is a project file, put it in any directory you want.
After saying FILE OPEN in PyCharm, you can select Mask_Detection and import the project.
If you want to use mask detection with the webcam, just open the MaskTespit-PcWebcam_ENG.py file.
If you want to detect the face with the phone camera, download the IP Webcam application on the phone.
Enter the ip value written below when IP Webcam service is started to the url value on line 178.



While the code is starting:

If the camera you want to use is a webcam, simply run the Mask Detect-PcWebcam.py file.
If you want to use the phone camera, you must start the service of the IP Webcam application on the phone and make sure it is on the same network as the computer.
Then just run the MaskDetection_TelephoneCamera_ENG.py file.
Note: 
-If you have problems with the libraries, we recommend you to reload them.
-Since different files have been tried in the main file of the project, they have been loaded in different libraries.
-Python Version used when writing the program: 3.7.6, Pycharm Version: 2020.2, Pip version = 20.2.2

while the code is running:

The instant Webcam Image appears on the middle screen.The faces selected by the program are drawn with a blue rectangle.
If the x, y point of the detected face is between the two green lines above, the photo is taken.
If no mask is detected in the captured photo, it will be saved in C: // screen / Unmasked file.
If there is no Screen folder and Masked face, Unmasked face folder inside, these files are created in C directory.
If there is a mask in the determined face, the mask is drawn with light blue rectangles.
If there is a mask on the face entered between two green lines, the photo is taken and saved to C: // screen / Masked face file.
The last photos taken are displayed in the frames on the right and left of the screen, respectively.
On the left are photos taken without a mask, on the right are photos taken with a mask.


