import cv2 as cv
#from training.training import test


face_detector = cv.CascadeClassifier(cv.data.haarcascades +'haarcascade_frontalface_default.xml') # initialize the cascade object to find the frontal faces
face_recognizer = cv.face.LBPHFaceRecognizer_create() # initialize the face LBHF face recognizer
face_recognizer.read("scripts/Backend/AI/training/classifiers/lbpg_classifier.yml") #the classifier that is created for our case
font = cv.FONT_HERSHEY_COMPLEX_SMALL
width, height = 220,220

#print(test)

def faceName(frame):
    frame_gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY) # transform the image from color image to Gray image, 
                                                      # because the LBHF classifier is working with gray images

    detection = face_detector.detectMultiScale(frame) # take the faces 
    
    for (x,y,w,h) in detection:
        image_face = cv.resize(frame_gray[y:y+w, x:x+h], (width, height)) # resize the face image
        cv.rectangle(frame, (x,y), (x+w,y+h), (0,0,225), 2) # draw the rectangle
        id, confidence = face_recognizer.predict(frame_gray) # call the recognizer and get the id of that face and the confidence
        
        name = ""
        if id == 1:
            name = 'Alex'
        elif id == 2:
            name = 'Godwin'

        cv.putText(frame, name, (x,y+(w+30)), font, 2, (0,0,255)) # Put the name for that person on the bottom of the rectangle
        cv.putText(frame, str(confidence), (x,y+(h+50)), font, 1, (0,0,255)) # put the confidence on the bottom of the name of that person detected
    
    return frame # return the image