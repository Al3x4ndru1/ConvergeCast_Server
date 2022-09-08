from wsgiref import headers
import zlib
import cv2 as cv
import bson
import requests
from flask import Flask, request, Response, make_response
import pickle

# additinal_headers['content-encodingf'] = 'gzip'

app = Flask(__name__)
#headers = {'Content-type': 'text/'} , header = {'Accept-Ranges','bytes'}
capture= cv.VideoCapture(0)

@app.route('/video/', methods=['GET'])
def video():
    #waith untill I get an other respinse
    if request.method == 'GET':
        while True:
            isTrue, frame = capture.read() 
            encode_param = [int(cv.IMWRITE_JPEG_QUALITY),85]
            encoded, buf =  cv.imencode('.jpg', frame,encode_param)
            copress = zlib.compress(pickle.dumps(buf))
            resp = Response(copress,status=200, headers={'Content-Encoding': 'b' ''})
            # resp.headers['Content-Encoding'] = 'b' '
            return  resp
 

 

if __name__ == '__main__':
    ip_address='10.33.16.13'
    ports=5000
    a=bson.BSON.encode({'ipaddress': ip_address, 'ports':ports})
    r=requests.post('http://10.33.16.19:5000/server',data=a)
    #print(r)
    app.run(host=ip_address,port=ports)
