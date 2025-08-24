import os 
import cv2 
import numpy as np

img_path = os.path.abspath(r'C:\Users\user\Desktop\Programming\fear_of_computers\j.jpg')
# print(img_path)
img = cv2.imread(img_path)
# print(img.shape)
img_height, img_width, img_chanels = img.shape
# print(img_height,img_width)
img_top = img[600:900,:100,:]
out_path = 'j2.jpg'
cv2.imwrite(out_path,img_top)
print('vse kruto',os.path.abspath(out_path))

