import cv2 as cv
from os import environ
import matplotlib.pyplot as plt
from pylab import *
import base64
#import v8eval
#import PyV8

import js2py
# import eel
#from drawnow import drawnow, figure

#from numba import jit, cuda

# TODO: https://pypi.org/project/drawnow/ imshow

environ["QT_DEVICE_PIXEL_RATIO"] = "0"
environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
environ["QT_SCREEN_SCALE_FACTORS"] = "1"
environ["QT_SCALE_FACTOR"] = "1"

class ShowClass:

    def show(self,frame):
        #frame = base64.b64encode(image)
        cv.imshow('test',frame)

        return

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
