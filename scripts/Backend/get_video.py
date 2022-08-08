import cv2 as cv
from os import environ
import matplotlib.pyplot as plt
from pylab import *
from drawnow import drawnow, figure

#from numba import jit, cuda

# TODO: https://pypi.org/project/drawnow/ imshow

environ["QT_DEVICE_PIXEL_RATIO"] = "0"
environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
environ["QT_SCREEN_SCALE_FACTORS"] = "1"
environ["QT_SCALE_FACTOR"] = "1"
#def show(self,frame):
def show(self,frame):
    drawnow(draw(frame))
    #cv.imshow('test',frame)
    #while True:
    #plt.axis("off")
    #plt.show(cv.cvtColor(frame, cv.COLOR_BGR2RGB))
    # fig, ax = plt.subplots()
    # ax.scatter(frame)
    # fig
    return
    
def draw(frame):
    subplot(1,2,1)
    imshow(frame)
