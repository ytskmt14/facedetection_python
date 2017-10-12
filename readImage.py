import cv2
import sys

# 画像の読み取り
def readImage(filepath = ""):
  # 引数にファイルパスが指定されていなければ、./tweet.pngを表示
  if not filepath:
    print("filepath is empty!")
    print("So, sample image sets var image.")
    filepath = "./image/lenna.png"
  image = cv2.imread(filepath)
  return image

if __name__ == "__main__":
  # コマンドラインの引数取得
  argv  = sys.argv
  if len(argv) == 1: # 引数にfilepathが指定されていない時
    filepath = ""
  else:
    filepath = argv[1]
  image = readImage(filepath)
  # 画像を表示
  cv2.imshow("image", image)
  cv2.waitKey(0)
  cv2.destroyAllWindows()