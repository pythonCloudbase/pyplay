from PIL import Image

image = Image.open('spider.jpg')
#image.show()

print(image.format)

print(image.mode)
print(image.size)

print(image.palette)

#image.thumbnail((400,400))
#image.save('spider_thumb.jpg')
#print(image.size)
#image.show()