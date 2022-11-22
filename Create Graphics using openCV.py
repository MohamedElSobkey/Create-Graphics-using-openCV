import cv2 as cv 
import numpy as np 

# to creat black window 
img = np.zeros((600,900, 3) , dtype= np.uint8)

# background
img = cv.rectangle(img, (0,0),(900,500),(255,225,85), -1)
img = cv.rectangle(img, (0,500),(900,600),(75,180,70), -1)



# to create sun
cv.circle(img, (200,150), 60, (0,255,255), -1) 
cv.circle(img, (200,150), 75, (220,255,255), 10)


#======================================#

#Tree 1

# tree stem
cv.line(img, (710, 500), (710, 420), (30,65,155), 15) #darw line


#tree leafs
triangle1 = np.array([[640,460],[780,460], [710,200]], dtype=np.int32)
cv.fillPoly(img, [triangle1], (75,180,70)) # to fill the triangle

#=================================================#

#Tree 2
# tree stem
cv.line(img, (600, 500), (600, 420), (30,65,155), 25)

#tree leafs
triangle2 = np.array([[500,440],[700,440], [600,75]], dtype=np.int32) 
cv.fillPoly(img, [triangle2], (75,200,70))


#============================================#


# to write on the img

# text
font = cv.FONT_HERSHEY_SCRIPT_SIMPLEX #text type

cv.putText(img, "I Love Python", (120,490), font, 1.7, (255,255,255), 2)


cv.imwrite('tree.png', img)
cv.imshow('Tree', img)

cv.waitKey(0)
cv.destroyAllWindows()
