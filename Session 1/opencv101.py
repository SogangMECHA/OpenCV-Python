import cv2

'''
* cv2.imread(fileName, flag): 이미지를 읽어 Numpy 객체로 만들기
IMREAD_COLOR: 이미지를 Color로 읽고, 투명한 부분은 무시
IMREAD_GRAYSCALE: 이미지를 Grayscale로 읽기
IMREAD_UNCHANGED: 이미지를 Color로 읽고, 투명한 부분도 읽기(Alpha)
- Return: Numpy 객체 (.shape 변수 => (행, 열, 색상: 기본 BGR))
'''
image = cv2.imread('opencvlogo.png', cv2.IMREAD_COLOR)

'''
* cv.imshow(title, image): 특정한 이미지를 윈도우 창으로 출력하기
'''
cv2.imshow('Image Basic', image)

'''
* cv2.waitkey(milisecond): 특정 시간 동안 대기. 0이면 입력받을때까지 무한대기
'''
cv2.waitKey(0)

'''
* cv2.imwrite(filename, image): 이미지를 파일로 저장하기
'''
cv2.imwrite('result1.png', image)

'''
* cv2.cvtColor(image, flag): 이미지의 색상을 변경하기
COLOR_BGR2GRAY: BGR 형식의 색상을 GRAY로 변환
'''
logo_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Image Gray', logo_gray)
cv2.waitKey(0)
cv2.imwrite('result2.png', logo_gray)

'''
* cv2.destroyAllWindows(): 화면에 나타는 윈도우를 모두 종료
'''
cv2.destroyAllWindows()