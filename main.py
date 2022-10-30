import cv2
import numpy as np
import matplotlib.pyplot as plt

######Task 1#####

figure1 = cv2.imread('figure1.png')

cv2.imshow("Figure1",figure1)

print(figure1.size)

print(figure1.dtype)

print(figure1.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()

######Task 2#####

row = 256
col =256
img= np.zeros((row,col))
img[100:105,:]=0.5
img[:,100:105]=1
plt.figure(figsize=(10,4))
plt.imshow(img)
plt.show()


######Task 3#####

heigth =512
width=512

img= np.random.randint(255,size=(heigth,width),dtype=np.uint8)

cv2.imshow('Binary',img)
cv2.waitKey(0)
cv2.destroyAllWindows()