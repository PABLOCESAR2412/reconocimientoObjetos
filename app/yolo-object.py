import numpy as np
from PIL import Image #python image library
import matplotlib.pyplot as plt
import cv2
import matplotlib
matplotlib.use('Agg')

img=Image.open('./assets/foto.jpg')
print('Image')
print(img)
img.show()

#cv2.imshow(img)
#cv2.imshow('rgb image',img)


#matplotlib

img_mat=plt.imread("./assets/foto.jpg")
print('matplotlib')
print(img_mat)

#cv2.imshow(img_mat)
#cv2.imshow('rgb image',img)

'''#cv2

img_cv=cv2.imread("./assets/foto.jpg")
print('opencv')
print(img_cv)
cv2.imshow("CV2 img",img_cv)
cv2.waitKey(0)
cv2.destroyAllWindows()
#cv2.imshow(img_cv)
#cv2.imshow('rgb image',img)'''