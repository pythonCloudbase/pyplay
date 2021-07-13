from PIL import Image, ImageEnhance
import cv2
import os

import sys

look_in = ".\photos"

print(f"Looking for directory {look_in} containing images.")

if not os.path.exists(look_in):
    print(f"please make a directory {look_in}, and put all the photos there.")
    sys.exit()

file_names = []

for r,d,f in os.walk(look_in):
    for fs in f:
        file_names.append(os.path.join(look_in, fs))


# change values here to adjust contrast and brightness
alpha = 1.5 # Contrast control (1.0-3.0)
beta = 0 # Brightness control (0-100)

print("Please note:")
print(f"Current contrast control: {alpha}")
print(f"Current brightness control: {beta}")


save_at = ".\output"

if not os.path.exists(save_at):
    os.makedirs(save_at)

#read the image
# im = Image.open(files[0])
for files in file_names:

    im = cv2.imread(files)
    print(files[0].split("\\"))

    # this is convoluted needlessly
    file_save_at = os.path.join(save_at, files.split("\\")[2])

    print(f"processing: {file_save_at}")

    # print(im)
    # #image brightness enhancer
    # enhancer = ImageEnhance.Contrast(im)

    # factor = 1 #gives original image
    # im_output = enhancer.enhance(factor)
    # im_output.save(file_save_at + '_s.png')


    adjusted = cv2.convertScaleAbs(im, alpha=alpha, beta=beta)

    cv2.imwrite(file_save_at, adjusted)

print("Done. Check in output folder to find adjusted images.")