import cv2

image1 = cv2.imread('opencvlogo.png')
image2 = cv2.imread('mechalogo.png')

# 이미지 Numpy 객체의 특정 픽셀을 가리킵니다.
px = image1[100, 100]
# B, G, R 순서로 출력됩니다.
# Gray Scale: B, G, R로 구분되지 않습니다.
print(px)
# R 값만 출력하기
print(px[2])
# 픽셀 수 및 이미지 크기 확인
print(image1.shape)
print(image1.size)

cv2.imshow('Image1', image1)
cv2.imshow('Image2', image2)
#cv2.waitKey(0)

# Numpy Slicing: ROI 처리 가능
slice = image2[44:304, 50:310]
cv2.imshow('Slicing', slice)
#cv2.waitKey(0)

# ROI 단위로 이미지 복사하기
image1_copy = image1.copy()
image1_copy[0:260, 140:400] = slice
cv2.imshow('Paste', image1_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 특정 색상만 보여주기 (0: Blue, 1: Green, 2: Red)
# image[height, width, depth], depth에 color 정보가 있다
cv2.imshow('BGR_R', image1[:, :, 2])
#cv2.waitKey(0)

# 특정 색상만 제거하기
image1_copy = image1.copy()
image1_copy[:, :, 2] = 0
cv2.imshow('EliminateR', image1_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()


# HSV 색체계를 이용하여 지정된 색 범위만 나타내기
# H: Hue(색상, 0~180), S: Saturation(채도, 0~255), V: Value(명도, 0~255)
image_HSV = cv2.cvtColor(image1, cv2.COLOR_BGR2HSV)
red_lower = (160, 128, 128)
red_upper = (180, 255, 255)
green_lower = (50, 128, 128)
green_upper = (70, 255, 255)
blue_lower = (100, 128, 128)
blue_upper = (120, 255, 255)
redmask_HSV = cv2.inRange(image_HSV, red_lower, red_upper)
greenmask_HSV = cv2.inRange(image_HSV, green_lower, green_upper)
bluemask_HSV = cv2.inRange(image_HSV, blue_lower, blue_upper)
cv2.imshow('Red Masking', redmask_HSV)
cv2.imshow('Green Masking', greenmask_HSV)
cv2.imshow('Blue Masking', bluemask_HSV)
cv2.waitKey(0)
cv2.destroyAllWindows()