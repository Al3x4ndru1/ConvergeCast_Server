#import the dependencies
from flask import request, render_template, Blueprint
import numpy as np
from numba import jit, cuda,njit

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
from .AI.face_detecetion import face_detect
from .AI.facial_lanmarks import landmark_detection
from .AI.body_detection import full_body_detector

from .get_video import show1
import jyserver.Flask  as jsf


processes = []
T_threads = []

# TODO: Implement Nvidia and to implemet the GUI

#from flask_bson import accept_bson, bsonify

server = Blueprint('index',__name__)
#jit(target_backend='cuda')
#@nb.njit()
#@jit(nopython=True)
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
            # c = ShowClass()
            # thread = threading.Thread(target=c.show, args=(image,))
            # T_threads.append(thread)

            # T_threads.append(thread)
            # T_threads[len(T_threads)-1].start()
            # T_threads[len(T_threads)-1].join()
            #show(frame)
            #T_threads.append(thread)
            #show1(frame,ipaddress)
            #a=face_detect(frame,1)
            a= landmark_detection(frame)
            #a= full_body_detector(frame)
            cv.imshow(ipaddress, a) # show images frame by frame 
            # a = App(frame,ipaddress)
            # thread = threading.Thread(target=a.show, args=())
            # T_threads.append(thread)
            # T_threads[len(T_threads)-1].start()
            # T_threads[len(T_threads)-1].join()
        except:
            continue # sometimes the line 41 will return a error about the headers so the code will not print that frame, will skip to be able to have more fps
        if cv.waitKey(20) & 0xFF == ord('d'):   # stop the video is the key 'd' is pressed (you can change as per your choice)
            break
    cv.release()
    cv.destroyAllWindows()


# @jsf.use(server)
# class App:
#     def __init__(self, bframe, bipaddress):
#         self.aframe = bframe
#         self.ipaddress = bipaddress

#     def show(self):
#         #cv.imshow(ipaddress,frame)
#         print(1)
#         self.self.js.document.getElementById('input_image').innerHTML = self.aframe


#Create connection with the client
@server.route('/server/',methods=['POST'])
def connect():
    if request.method == 'POST':
        try:
            s = requests.Session()
            data=request.data #Get a Bson
            a=bson.BSON(data).decode() #Decode the Bson
            b=a['ipaddress'] #Get the Ipaddress of the client
            process =Process(target=hello_world,args=(s,b))
            processes.append(process) # Put the thread at the end of the list
            processes[len(processes)-1].start()

            return("OK") #Return Ok (<Response 200>)

        except:
            return ("Can not make a connection")
        
    return ("OK")

@server.route('/')
def index():
    return render_template('index.html')      # App.render(render_template('index.html')) 