import cv2
import numpy as np 
from matplotlib import pyplot as plt 

img = cv2.imread('handbag.png',0)
edges = cv2.Canny(img, 100, 200)

# plt.subplot(121)
# plt.imshow(img, cmap='gray')
# plt.title('Original image')
# plt.xticks([])
# plt.yticks([])
# plt.subplot(122)
plt.imshow(edges,cmap = 'Greys')
#plt.title('Edge Image')
plt.xticks([])
plt.yticks([])

plt.show()
#plt.savefig('hb_edges.png')

