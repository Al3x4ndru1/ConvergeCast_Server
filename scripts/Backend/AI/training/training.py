from PIL import Image
import cv2 as cv
import numpy as np
import os


test={}

def get_image_data():
    paths = [os.path.join('./scripts/Backend/AI/photo',f) 
    for f in os.listdir('./scripts/Backend/AI/photo')] #we are perring the file in the format of a list
                                                           #we will get the full path of the image, using the join commands,
                                                           #it will join the first path with the path of the file in that directory
                                                           #that the for loop will traverse
   
    #print(paths)
    faces = [] #store information about the list ( information about the pixels)
    ids = [] #store the name of the classes, because we have from subject 1 to subject 15, in this example
    names = [] # store the name of the faces

    for path in paths:
        #print(path)
        image = Image.open(path).convert('L') #we are reading the images with the Image class 
                                              #because the images are stored as gif images
                                              #we have to convert with set the parameter "L" and it means the mode of the image
                                              #if we have an "L" mode images, it means it is a sinlge channel image, which is
                                              #interpreted as a gray scale image, the letter "L" means is just store the
                                              #luminance of the image, it is a compact format, but only stores a gray scale not colors
                                              #in other words we are converting from a clolr image to a gray scale image
        
        #print(type(image))
        image_np = np.array(image) #"unit8" means each pixel of the image is an integer value (unit8 doesn't work)
        #print(type(image_np))
        name = os.path.split(path)[1].split('.')[0].split('_')[1].replace('name','')
        print(type(name))

        print(os.path.split(path)[1].split('.')[0].split('_')[0].replace('subject',''))
        id = int(os.path.split(path)[1].split('.')[0].split('_')[0].replace('subject','')) #will split when will find a space
        global test
        test[id]= name
        #print(os.path.split(path)[1].split('.')[0].split('_')[0].replace('subject',''))

       
        # #print(id)
        ids.append(id)
        faces.append(image_np)
        names.append(name)
        
    return np.array(ids), faces

        
ids,faces = get_image_data()
# print(faces[0], faces[0].shape)

print(test)
lbph_classifier = cv.face.LBPHFaceRecognizer_create() #for this one we have a lot of parameters and I don't understand are grid_x and also grid_y
                                                      # the default value for grid_x and grid_y is 8

#lbph_classifier = cv.face.LBPHFaceRecognizer_create(radius =4, neighbors =14,grid_x=9,grid_y=9) modified to change the default values

lbph_classifier.train(faces, ids) # face variable stores all the pixels of all the images
                                  # ids variable stores all the name of the images of the classes, each number represents a person
                                  # the algorithm will store 64 histogram for each face, with the default values, 
                                  # because for each one of the square we will have a histogram

lbph_classifier.write('lbpg_classifier.yml') #this file stores each histogram of each one of the images


