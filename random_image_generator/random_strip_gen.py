import os
import time
import numpy

from PIL import Image

def create_image(width, height):
    
    rgb_array = []
    for k in range(height):
        double_array = []
        color = []
        color.append(int(numpy.random.rand(1)*255))
        color.append(int(numpy.random.rand(1)*255))
        color.append(int(numpy.random.rand(1)*255)) 
        for i in range(width):  
            width_array = []
            for j in range(3):
                width_array.append(color[j])
            print(width_array)
            double_array.append(width_array)
        rgb_array.append(double_array)

    #print(rgb_array)

    result = numpy.asarray(rgb_array)

    print(result)

    image = Image.fromarray(result.astype('uint8')).convert('RGB')
    image.save('created_strip.png')

create_image(10,10)