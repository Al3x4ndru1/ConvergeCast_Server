#import the dependencies
from flask import request, render_template, Blueprint
import numpy as np

from PIL import Image
import io
import cv2 as cv
import bson
import pickle
import os
import zlib

import threading
from threading import active_count
import requests
from multiprocessing import Process

from .get_video import show, ShowClass

#import eel

processes = []

# TODO: Implement Nvidia and to implemet the GUI

#from flask_bson import accept_bson, bsonify

server = Blueprint('index',__name__)

#TheClass that handles the 
class TheProces:
    #@cuda.autojit
    def hello_world(s,ipaddress):
        T_threads = []
        while True:
            try:
                data= s.get(f'http://{ipaddress}:5000/video')
                decompressed = pickle.loads(zlib.decompress(data.content))
                image = np.frombuffer(decompressed, dtype=np.uint8) # interpretate the 
                frame = cv.imdecode(image, 1) # decode the image
                # tensor_a= torch.from_numpy_array(frame)
                # y= torch.tensor()
                # cv.gpu.GpuMat()
                #return frame
                #yield (b' --frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(decompressed) + b'\r\n')
                # c = ShowClass()
                # thread = threading.Thread(target=c.show, args=(frame,))
                # T_threads.append(thread)
                # thread.start()
                #show(frame)
                #T_threads.append(thread)
                cv.imshow(ipaddress, frame) # show images frame by frame 
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
            p = TheProces
            process =Process(target=p.hello_world,args=(s,b,))
            processes.append(process) # Put the thread at the end of the array
            process.start()
            #thredd.start() #Start a Thread for each client
            return("OK") #Return Ok (<Response 200>)
        except:
            return ("Can not make a connection")
        
    return ("OK")

@server.route('/')
def index():
    return render_template('index.html')