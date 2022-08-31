import cv2 as cv

face_detector = cv.CascadeClassifier(cv.data.haarcascades +'haarcascade_frontalface_default.xml')

def face_detect(frame, scale):
    '''
    Input : Frame 
    output: Frame with face detected 
    '''
    height, width, channel = frame.shape
    if scale == 1:
        frame_scalled = frame
    else:
        frame_scalled = cv.resize(frame,                                                   # source image 
                                (int(width * scale), int(height * scale)),  # target resolution 
                                interpolation=cv.INTER_AREA
                        )  
    #frame_gr = cv.cvtColor(frame_scalled, cv.COLOR_BGR2GRAY)
    face_detected = face_detector.detectMultiScale(frame)
    number_of_faces = len(face_detected)
    count = number_of_faces
    if count:
        for x,y,w,h in face_detected:
            cv.rectangle(img=frame_scalled,
                         pt1=(x,y), pt2=(x+h,y+h), 
                         color=(255,0,255),
                         thickness=2)
            cv.putText(img=frame_scalled,
                       text=f'Face {count}', 
                       org=(x,y),
                       fontFace=cv.FONT_HERSHEY_PLAIN, 
                       fontScale=2, 
                       color=(0,255), 
                       thickness=2)
            count-=1
    
    cv.putText(img=frame_scalled,
               text=f'Face Count = {number_of_faces}', 
               org=(50,50),
               fontFace=cv.FONT_HERSHEY_PLAIN,
               fontScale=2, 
               color=(0,255,255), 
               thickness=2)
    return frame_scalled