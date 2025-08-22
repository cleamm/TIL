import cv2
img = cv2.imread('data1.jpg')
# 영역이나 엣지 검출 시엔 그레이스케일로 변경한 후 처리하는 것이 좋음(속도, 메모리 면에서)
gry_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) # 밝기를 파악하여 영역을 선정한다
t, tr_img = cv2.threshold(gry_img, 0, 255, cv2.THRESH_OTSU) # otsu(오츄)알고리즘은 어느정도 알아서 처리해줌
cv2.imshow('tr_img', tr_img)
cv2.waitKey()
# 어두운 부분과 밝은 부분을 기점으로 t값을 잡기 때문에 검정과 흰색을 잘 나눈 것처럼 보이지만 아주 잘 나누는 것은 아님
t1, tr_img = cv2.threshold(gry_img, 99, 255, cv2.THRESH_BINARY)
cv2.imshow('tr_img', tr_img)
cv2.waitKey()
t2, tr_img = cv2.threshold(gry_img, 99, 255, cv2.THRESH_BINARY_INV)
print(t, t1, t2) # 99, 0, 0 으로 오추알고리즘은 자동 설정이 된 것을 확인할 수 있다
# (다른 사람과 값이 다를 수도 있는듯?)

# cv2.imshow('img', img)
# cv2.imshow('gry_img', gry_img)
cv2.imshow('tr_img', tr_img)
cv2.waitKey()
cv2.destroyAllWindows()