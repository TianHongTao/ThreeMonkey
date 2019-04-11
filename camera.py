import cv2
import numpy as np
#调用笔记本内置摄像头，所以参数为0，如果有其他的摄像头可以调整参数为1，2
class Camera:
    def __init__(self,NO):
        self.cap = cv2.VideoCapture(NO)
        self.face_cascade = cv2.CascadeClassifier("/anaconda3/pkgs/libopencv-3.4.2-h7c891bd_1/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml")
        self.failed = 2

    def closeCamera(self):
        # 关闭摄像头
        self.cap.release()

    def runCamera(self):
        while True:
            sucess, img = self.cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            x = int(img.shape[0] / 2)
            y = int(img.shape[1] / 2)
            # 高斯滤波
            temp = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
            GaussianImage = cv2.GaussianBlur(gray, (7, 7), 0)
            thresh = cv2.adaptiveThreshold(GaussianImage, 255, cv2.CHAIN_APPROX_NONE, cv2.THRESH_BINARY, 9
                                            , 8)
            _, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_TC89_L1)
            cv2.drawContours(temp, contours, -1, (255, 255, 255), 5)
            # 检测人脸位置
            faces = self.face_cascade.detectMultiScale(GaussianImage, 1.3, 5)
            temp = cv2.GaussianBlur(temp, (3,3), 0)
            if sucess:
                if len(faces) > 0:
                    for faceRect in faces:
                        x, y, w, h = faceRect
                        cv2.rectangle(temp, (x, y), (x + w - 15, y + h + 15), (255, 255, 255), 10)

                if self.failed == 0:
                    cv2.putText(img=temp, text="Distinguish failed, Please try again", fontScale=1,
                                fontFace=cv2.FONT_HERSHEY_COMPLEX, color=(0, 0, 255), org=(x, y))
                elif self.failed == 1:
                    cv2.putText(img=temp, text="Distinguish sucessful, Please waiting for a moment", fontScale=1,
                                fontFace=cv2.FONT_HERSHEY_COMPLEX, color=(0, 255, 255), org=(x, y))

                cv2.imshow('img', temp)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    cv2.destroyAllWindows()
                    break
                elif cv2.waitKey(1) & 0xFF == ord('w'):
                    # 模型输入接口
                    z = 0
                    if z == 0:
                        self.failed = 0
                    else:
                        self.failed = 1
                        if z == 1:

                            pass
                        elif z == 2:

                            pass
                        elif z == 3:

                            pass
        self.closeCamera()

# test = Camera(0)
# test.runCamera()