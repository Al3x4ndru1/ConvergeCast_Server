import cv2 as cv

body_detector = cv.CascadeClassifier(cv.data.haarcascades +'haarcascade_fullbody.xml')


def full_body_detector(frame):

    height, width, channel = frame.shape

    body_detected = body_detector.detectMultiScale(frame)
    number_of_bodies = len(body_detected)
    count = number_of_bodies

    if count:
        for x,y,w,h in body_detected:
            cv.rectangle(img=body_detected,
                         pt1=(x,y), pt2=(x+h,y+h), 
                         color=(255,0,255),
                         thickness=2)
            cv.putText(img=body_detected,
                       text=f'Body {count}', 
                       org=(x,y),
                       fontFace=cv.FONT_HERSHEY_PLAIN, 
                       fontScale=2, 
                       color=(0,255), 
                       thickness=2)
            count-=1
    
    cv.putText(img=body_detected,
               text=f'Body Count = {number_of_bodies}', 
               org=(50,50),
               fontFace=cv.FONT_HERSHEY_PLAIN,
               fontScale=2, 
               color=(0,255,255), 
               thickness=2)

    return body_detected