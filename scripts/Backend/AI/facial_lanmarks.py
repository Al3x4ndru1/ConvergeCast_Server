
import cv2 as cv
import dlib
from numba import jit, cuda


hog_model = dlib.get_frontal_face_detector()

fp_model = dlib.shape_predictor('./scripts/Backend/AI/68/shape_predictor_81_face_landmarks.dat')

#@jit(target_backend='cuda')
def landmark_detection(frame):
    '''
    hog_model : hog classifier object
    fp_model : 81 facial point predictor object 
    '''
    hog_face_detector = hog_model
    point_predictor = fp_model

    face_detected = hog_face_detector(frame)

    face_count = len(face_detected)

    ## face count
    cv.putText(img=frame,
               text=f'Face Count = {face_count}',
               color=(0,255,255),
               org=(50,50),fontFace=cv.FONT_HERSHEY_PLAIN,
               thickness=2, 
               fontScale=2
               )

    for face in face_detected:
        t,b,l,r=  face.top(), face.bottom(), face.left(), face.right()
        points = fp_model(frame, face)
        
        #mark face
        cv.rectangle(img=frame, 
                     pt1=(l,t), pt2=(r,b), 
                     color=(0,255,0), thickness=2) 
        ## Face label 
        cv.putText(img=frame,
                    text=f'Face {face_count}',
                    color=(255,0,255),
                    org=(l,t-10),fontFace=cv.FONT_HERSHEY_PLAIN, 
                    thickness=3,
                    fontScale=2
                    )
        face_count-=1

        ## plot points
        for point in points.parts():
            cv.circle(img=frame, 
                      center=(point.x, point.y), radius=2, 
                      color=(0,0,255), thickness=-1)
    return frame