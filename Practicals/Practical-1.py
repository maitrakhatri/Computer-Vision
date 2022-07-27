import cv2
import os
import numpy as np

# Reading Image
img = cv2.imread("Images\colorwheel.png")
cb = cv2.imread("Images\chessboard.png")

# Operations on Image
img1 = img + 150
img2 = img - 75
img3 = img * 1.5
img4 = img / 2

# Displaying Image
cv2.imshow("Img", img4) # "Img" --> Window Name

# Writing Image
path = "Images" # realtive or absolute folder path
cv2.imwrite(os.path.join(path , 'newImg.png'),img1)

# Converting Image
convertedImage = cv2.cvtColor(img, cv2.COLOR_BGR2XYZ)
cv2.imshow("Converted Image", convertedImage)

# Converting to Grayscale
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", grayImage)

# Inverting/Complement of an Image
invertedImage = cv2.bitwise_not(img)
cv2.imshow("Inverted Image", invertedImage)

# Replacing specific Colors
# axis = -1 --> apply to each and every pixel, till the end
cb[np.all(cb == (255,255,255), axis=-1)] = (0,165,255)
cb[np.all(cb == (0,0,0), axis=-1)] = (255,255,0)
cv2.imshow("Color replaced Image",cb)

# keeps window open, press 0 to close the window
cv2.waitKey(0)