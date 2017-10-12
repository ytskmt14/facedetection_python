import cv2
import numpy as np

'''
目　　　　　　　：haarcascade_eye.xml
目（メガネあり）：haarcascade_eye_tree_eyeglasses.xml
正面の猫の顔　　：haarcascade_frontalcatface.xml
正面の猫の顔　　：haarcascade_frontalcatface_extended.xml
正面の顔（人）　：haarcascade_frontalface_alt.xml
正面の顔（人）　：haarcascade_frontalface_alt2.xml
正面の顔（人）　：haarcascade_frontalface_alt_tree.xml
正面の顔（人）　：haarcascade_frontalface_default.xml
全身　　　　　　：haarcascade_fullbody.xml
左目　　　　　　：haarcascade_lefteye_2splits.xml
ナンバープレート：haarcascade_licence_plate_rus_16stages.xml
下半身　　　　　：haarcascade_lowerbody.xml
横顔　　　　　　：haarcascade_profileface.xml
右目　　　　　　：haarcascade_righteye_2splits.xml
ナンバープレート：haarcascade_russian_plate_number.xml
笑顔　　　　　　：haarcascade_smile.xml
上半身　　　　　：haarcascade_upperbody.xml
'''

# Haarlike特徴分類器のファイルパス
CASCADEFILEDIR = '/usr/local/Cellar/opencv3/3.2.0/share/OpenCV/haarcascades/'

objDetector = cv2.CascadeClassifier(CASCADEFILEDIR + 'haarcascade_frontalface_alt2.xml') 
# objDetector = cv2.CascadeClassifier(CASCADEFILEDIR + 'haarcascade_eye.xml') 
# objDetector = cv2.CascadeClassifier(CASCADEFILEDIR + 'haarcascade_smile.xml') 

def objDetection(img):
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  # 物体の検出
  objs = objDetector.detectMultiScale(gray)
  if len(objs) > 0:
    for rect in objs:
      #検出物体を矩形で囲む
      cv2.rectangle(img, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]), (255, 0, 0) ,2)
  return img


if __name__ == '__main__':
  img = cv2.imread('./image/lenna.png')
  img_data = np.asarray(img)
  objDetection(img_data)
  cv2.imshow('img', img)
  cv2.waitKey(0)