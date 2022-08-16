#https://stackoverflow.com/questions/60203320/inserting-and-using-the-user-uploaded-image-in-html-and-javascript
#https://www.w3docs.com/snippets/css/how-to-add-a-frame-around-an-image.html

#Ce trebuie:
#https://www.youtube.com/watch?v=-E8pdgsZ-ds
#https://docs.opencv.org/3.4/df/d24/tutorial_js_image_display.html

import cv2 as cv
from os import environ
import matplotlib.pyplot as plt
from pylab import *
import base64
#import v8eval
#import PyV8

import js2py
#from drawnow import drawnow, figure

from numba import jit, cuda

# TODO: https://pypi.org/project/drawnow/ imshow

environ["QT_DEVICE_PIXEL_RATIO"] = "0"
environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
environ["QT_SCREEN_SCALE_FACTORS"] = "1"
environ["QT_SCALE_FACTOR"] = "1"


#class ShowClass():
#@jit(target='cuda')
# def show(frame,ipaddress):
#     # js2py 
#     numplusm= '''
#     import "./static/javascript/js/opencv.js";

#     function ShowImageJavaScript(ipaddress,frame){
#         if(document.getElementById(ipAddress).checked){
            
#         }
#         else{
#             cv.imshow('canvas_output',frame);
#         }
#     }
#     '''
#     a=js2py.eval_js(numplusm)
#     a("canvas_output",frame)


    #drawnow(draw(frame))
    #cv.imshow('test',frame)
    #while True:
    #plt.axis("off")
    # plt.show(cv.cvtColor(frame, cv.COLOR_BGR2RGB))
    # fig, ax = plt.subplots()
    # # ax.scatter(frame)
    # fig
# def draw(frame):
#     subplot(1,2,1)
#     imshow(frame)


def show1(frame,ipaddress):
    numplusm= """
    import { ShowImageJavaScript } from "./javascript/video/check_first_checkbox.js"; // import the javascript function

    function GetFirstCheckbox(){
       var check = ShowImageJavaScript(); // call tha JavaScript function from the check_first_checkbox file
       return check; // return the check variable
    }
    """
    a = js2py.eval_js(numplusm)
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