# ConvergeCast

## Overview

> _"venv" filder is your environment so you need to be in the environment be able to perform correctly_

> _You have to run the install_linux.sh or install)windows.bat to be sure you are up to date with te dependencies_

> _If you wanto to commit your changes and you are on linux just type: "./commit.sh" type space and type the name of your commit it can be anything_

> _If you want to delete your changes from your pc and you are on linux just type: "./delete.sh"_


-----------------------------------------------

# Memory management

![](figs/Screenshot%20from%202022-08-04%2019-47-16.png)

-----------------------------------------------

# Network management

## Camera Network


![](figs/camera_network)

This is the first version of the project that works. For a 640x480 video with 45~50 fps video the network packets requier is 98 maximum.

Problem:

The amount of packets can be reduce at 85 ~ 87 and we can obtain a bit more frames per second but the session must be stable, because now the session is not as stable as I excepted.

-----------------------------------------------

## 1 second of Youtube video

![](figs/all_network)

The black line is network packets require for a 720x480 with 45 fps video on Youtube for just 1 second watching.

-----------------------------------------------

## The Backend

### Python

#### Server

> The main.py


```python
# import dependecies
from flask import Flask, render_template
from scripts.Backend import create_app

app = Flask(__name__)

app = create_app() # create_app function

if __name__ == '__main__':                  # main function
    app.run(host='10.33.16.19', port=5000)  # the flask app will run on the specific host and the default port 5000
```

This is the main function for the server. First 2 lines are for importing the dependencies, Flask and the create_app function from the Backend folder.


> The __init__.py


```python
# import dependecies
from flask import Flask
from .sserver import server

def create_app():
    app = Flask(__name__)
    app.register_blueprint(server,url_prefix='/')

    return app


```



> The get_video.py


```python
#importing dependencies
from cgitb import enable
import cv2 as cv
from os import environ
import matplotlib.pyplot as plt
from pylab import *
import base64

import js2py
from js2py import require


from numba import jit, cuda

# TODO: https://pypi.org/project/drawnow/ imshow

environ["QT_DEVICE_PIXEL_RATIO"] = "0"
environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
environ["QT_SCREEN_SCALE_FACTORS"] = "1"
environ["QT_SCALE_FACTOR"] = "1"

def show1(frame,ipaddress):
    shoow = js2py.require('')

    numplusm= """
 
    
    const ShowImageJavaScript = require("./javascript/video/check_first_checkbox").ShowImageJavaScript;
    
    function GetFirstCheckbox(){
        
        <check_first_checkbox> = require('<check_first_checkbox>');
        var.put(u'<variable name>', var.get(u'require')(Js(u'<check_first_checkbox>')));
        var.put(u'<variable name>', <check_first_checkbox>);
        var check = ShowImageJavaScript(); // call tha JavaScript function from the check_first_checkbox file
        return check; // return the check variable
    }
    """


    a = js2py.eval_js(numplusm)
    a.js2py.EvalJS(enable_require=True)
    b=a()
    print(b)
    # if(a()==2):
    #     javascript2 =  """"
    #         import "./js/opencv.js";
    #         function ShowImageJavaScript(ipaddress,frame){
    #             cv.imshow(ipaddress,frame)
    #         }
    #     """
    #     b= js2py.eval_js(javascript2)
    #     b(ipaddress,frame)

    #cv.imshow('test',frame)
    #self.stop()
```



> The sserver.py


```python
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

from .static.javascript.python.get_video import show1

processes = []
T_threads = []

# TODO: Implement Nvidia and to implemet the GUI

#from flask_bson import accept_bson, bsonify

server = Blueprint('index',__name__)

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
            process =Process(target=hello_world,args=(s,b))
            processes.append(process) # Put the thread at the end of the list
            processes[processes.length - 1].start() # Start a process for each client
            return("OK") #Return Ok (<Response 200>)

        except:
            return ("Can not make a connection")
        
    return ("OK")

@server.route('/')
def index():
    return render_template('index.html')
```

The default function is the _server.route('/')_ , which will render the HTML page. Is the only Flask function which is call internal.

-------------------------------------------

The _server.route('/server/')_ function is called by the client to create a connection to the server. This function will receive a 'POST' request from the client, which contains a BSON. The next step is to create a network session, for the process that will be create. The function will get the BSON and decode it, get the IPAddress of he client who want to create a connection and initialize a process which will have that network session and that IPAddress. The process will be append to a list and after will start the process. While the process is running function will return the OK response (<Response 200>) and it will be available for other clients.

Problems:
At this stage we have a problem in terms of SOLID principels. Moreover, the Single-responsiblity principle.

-------------------------------------------

The _hello_world_ function is meant to run on the GPU.

-------------------------------------------

#### Client



> client1.py


```python
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
 


if __name__ == '__main__':
    ip_address='10.33.16.17'
    ports=5000
    #Get the ip address of the client
    a=bson.BSON.encode({'ipaddress': ip_address, 'ports':ports}) #Create a bson object
    r=requests.post('http://10.33.16.19:5000/server',data=a) #Send the bson to create a connection with the server
    app.debug=True
    app.run(host=ip_address,port=ports) #Run the flask server for the client
```


```python

```

The first thing that will be executed on the client side is to create the Flask app and set the where the capture is getting from,"from the main camera, 0" and the later the if condition. Will get the 'ip_address' from the 'net.sh' bash script, the port is the default port "5000". The 'ip_address' and the 'port' are going to be encode it into a BSON and post it to the server. The Flask server will be created and will wait for the server to have a GET request.

-------------------------------------------

#### AI

> facial_lanmasrks


```python

import cv2 as cv

def landmark_detection(frame, hog_model, fp_model):
    '''
    hog_model : hog classifier object
    fp_model : 68 facial point predictor object 
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
                    thickness=2,
                    fontScale=1
                    )
        face_count-=1

        ## plot points
        for point in points.parts():
            cv.circle(img=frame, 
                      center=(point.x, point.y), radius=2, 
                      color=(0,0,255), thickness=-1)
    return frame
```



> face_detection


```python
import cv2 as cv

def face_detect(frame, scale, face_detector):
    '''
    Input : Frame 
    output: Frame with face detected 
    '''
    height, width, channel = frame.shape
    if scale == 1:
        frame_scalled = frame
    else:
        frame_scalled = cv.resize(frame,                                                   # source image 
                                (int(width * scale), int(height * scale)),  # target resolution 
                                interpolation=cv.INTER_AREA
                        )  
    frame_gr = cv.cvtColor(frame_scalled, cv.COLOR_BGR2GRAY)
    face_detected = face_detector.detectMultiScale(frame_gr)
    number_of_faces = len(face_detected)
    count = number_of_faces
    if count:
        for x,y,w,h in face_detected:
            cv.rectangle(img=frame_scalled,
                         pt1=(x,y), pt2=(x+h,y+h), 
                         color=(255,0,255),
                         thickness=2)
            cv.putText(img=frame_scalled,
                       text=f'Face {count}', 
                       org=(x,y),
                       fontFace=cv.FONT_HERSHEY_PLAIN, 
                       fontScale=1, 
                       color=(0,255), 
                       thickness=1)
            count-=1
    
    cv.putText(img=frame_scalled,
               text=f'Face Count = {number_of_faces}', 
               org=(50,50),
               fontFace=cv.FONT_HERSHEY_PLAIN,
               fontScale=2, 
               color=(0,255,255), 
               thickness=2)
    return frame_scalled
```



##### Object detection

> object_detection


```python

```

> words

person
bicycle
car
motorcycle
airplane
bus
train
truck
boat
traffic light
fire hydrant
street sign
stop sign
parking meter
bench
bird
cat
dog
horse
sheep
cow
elephant
bear
zebra
giraffe
hat
backpack
umbrella
shoe
eye glasses
handbag
tie
suitcase
frisbee
skis
snowboard
sports ball
kite
baseball bat
baseball glove
skateboard
surfboard
tennis racket
bottle
plate
wine glass
cup
fork
knife
spoon
bowl
banana
apple
sandwich
orange
broccoli
carrot
hot dog
pizza
donut
cake
chair
couch
potted plant
bed
mirror
dining table
window
desk
toilet
door
tv
laptop
mouse
remote
keyboard
cell phone
microwave
oven
toaster
sink
refrigerator
blender
book
clock
vase
scissors
teddy bear
hair drier
toothbrush
hair brush



### JavaScript

#### Aside

> active_Buttons


```python
number_of_cameras_selected = 0; // number of cameras that are selected at that time

// function that check if the user selected a camera or not
function CheckCommand() {
    if (number_of_cameras_selected==0){
        alert("Please select a camera");
    }else{
        console.log("Is checked");
    }
    
}

// function that check increase or decrease the number of cameras that are selected at that time
function selectCameras(cb){
    if(document.getElementById(cb).checked){ // check if that checkbox is selected or not, by the "cb" reference
        number_of_cameras_selected++; // increase the number of cameras that are selected at that time
    }
    else{
        number_of_cameras_selected--; // decrease the number of cameras that are selected at that time
    }

}
```

We have a global variable 'number_of_cameras_selected' that will be increase or decrease when a camera will be selected. Moreover, the file contains 2 functions, one is for checking the user input and one is for modifying the value of the global variable. The first function _CheckCommand_ is checking if the user selected an AI option withoud selecting any cameras (This is more for the user to uderstand faster how to use the webapp). If the user did not select any camera will show an error, which will tell to the user to select a camera.

-------------------------------------------

The _selectCameras_ will increase or decrease the variable 'number_of_cameras_selected' based on the reference that is passed 'cb'.

-------------------------------------------

> aside


```python

```

#### list_of_buttons

Face Recognition
<br>
Number of People

For each line will create a button in the aside

#### main

> create_video


```python
// TODO: Sa fac sa fie pe coloane si pe linii

number_of_cameras= 0;

export function myFunction(ipAddress) {
  if(number_of_cameras%2!==0){
      var div = document.createElement('div'); // Create div for CameraArticle element

      var div_title = document.createElement('div'); // Create div for Camera Title which will contain all the elements
      div_title.className= "CameraTitle"; // set div clann name as "CameraTitle"
      div_title.setAttribute = number_of_cameras; // make the title of the camera the ipAddress of that camera

      var input = document.createElement('input'); // Create input element
      input.type = 'checkbox'; // Make the input element as a checkbox
      div_title.appendChild(input); // Append the input the the CameraTitle div

      var video = document.createElement('video'); // Create video
      video.src = 'http://'; // Add the src of the video variable
      video.autoplay = 'true'; // Make the video autoplay
      video.id= 'videoplayer/' + ipAddress; // Make the id of the video as: "videoplayer/" and the actual ipAddress
      div_title.appendChild(video); //  Append the video to the CameraTitle

      div.appendChild(div_title); //  Append the div_title to the main div("CameraArticle")

      number_of_cameras++; // Increment number_of_cameras variable
      
      

      document.body.appendChild(div); // Append the main div into the HTML document

    }
    else{



      number_of_cameras++; // Increment number_of_cameras variable
      document.body.appendChild(div); // Append the main div into the HTML document
    }
  }
```



#### video

> video

#### Checks

> check_first_checkbox


```python
function ShowImageJavaScript(){
    if(document.getElementById("IpAddress").checked==true){ // check that checkbox with that ipAddress
    return 1; //return 1 if the checkbox is selected
        }
    else{
        return 2; //return 2 if the checkbox is not selected
    }
}
```

The _ShowImageJavaScript_ function will check if that camera is selected or not. If the camera is selected will return 1, if it is not selected will return 2.

-------------------------------------------

### Bash

> delete


```python
#!/bin/bash

git reset --hard
git clean -fxd
```



> commit


```python
#!/bin/bash

$msg
git add .
git status
git commit -m '$msg'
git push
```

> install_linux


```python
#!/bin/bash
echo 'Initializing...'
sudo apt -y install python3 python3.10-venv figlet > /dev/null 2>&1

figlet 'Welcome to ConvergeCast Installation'
read x

python3 -m pip install --upgrade pip
python3 -m venv venv 
source venv/bin/activate
python -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
#pip install bson Do not install the "bson" package from pypi. PyMongo comes with its own bson package;
                # doing "easy_install bson" installs a third-party package that is incompatible with PyMongo.
pip install Flask-JSON
pip install numba
python3 -m pip install -U setuptools pip
pip install cupy-cuda117
python3 -m pip install pymongo
```

> net


```python
#!/bin/bash
function get_network(){
    interface=wlp3s0
    x=`ifconfig $interface | head -2 | tail -1` ; return $x | cut -d ' ' -f2
    return "$x"
}
a=$get_network
echo "$a"
```



This bash function get just the ip address of the interface wlp3s0, which is the ip address of the wide area network. We need wide area network to be able to communicate through the internet.

## Requierements

> requirements


```python
anyio==3.6.1
blinker==1.5
bottle==0.12.23
bottle-websocket==0.2.9
certifi==2022.6.15
charset-normalizer==2.1.0
click==8.1.3
colorlog==6.6.0
compress-json==1.0.7
cupy==10.6.0
cycler==0.11.0
Cython==0.29.30
drawnow==0.72.5
Eel==0.14.0
fastapi==0.79.0
fastrlock==0.8
ffmpeg-python==0.2.0
Flask==2.1.3
Flask-DebugToolbar==0.13.1
Flask-WTF==1.0.1
flaskwebgui==0.3.5
fonttools==4.34.4
future==0.18.2
gensim==4.2.0
gevent==21.12.0
gevent-websocket==0.10.1
greenlet==1.1.2
idna==3.3
imutils==0.5.4
itsdangerous==2.1.2
Jinja2==3.1.2
Js2Py==0.71
kiwisolver==1.4.4
llvmlite==0.38.1
MarkupSafe==2.1.1
matplotlib==3.5.2
numba==0.55.2
opencv-contrib-python==4.6.0.66
opencv-python==4.6.0.66
packaging==21.3
pgi==0.0.11.2
Pillow==9.2.0
pydantic==1.9.1
pyjsparser==2.7.1
pymongo==4.2.0
pyparsing==3.0.9
pyshine==0.0.9
python-bsonjs==0.3.0
python-dateutil==2.8.2
pytz-deprecation-shim==0.1.0.post0
requests==2.28.1
scipy==1.9.0
six==1.16.0
smart-open==6.0.0
sniffio==1.2.0
starlette==0.19.1
tqdm==4.64.0
typing_extensions==4.3.0
tzdata==2022.1
tzlocal==4.2
urllib3==1.26.10
vidgear==0.2.6
waitress==2.1.2
Werkzeug==2.1.2
whichcraft==0.6.1
WTForms==3.0.1
zope.event==4.5.0
zope.interface==5.4.0
```

## Frontend

### CSS

> style


```python
body{
    background-color:black;
    color:white;
}

.alertNoCameras{
    background-color:black;
    color:coral;
    border: solid 2px;
    border-radius: 12px;
    border-width: fit;
    border-color:coral;
}

aside {
    width: 30%;
    margin-top:80px;
    padding-left: 15px;
    margin-left: 15px;
    float: right;
    position: fixed;
    font-style: italic;
    background-color: lightgray;
    
  }

.btn-styled {
    font-size: 14px;
    margin: 8px;
    padding: 0 10px;
    line-height: 2;
}

header {
    overflow: hidden;
    background-color: #333;
    position: fixed;
    top: 0;
    width: 100%;
  }

.sidenav {
  height: 90%;
  width: 15%;
  position: fixed;
  z-index: 1;
  top: 17%;
  right: 0;
  background-color: #111;
  overflow-x: hidden;
  padding-top: 20px;
}

.mainSection {
  height:79%;
  width: 84%;
  z-index: 1;
  top: 18%;
  position: absolute;
  left: 1;
  background-color: #111;
  border-color: aqua;
  border-width: fit;
  overflow-x: hidden;
  border-style: solid;
  padding-top: 20px;
}

.CameraArticle{
  height: 20%;
  width: 20%;
  position: auto;
  border-color: red;
  border-width: 2px;
  border-style: solid;
  border:fit;
}

.CameraTitle{
  text-align: center
}
```



### HTML

#### templates

> index


```python
<!DOCTYPE html>
<html>
<head>
<title>Convrge Cast</title>
<link rel="stylesheet" href="{{ url_for('static', filename='Css/style.css') }}"/>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
<link async rel="stylesheet" href="{{ url_for('static', filename='javascript/js/opencv.js')}}">
<link rel="stylesheet" href="javascript/js/utils.js">



<link rel="stylesheet" 
href="{{ url_for('static', 
filename='javascript/video/Checks/check_first_checkbox.js')}}"/> <!--Inport javascript that will check if 
                                                                the ckeckbox for that ip is selected-->


<link rel="stylesheet"
href="{{ url_for('static', 
filename='javascript/video/video.js')}}"/> <!--Inport javascript that will upload the video stream to the HTML-->


<link rel="stylesheet" 
href="{{ url_for('static',
filename = 'javascript/main/create_video.js')}}"/> <!--Inport javascript that will automatically create 
                                                    a new HTML element that will show the video stream-->




<script
type="text/javascript"
src="{{ url_for('static', filename='/javascript/aside/activate_Buttons.js')}}" 
 ></script> <!--Inport javascript that will check the if the ckeckboxs are selected to tell the user to don't activate
                any computervision features without selecting a camera-->



<!-- <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" /> -->
<!-- <script defer src="https://pyscript.net/alpha/pyscript.js"></script> -->


<!-- <script
type="text/javascript"
src="{{ url_for('static', filename='/javascript/aside/aside.js')}}"
 ></script> -->

 <py-env>
    - OpenCV
    - cv2
    - os
    - matplotlib
     - ./get_video.py
 </py-env>

</head>
<body>

    <header>
        <div class="Number-of-Cameras">
            <h1>Number of cameras</h1>
            <p>0</p>
        </div>
    </header>


<div class="sidenav">

     <button onclick="myFunction()">Try</button>
    <div id="container"></div>
  </div>
  

<!--TODO: add javascript to allow this part or not-->

<div class="mainSection">
        <div class="CameraArticle">
            
            <div class="CameraTitle">Camera 1

                <input type="checkbox" id="IpAddress" value="true" onclick="selectCameras(this.id)"  > <!-- onclick="selectCameras(this.id)" -->
                <img id="input_image">

                <cameras id='canvas_output'></cameras>
                <!-- <img src="data:image/jpeg;base64, {{img}}"></img>

                <py-script
                    output="plot"
                    src="./Backend/get_video.py">
                </py-script> -->

                <!-- <div container class="Camera"><py-script src="./Backend/get_video.py"></py-script></div> -->
                
                <!-- <video id="videoplayer" autoplay="true" src= ""

                </video> -->
           
            </div>
            
        </div>
        
    <div class="row">
        <div class="col-md-3">
        </div>
    </div>
      
        
</div>


<button class="font-size:24px"><i class="material-icons">fullscreen</i></button>

</body>
</html>
```


