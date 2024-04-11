import cv2

img = cv2.imread("solar-system.jpg")
cv2.putText(img,"Sun",(20,300),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Mercury",(105,185),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Venus",(200,255),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Earth",(295,175),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Mars",(390,255),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Jupiter",(505,105),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Saturn",(725,285),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Uranus",(950,145),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Neptune",(1100,295),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))

cv2.imwrite("Solar_Planets_with_names.jpg",img)
cv2.imshow("Solar Planets",img)
cv2.waitKey(0)