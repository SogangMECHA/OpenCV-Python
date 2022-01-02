import cv2
import numpy as np

'''
* cv2.GaussianBlur(image, kernelsize, sigma)
: image를 Gaussian Filter 연산을 이용하여 blurring 합니다.
kernel: convolution 연산시 이용하는 필터. pdf 참조
kernel size 입력 시 sigma 는 0으로 설정함
* cv2.Canny(image, threshold1, threshold2, edges=, apertureSize=, L2gradient=)
threshold1: min threshold
threshold2: max threshold
각 parammeter의 값들은 시행착오를 거쳐 조정함
* cv2.HoughLines(image, rho, theta, threshold, lines, srn=, stn=, min_theta, max_theta)
rho: 거리 측정 해상도
theta: 각도, 라디안 단위
threshold: 직선으로 판단할 최소한의 동일 개수(작은 값: 정확도 감소, 검출 개수 증가, 큰 값: 정확도 증가, 검출 개수 감소)
* cv2.line(image, startpoint, endpoint, color, thickness)
'''

line = cv2.imread('line.png')
cv2.imshow('Default', line)

# 이미지 noise 임의로 생성 (20픽셀마다 검은줄 긋기)
line_scratch = line.copy()
#특정 픽셀의 색상을 마음대로 변경
for i in range (0,577):
    for j in range (0,655):
        if i % 20 == 0:
            line_scratch[i,j] = [0,0,0]
        if j % 20 == 0:
            line_scratch[i,j] = [0,0,0]
cv2.imshow('scratch',line_scratch)

# Gaussian Blur
line_blur = cv2.GaussianBlur(line_scratch, (7,7), 0)
cv2.imshow('GaussianBlur', line_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()

# HSV 색변환 및 이미지 masking
line_HSV = cv2.cvtColor(line_blur, cv2.COLOR_BGR2HSV)
yellow_lower = (20, 50, 50)
yellow_upper = (40, 255, 255)
line_mask = cv2.inRange(line_HSV, yellow_lower, yellow_upper)
cv2.imshow('Masking', line_mask)

# Canny를 이용한 가장자리 검출
line_canny = cv2.Canny(line_mask, 50, 150, apertureSize=3)
cv2.imshow('Canny', line_canny)

# HoughLine을 이용하여 가장자리 선 긋기
lines = cv2.HoughLines(line_canny, 1, np.pi/180, 150)
for i in range(len(lines)):
    for rho, theta in lines[i]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 - 1000 * b)
        x2 = int(x0 + 1000 * b)
        y1 = int(y0 + 1000 * a)
        y2 = int(y0 - 1000 * a)
        # line이라는 원본이미지에 빨간 선 그리기
        cv2.line(line, (x1,y1), (x2,y2), (0,0,255), 2)
cv2.imshow('Houghline', line)
cv2.waitKey(0)
cv2.destroyAllWindows()
