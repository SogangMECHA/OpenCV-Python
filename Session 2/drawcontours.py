import cv2

'''
* cv2.findContours(image, mode, method)
: 이미지에서 Contour를 찾습니다. (Gray Thresh 전처리 필요. 여기서는 inRange로 이진화한 이미지에서 진행)
- mode: Contour를 찾는 방법
1. RETR_EXTERNAL: 바깥쪽 Line만 찾기
2. RETR_LIST: 모든 Line을 찾지만, Hierarchy 구성 X
3. RETR_TREE: 모든 Line을 찾으며, 모든 Hierarchy 구성 O
- method: Contour를 찾는 근사치 방법
1. CHAIN_APPROX_NONE: 모든 Contour 포인트 저장
2. CHAIN_APPROX_SIMPLE: Contour Line을 그릴 수 있는 포인트만 저장
* cv2.drawContours(image, contours, contour_index, color, thickness )
: Contours를 그립니다.
- contour_index: 그리고자 하는 Contours Line (전체: -1)
'''

image = cv2.imread('opencvlogo.png')
image_HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
red_lower = (160, 128, 128)
red_upper = (180, 255, 255)
redmask_HSV = cv2.inRange(image_HSV, red_lower, red_upper)

contours, hierarchy = cv2.findContours(redmask_HSV, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#print(contours)
image_draw = image.copy()
image_contour = cv2.drawContours(image_draw, contours, -1, (0, 255, 255), 4)
cv2.imshow('Contours', image_contour)
#cv2.waitKey(0)

x,y,w,h = cv2.boundingRect(contours[0])
image_draw = image.copy()
image_box = cv2.rectangle(image_draw, (x, y), (x + w, y + h), (200, 200, 200), 2)
print('Midpoint: ', x+w/2, y+h/2)
print('Area: ', cv2.contourArea(contours[0]))
cv2.imshow('BoundingBox', image_box)
cv2.waitKey(0)
cv2.destroyAllWindows()