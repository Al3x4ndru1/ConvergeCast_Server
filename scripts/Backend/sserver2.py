from flask import request, render_template, Blueprint, Flask
from flask_restful import Resource, Api, reqparse
import bson
import base64
import numpy as np
import json
import cv2 as cv
import zlib

#server = Blueprint('index',__name__)
app = Flask(__name__)
#api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('imgb64', help = 'type error')
#Create connection with the client
@app.route('/server/',methods=['POST'])
def connect():
    while True:
        data=request.data #Get a Bson
        a=bson.BSON(data).decode() #Decode the Bson
        b=a['data'] #Get the Ipaddress of the client


        #data2 = b.encode()
        data2 = base64.b64decode(b)

        #data2 = zlib.decompress(data2)

        fdata = np.frombuffer(data2, dtype=np.uint8)
        frame = cv.imdecode(fdata, 1)

        cv.imshow('test', frame)
        if cv.waitKey(20) & 0xFF == ord('d'):   # stop the video is the key 'd' is pressed (you can change as per your choice)
            break



if __name__ == '__main__':
    app.run(host='10.33.16.19', port=5000, threaded=True)