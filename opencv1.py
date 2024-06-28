import cv2

# cv2.imread() method loads an image from the specified file
img=cv2.imread('img.jpg')

# display image
cv2.imshow('image',img)
key=cv2.waitKey(0)#to wait for infinite sec
if key==27:
    cv2.destroyAllWindows()#destroy all windows
    # ie press escape key destrouy all windows
elif key==ord('s'):
    print('helo')
    #press s key then print helo


# cv2.imwrite() method is used to save an image to any storage device
cv2.imwrite('name.png',img)