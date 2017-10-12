import numpy as np
import cv2
import faceDetection as fd

def captureVideo(detect_flg):
  cap = cv2.VideoCapture(0)
  while(True):
    # 動画像の取得
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if detect_flg == 1:
      frame = fd.objDetection(frame)
    # 表示
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    key = cv2.waitKey(20)
    if key == 27 or key == ord('q'):
      break
  cap.release()
  cv2.destroyAllWindows()

if __name__ == '__main__':
  captureVideo(0)