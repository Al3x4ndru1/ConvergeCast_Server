#import the dependencies
from flask import request, render_template, Blueprint
import numpy as np
from numba import jit, cuda

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

from .static.javascript.python_js.get_video import show1

processes = []
T_threads = []

# TODO: Implement Nvidia and to implemet the GUI

#from flask_bson import accept_bson, bsonify

server = Blueprint('index',__name__)

#TheClass that handles the 
#class TheProces():
#@jit(target='cuda')
def hello_world(s,ipaddress):
    
    #T_threads = []
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
            show1(frame,ipaddress)
            #cv.imshow(ipaddress, frame) # show images frame by frame 
        except:
            continue # sometimes the line 41 will return a error about the headers so the code will not print that frame, will skip to be able to have more fps
        if cv.waitKey(20) & 0xFF == ord('d'):   # stop the video is the key 'd' is pressed (you can change as per your choice)
            break
    cv.destroyAllWindows()

#Create connection with the client
@server.route('/server/',methods=['POST'])
def connect():
    if request.method == 'POST':
        try:
            s = requests.Session()
            data=request.data #Get a Bson
            a=bson.BSON(data).decode() #Decode the Bson
            b=a['ipaddress'] #Get the Ipaddress of the client
            #p = TheProces()
            process =Process(target=hello_world,args=(s,b))
            processes.append(process) # Put the thread at the end of the list
            process.start()
            #processes[len(processes)-1].start()
            # t= TheClass() #Create class of the TheClass
            # thredd=threading.Thread(target=t.hello_world,args=(s,b))
            # threads.append(thredd) # Put the thread at the end of the array
            # thredd.start() #Start a Thread for each client
            return("OK") #Return Ok (<Response 200>)

            #thredd.start() #Start a Thread for each client
        except:
            return ("Can not make a connection")
        
    return ("OK")

@server.route('/')
def index():
    return render_template('index.html')