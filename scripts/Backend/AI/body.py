import cv2 as cv

full_body = cv.CascadeClassifier(cv.data.haarcascades +'haarcascade_fullbody.xml')

frame = cv.imread('./scripts/Backend/AI/Roots-1445px (1).jpg')
#gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
frame1=cv.resize(frame,(1200,720))
detection = full_body.detectMultiScale(frame1, scaleFactor= 1.005, minNeighbors=5, minSize=(50,50))
print (detection)

for (x,y,w,h) in detection:
    cv.rectangle(frame1, (x, y), (x+w, y+h), (0,255,0), 2)

cv.imshow('a',frame1)
cv.waitKey()