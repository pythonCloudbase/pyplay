from PIL import Image
import math

# image = Image.open('spider.jpg')

# print("Image info: ")
# print("Format: ",image.format)
# print("Mode: ", image.mode)
# print("Size: ",image.size)
# print("Pallette: ",image.palette)

# box = (550,80,1520,1000)
# c_i = image.crop(box)

# print("Image info After cropping: ")
# print("Format: ",c_i.format)
# print("Mode: ", c_i.mode)
# print("Size: ",c_i.size)
# print("Pallette: ",c_i.palette)

# #c_image.show()
# px= c_i.load()

# testing
# print(px)
# for i in range(0,600):
#     for j in range(0,400):
#         print(px[i,j])

image = Image.open('pika.jpg')
px = image.load()

pixBright = []
for i in range(0,image.size[0]):
    for j in range(0,image.size[1]):
        #print(px[i,j])
        #pixBright[i][j] = 2
        pixBright.append((0.21*px[j,i][0]) + (0.72*px[j,i][1]) + (0.07*px[j,i][2]))
        
print(len(pixBright))
# for i in pixBright:
#     print(i)

string_arr = '`^\\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'
print(len(string_arr))

ascii_map =[]
for i in range(0,len(pixBright)):
    
    #100 -> 50
    # 20 -> 10 = 50/100 * 20

    mapping = ((pixBright[i])/len(pixBright)) * len(string_arr) * 100
    #print(mapping)
    ascii_map.append(string_arr[math.floor(mapping)])



for i in range(0,len(ascii_map)):
    if(i%image.size[1]):
        print((ascii_map[i]),end="")
    else:
        print("\n")