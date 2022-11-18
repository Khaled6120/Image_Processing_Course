import random
import cv2
 
def adding_noise(img):
 
    # dimensions of the image
    row , col = img.shape
     
    # Randomly pick some pixels in the image for coloring them white
    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):
       
        #  random y coordinate
        y_coord=random.randint(0, row - 1)
         
        #  random x coordinate
        x_coord=random.randint(0, col - 1)
         
        #  pixel to white
        img[y_coord][x_coord] = 255
         
    # Randomly pick some pixels in the image for coloring them black
    number_of_pixels = random.randint(300 , 10000)
    for i in range(number_of_pixels):
       
        #  random y coordinate
        y_coord=random.randint(0, row - 1)
         
        #  random x coordinate
        x_coord=random.randint(0, col - 1)
         
        #  pixel to black
        img[y_coord][x_coord] = 0
         
    return img
 
# Reading the color image in grayscale image
img = cv2.imread('photo.jpg',cv2.IMREAD_GRAYSCALE)
                
#Storing the image
cv2.imwrite('salt-and-pepper-lena.jpg', adding_noise(img))
         
