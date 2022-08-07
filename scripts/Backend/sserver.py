#import the dependencies
from flask import request, render_template, Blueprint, session, app
import numpy as np

import time 
from cv2 import cuda

import cv2 as cv
import bson
import pickle
import gc
import os
import zlib
#import torch
from os import environ
import threading
from threading import active_count
import requests
import cupy as cp

threads = []


# TODO: Implement Nvidia and to implemet the GUI

#from flask_bson import accept_bson, bsonify

server = Blueprint('index',__name__)

#TheClass that handles the 
class TheClass:

    def hello_world(self,s,ipaddress):
        environ["QT_DEVICE_PIXEL_RATIO"] = "0"
        environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
        environ["QT_SCREEN_SCALE_FACTORS"] = "1"
        environ["QT_SCALE_FACTOR"] = "1"
        while True:
            try:
                data= s.get(f'http://{ipaddress}:5000/video')
                decompressed = pickle.loads(zlib.decompress(data.content))
                image = np.frombuffer(decompressed, dtype=np.uint8) # interpretate the 
                frame = cv.imdecode(image, 1) # decode the image
                # tensor_a= torch.from_numpy_array(frame)
                # y= torch.tensor()
                # cv.gpu.GpuMat()
                cv.imshow('test', frame) # show images frame by frame 
            except:
                continue # sometimes the line 41 will return a error about the headers so the code will not print that frame, will skip to be able to have more fps
            if cv.waitKey(20) & 0xFF == ord('d'):   # stop the video is the key 'd' is pressed (you can change as per your choice)
                break
        cv.destroyAllWindows()

#@server.route(f'/get_video/{}')


#Create connection with the client
@server.route('/server/',methods=['POST'])
def connect():
    if request.method == 'POST':
        try:
            s = requests.Session()
            data=request.data #Get a Bson
            a=bson.BSON(data).decode() #Decode the Bson
            b=a['ipaddress'] #Get the Ipaddress of the client
            t= TheClass() #Create class of the TheClass
            thredd=threading.Thread(target=t.hello_world,args=(s,b))
            threads.append(thredd) # Put the thread at the end of the array
            thredd.start() #Start a Thread for each client
            return("OK") #Return Ok (<Response 200>)
        except:
            return ("Can not make a connection")
        
    return ("OK")

@server.route('/')
def index():
    return render_template('index.html')