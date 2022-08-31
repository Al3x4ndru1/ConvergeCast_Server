#https://stackoverflow.com/questions/60203320/inserting-and-using-the-user-uploaded-image-in-html-and-javascript
#https://www.w3docs.com/snippets/css/how-to-add-a-frame-around-an-image.html

#Ce trebuie:
#https://www.youtube.com/watch?v=-E8pdgsZ-ds
#https://docs.opencv.org/3.4/df/d24/tutorial_js_image_display.html

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

#import { ShowImageJavaScript } from "./javascript/video/check_first_checkbox.js"; // import the javascript function

def show1(frame,ipaddress):
    shoow = js2py.require('')

    numplusm= '''
 
    
    const ShowImageJavaScript = require("./javascript/video/check_first_checkbox").ShowImageJavaScript;
    
    function GetFirstCheckbox(){
        
        <check_first_checkbox> = require('<check_first_checkbox>');
        var.put(u'<variable name>', var.get(u'require')(Js(u'<check_first_checkbox>')));
        var.put(u'<variable name>', <check_first_checkbox>);
        var check = ShowImageJavaScript(); // call tha JavaScript function from the check_first_checkbox file
        return check; // return the check variable
    }
    '''


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


