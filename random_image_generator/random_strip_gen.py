import os
import time
import numpy
import math
import random

from PIL import Image

def create_image(width, height):
    
    count = 0
    color = [127,230,127]

    random_num = random.choice([2,3,4,5,6])

    rgb_array = []
    for k in range(height):
        double_array = []

        count = count + 1
        #print(count)

        
        if(count == math.floor(height/random_num)):
            color = []
            color.append(int(numpy.random.rand(1)*255))
            color.append(int(numpy.random.rand(1)*255))
            color.append(int(numpy.random.rand(1)*255))
            count = 0
         
        for i in range(width): 
            
            width_array = []
            for j in range(3):
                if((i > width/6 and i < 2 * width/6)):
                    width_array.append(color[j])
                elif((i > 4 * width/6) and (i< 5*width/6)):
                    width_array.append(color[-1 *j])
                else:
                    width_array.append(255)
            #print(width_array)
            double_array.append(width_array)
        rgb_array.append(double_array)

    #print(rgb_array)

    result = numpy.asarray(rgb_array)

    #print(result)

    image = Image.fromarray(result.astype('uint8')).convert('RGB')
    image.save('created_strip.png')


get = input('Enter the dimension seperated by comma: ').split(',')
if(len(get) > 1):
    create_image(int(get[0]),int(get[1]))
else:
    
    create_image(100,100)
    print("\nInvalid input. Created a 100x100 image.")