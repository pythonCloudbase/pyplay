import os
import time
import numpy
import random
from PIL import Image

#inspired by github

rgb_array = []
random_rectangles = []

color = [int(numpy.random.rand(1)*255),int(numpy.random.rand(1)*255),int(numpy.random.rand(1)*255)]
width = 420
height = 420

def create_rectangles(rgb_array):
    rect_size = 20
    rand_num = random.choice([2,3,4,5,6])

    for i in range(rand_num):
        x = 1
        y = 1
        while(width%x==0 & height%y == 0):
            x = random.randint(20, 180 - rect_size)
            y = random.randint(20, 180 - rect_size)
    
        random_rectangles.append([y,            x,          rect_size,rect_size])
        random_rectangles.append([y,            width-20-x, rect_size,rect_size])
        random_rectangles.append([height-20-y,  x,          rect_size,rect_size])
        random_rectangles.append([height-20-y,  width-20-x, rect_size,rect_size])

    for rectangle in random_rectangles:

        for i in range(rectangle[0], rectangle[0] + rectangle[2]):
            for j in range(rectangle[1], rectangle[1] + rectangle[3]):
                for k in range(3):
                    try:
                        rgb_array[i][j][k] = 255
                    except:
                        print(i,j,x,y)
                    

def create_image():
    for i in range(height):
        twod_array = []
        for j in range(width):
            width_array = []
            for k in range(3):
                #code for generating rectangles
                minpad =20
                if(i<20 or i >400 or j <20 or j >400):
                    width_array.append(255)
                else:
                    #create code to randomise the length of the division factor
                    width_array.append(color[k])        
            twod_array.append(width_array)
        rgb_array.append(twod_array)

    create_rectangles(rgb_array)
    result = numpy.asarray(rgb_array)
    image = Image.fromarray(result.astype('uint8')).convert('RGB')
    image.save('gavatar.png')
    

create_image()
print("gavatar.png saved!")