#import the dependencies
import cv2 as cv
import bson
import requests
from flask import Flask, request, Response
import pickle
import zlib

app = Flask(__name__)

capture= cv.VideoCapture(0) # Set the opencv to get input from the camera

#The Client Flask method that return the frame
@app.route('/video/', methods=['GET'])
def video():
    
    if request.method == 'GET':
        while True:
            
            isTrue, frame = capture.read() # capture frames form the camera
            encode_param = [int(cv.IMWRITE_JPEG_QUALITY),85] #set the quality of the frame 
            encoded, buf =  cv.imencode('.jpg', frame, encode_param) # encode the frame using opencv with the quality selected "85"
            zlibcompression = zlib.compress(pickle.dumps(buf)) #Compress the encoded JPEG, first convert the object into a byte steam 
            return Response(zlibcompression,status=200,headers={'Content-Enconded':'b' ''}) #Response with the zlibcompression, status "ok/200",
    cv.release()
    #cv.destroyAllWindows()


if __name__ == '__main__':
    ip_address='10.33.16.17'
    ports=5000
    #Get the ip address of the client
    a=bson.BSON.encode({'ipaddress': ip_address, 'ports':ports}) #Create a bson object
    r=requests.post('http://10.33.16.19:5000/server',data=a) #Send the bson to create a connection with the server
    app.debug=True
    app.run(host=ip_address,port=ports) #Run the flask server for the client