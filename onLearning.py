# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'onLearning.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont, QPixmap, QPainter, QImage
import cv2
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import QVideoWidget
from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler
import numpy as np

FILE1 = "/Users/lixiaojuan/Downloads/ThreeMonkey/毕设最终视频/不听.png"
FILE2 = "/Users/lixiaojuan/Downloads/ThreeMonkey/毕设最终视频/不看.png"
FILE3 = "/Users/lixiaojuan/Downloads/ThreeMonkey/毕设最终视频/不说.png"

WORDS1 = "等待识别中, 请做出左图姿势"
WORDS2 = "识别失败, 请再次做出左图姿势"
WORDS3 = "(识别成功)干得漂亮"

PATH1 = QUrl("file:///Users/lixiaojuan/Downloads/ThreeMonkey/毕设最终视频/不听 选择后.mov")
PATH2 = QUrl("file:///Users/lixiaojuan/Downloads/ThreeMonkey/毕设最终视频/不看 后 新.mov")
PATH3 = QUrl("file:///Users/lixiaojuan/Downloads/ThreeMonkey/毕设最终视频/不说 后.mov")
PATH4 = QUrl("file:///Users/lixiaojuan/Downloads/ThreeMonkey/毕设最终视频/识别成功.mov")

class Onlearn_Form(object):
    def setupUi(self, Form, start, onlearning, readMe, study, choose, whatdo, allsee, finish, finishlearning, ending, tag = None):
        self.featrure_help = 0
        self.tmpPicture = None
        self.InImage = None
        self.clf = joblib.load("/Users/lixiaojuan/Downloads/ThreeMonkey/model/tree.pkl")
        self.sc = StandardScaler()
        self.bool = True
        self.ending = ending
        Form.setObjectName("Form")
        Form.resize(648, 454)
        self.tag = tag
        self.test = 0
        self.start = start
        self.onlearning = onlearning
        self.readMe = readMe
        self.study = study
        self.choose = choose
        self.whatdo = whatdo
        self.allsee = allsee
        self.finish = finish
        self.finishlearning = finishlearning
        self.Form = Form
        self.tmp = None
        self.featrure = [False,False,False]
        self.camera = cv2.VideoCapture(0)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.words = QtWidgets.QLabel(Form)
        self.words.setMaximumSize(QtCore.QSize(16777215, 35))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(159, 251, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 251, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 251, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 251, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 251, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 251, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 251, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 251, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 251, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.addItem(spacerItem)
        self.pictureShow = QtWidgets.QLabel(Form)
        self.pictureShow.setObjectName("pictureShow")
        self.horizontalLayout.addWidget(self.pictureShow)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 60))
        # self.label_4.setMaximumSize(QtCore.QSize(16777215, 200))
        self.label_4.setStyleSheet("font: 50pt \"FZZhengHeiS-EB-GB\";")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.videoShow = QtWidgets.QLabel(Form)
        self.videoShow.setMaximumSize(QtCore.QSize(900, 10000))
        self.videoShow.setObjectName("videoShow")
        self.verticalLayout_2.addWidget(self.videoShow)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout)

        if tag == None:
            self.timer = QTimer()
            # 定时器结束，触发showTime方法
            self.timer.timeout.connect(self.show_camera)
        else:
            self.timer2 = QTimer()
            # 定时器结束，触发showTime方法
            self.timer2.timeout.connect(self.Game)


        # self.retranslateUi(Form, None ,FILE1, "等待识别中, 请作出左图姿势", None)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form, Qimg, filename, words, way, word):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form23"))
        self.pictureShow.setPixmap(QtGui.QPixmap(filename).scaled(300,500))
        self.label_4.setText(_translate("Form", word))
        if Qimg is None:
            self.videoShow.setText(_translate("Form", "Camera_waiting"))
        else:
            self.videoShow.setPixmap(QPixmap.fromImage(Qimg))

        if way == 1:
            self.timer.start(200)
        elif way == 2:
            self.timer2.start(200)
        # self.Form.showFullScreen()

    def show_camera(self):
        self.test += 1
        self.featrure_help+=1
        flag, image = self.camera.read()
        show = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        size = (int(show.shape[1] * 0.8), int(show.shape[0] * 0.8))
        tmp = cv2.resize(show, size, interpolation=cv2.INTER_AREA)
        showImage = QtGui.QImage(tmp.data, tmp.shape[1], tmp.shape[0], QtGui.QImage.Format_RGB888)
        # 缺少模型输入检测模块,本处为测试
        self.tmpPicture = self.clf.predict(self.sc.fit_transform(cv2.resize(image[0].astype(np.float32), (400, 400), interpolation=cv2.INTER_AREA)).astype(np.float32).reshape(1, -1))
        if self.featrure[0] == False:
            if self.tmpPicture[0] == 0:
                self.retranslateUi(self.Form, showImage, FILE1, WORDS3, 1, WORDS1)
                self.featrure[0] = True
                self.featrure_help = 50
            else:
                self.retranslateUi(self.Form, showImage, FILE1, WORDS2, 1, WORDS1)
        else:
            if self.featrure[1] == False:
                if self.tmpPicture[0] == 1:
                    self.retranslateUi(self.Form, showImage, FILE2, WORDS3, 1, WORDS1)
                    self.featrure[1] = True
                    self.featrure_help = 100
                else:
                    self.retranslateUi(self.Form, showImage, FILE2, WORDS2, 1, WORDS1)
            else:
                if self.featrure[2] == False:
                    if self.tmpPicture[0] == 2:
                        self.retranslateUi(self.Form, showImage, FILE3, WORDS3, 1, WORDS1)
                        self.featrure[2] = True
                    else:
                        self.retranslateUi(self.Form, showImage, FILE3, WORDS2, 1, WORDS1)
        # print(self.featrure)

        if self.featrure_help == 50:
            self.featrure[0] = True
            self.retranslateUi(self.Form, showImage, FILE1, WORDS2, 1, WORDS1)

        if self.featrure_help == 150:
            self.featrure[1] = True
            self.retranslateUi(self.Form, showImage, FILE2, WORDS2, 1, WORDS1)

        if self.featrure_help == 250:
            self.featrure[2] = True
            self.retranslateUi(self.Form, showImage, FILE3, WORDS3, 1, WORDS1)

        if not self.featrure[0]:
            self.retranslateUi(self.Form, showImage, FILE1, WORDS1, 1, WORDS1)
            # threading.Timer(0.05, self.show_camera).start()
        elif not self.featrure[1]:
            self.retranslateUi(self.Form, showImage, FILE2, WORDS1, 1, WORDS1)
            # threading.Timer(0.05, self.show_camera).start()
        elif not self.featrure[2]:
            self.retranslateUi(self.Form, showImage, FILE3, WORDS1, 1, WORDS1)
            # threading.Timer(0.05, self.show_camera).start()

        if not (False in self.featrure):            
            self.featrure = [False, False, False]
            self.featrure_help = 0
            self.timer.stop()
            self.camera.release()
            self.Form.hide()
            self.flag = "NoListen"
            self.window = GUI1(self.Form, self.flag, self.start, self.onlearning, self.readMe, self.study, self.choose, self.whatdo, self.allsee, self.finish, self.finishlearning, self.ending)
            self.window.player.setVideoOutput(self.window.vw)
            self.window.player.setMedia(QMediaContent(PATH4))  # 选取视频文件
            self.window.player.play()  # 播放视频
            if self.window.isFirst:
                self.window.player.stateChanged.connect(self.window.Next)
                self.window.isFirst = False



            # self.tmp = QWidget()
            # self.finishlearning.setupUi(self.tmp, self.start, self.onlearning, self.readMe, self.study, self.choose, self.whatdo, self.allsee, self.finish, self.finishlearning, self.ending)
            # self.tmp.showFullScreen()

        if not self.Form.isFullScreen():
            self.Form.showFullScreen()

    def Game(self):
        tag = self.tag
        self.test += 1
        flag, image = self.camera.read()
        show = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
        # 缺少模型输入检测模块,本处为测试


        if tag == "NoListen":
            if self.test == 60:
                self.featrure[0] = True

            if self.test % 10 == 0:
                self.tmpPicture = self.clf.predict(
                    self.sc.fit_transform(cv2.resize(image[0], (400, 400), interpolation=cv2.INTER_AREA)).astype(
                        np.float32).reshape(1, -1))
                if self.tmpPicture[0] == 0:
                    self.featrure[0] = True
        elif tag == "NoSee":
            if self.test == 60:
                self.featrure[1] = True

            if self.test % 10 == 0:
                self.tmpPicture = self.clf.predict(
                    self.sc.fit_transform(cv2.resize(image[0], (400, 400), interpolation=cv2.INTER_AREA)).astype(
                        np.float32).reshape(1, -1))
                if self.tmpPicture[0] == 1:
                    self.featrure[1] = True
        else:
            if self.test == 60:
                self.featrure[2] = True

            if self.test % 10 == 0:
                self.tmpPicture = self.clf.predict(
                    self.sc.fit_transform(cv2.resize(image[0], (400, 400), interpolation=cv2.INTER_AREA)).astype(
                        np.float32).reshape(1, -1))
                if self.tmpPicture[0] == 2:
                    self.featrure[2] = True

        if tag == "NoListen":
            if self.featrure[0]:
                self.noListen()
            else:
                self.retranslateUi(self.Form, showImage, FILE1, WORDS1, 2, WORDS1)
        elif tag == "NoSee":
            if self.featrure[1]:
                self.noSee()
            else:
                self.retranslateUi(self.Form, showImage, FILE2, WORDS1, 2, WORDS1)
        else:
            if self.featrure[2]:
                self.noSay()
            else:
                self.retranslateUi(self.Form, showImage, FILE3, WORDS1, 2, WORDS1)

        if not False in self.featrure:
            self.featrure = [False,False,False]

        if not self.bool:
            if not self.Form.isFullScreen():
                self.Form.showFullScreen()

    def noListen(self):
        self.timer2.stop()
        self.camera.release()
        self.Form.hide()
        self.flag = "NoListen"
        self.window = GUI(self.Form, self.flag, self.start, self.onlearning, self.readMe, self.study, self.choose,self.whatdo, self.allsee, self.finish, self.finishlearning, self.ending)
        self.window.player.setVideoOutput(self.window.vw)
        self.window.player.setMedia(QMediaContent(PATH1))  # 选取视频文件
        self.window.player.play()  # 播放视频
        if self.window.isFirst:
            self.window.player.stateChanged.connect(self.window.Next)
            self.window.isFirst = False

    def noSee(self):
        self.timer2.stop()
        self.camera.release()
        self.Form.hide()
        self.flag = "NoSee"
        self.window = GUI(self.Form, self.flag, self.start, self.onlearning, self.readMe, self.study, self.choose,
                          self.whatdo, self.allsee, self.finish, self.finishlearning, self.ending)
        self.window.player.setVideoOutput(self.window.vw)
        self.window.player.setMedia(QMediaContent(PATH2))  # 选取视频文件
        self.window.player.play()  # 播放视频
        if self.window.isFirst:
            self.window.player.stateChanged.connect(self.window.Next)
            self.window.isFirst = False

    def noSay(self):
        self.timer2.stop()
        self.camera.release()
        self.Form.hide()
        self.flag = "NoSay"
        self.window = GUI(self.Form, self.flag, self.start, self.onlearning, self.readMe, self.study, self.choose,
                          self.whatdo, self.allsee, self.finish, self.finishlearning, self.ending)
        self.window.player.setVideoOutput(self.window.vw)
        self.window.player.setMedia(QMediaContent(PATH3))  # 选取视频文件
        self.window.player.play()  # 播放视频
        if self.window.isFirst:
            self.window.player.stateChanged.connect(self.window.Next)
            self.window.isFirst = False


class GUI(QWidget):
    def __init__(self, Form, flag, start, onlearning, readMe, study, choose, whatdo, allsee, finish, finishlearning, ending):
        super(GUI,self).__init__()
        self.ending = ending
        self.start = start
        self.onlearning = onlearning
        self.readMe = readMe
        self.study = study
        self.choose = choose
        self.whatdo = whatdo
        self.allsee = allsee
        self.finish = finish
        self.finishlearning = finishlearning
        self.isFirst = True
        self.flag = flag
        self.Form = QWidget()
        self.allsee.setupUi(self.Form, self.start, self.onlearning, self.readMe, self.study, self.choose, self.whatdo, self.allsee, self.finish, self.finishlearning, self.ending)
        self.layout = QVBoxLayout()
        self.vw = QVideoWidget()
        self.player = QMediaPlayer()
        self.vw.setAspectRatioMode(Qt.IgnoreAspectRatio)
        # self.vw.setFullScreen(True)
        self.layout.addWidget(self.vw)
        self.setLayout(self.layout)
        self.showFullScreen()

    def keyPressEvent(self,event):
        if (event.key() == Qt.Key_Return):
            self.player.play()  # 播放视频
        if (event.key() ==  Qt.Key_Space):
            self.player.pause()
        if (event.key() == Qt.Key_Escape):
            self.player.stop()
            self.vw.hide()
            self.hide()
            self.close()

    @pyqtSlot()
    def Next(self):
        if self.player.state() == QMediaPlayer.StoppedState:
            if not False in self.choose.choice:
                self.vw.hide()
                self.hide()
                self.tmp = QWidget()
                self.ending.setupUi(self.tmp, self.start, self.onlearning, self.readMe, self.study, self.choose, self.whatdo, self.allsee, self.finish, self.finishlearning, self.ending)
                self.tmp.showFullScreen()
            else:
                self.vw.hide()
                self.close()
                self.Form.showFullScreen()

class GUI1(QWidget):
    def __init__(self, Form, flag, start, onlearning, readMe, study, choose, whatdo, allsee, finish, finishlearning, ending):
        super(GUI1,self).__init__()
        self.start = start
        self.ending = ending
        self.onlearning = onlearning
        self.readMe = readMe
        self.study = study
        self.choose = choose
        self.whatdo = whatdo
        self.allsee = allsee
        self.finish = finish
        self.finishlearning = finishlearning
        self.isFirst = True
        self.flag = flag
        self.Form = QWidget()
        self.finishlearning.setupUi(self.Form, self.start, self.onlearning, self.readMe, self.study, self.choose, self.whatdo, self.allsee, self.finish, self.finishlearning, self.ending)
        self.layout = QVBoxLayout()
        self.vw = QVideoWidget()
        self.player = QMediaPlayer()
        self.vw.setAspectRatioMode(Qt.IgnoreAspectRatio)
        # self.vw.setFullScreen(True)
        self.layout.addWidget(self.vw)
        self.setLayout(self.layout)
        self.showFullScreen()

    def keyPressEvent(self,event):
        if (event.key() == Qt.Key_Return):
            self.player.play()  # 播放视频
        if (event.key() ==  Qt.Key_Space):
            self.player.pause()
        if (event.key() == Qt.Key_Escape):
            self.player.stop()
            self.vw.hide()
            self.hide()
            self.Form.showFullScreen()

    @pyqtSlot()
    def Next(self):
        if self.player.state() == QMediaPlayer.StoppedState:
            self.vw.hide()
            self.hide()
            self.Form.showFullScreen()