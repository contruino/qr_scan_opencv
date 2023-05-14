import cv2
img = cv2.imread('1.png')
detect = cv2.QRCodeDetector()



data, bbox, straight = detect.detectAndDecode(img)

if bbox is not None:
        print(data)

        n_lines = len(bbox)
        for i in range(n_lines):
            point1 = tuple(bbox[i][0])
            point2 = tuple(bbox[(i+1) % n_lines][0])
                              
cv2.imshow('Image',img)
                      

cv2.waitKey(0)
cv2.destroyAllWindows()


