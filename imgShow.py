import cv2
from google.colab.patches import cv2_imshow

img=cv2.imread('image_path') #this will read the image as np array 
cv2_imshow(img)
plt.imshow(X[0]) #X[0] is a numpy array
