# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'choose.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import *

PATH1 = QUrl("file:///Users/lixiaojuan/Downloads/ThreeMonkey/毕设最终视频/声音 听 前改.mov")
PATH2 = QUrl("file:///Users/lixiaojuan/Downloads/ThreeMonkey/毕设最终视频/不看 前改.mov")
PATH3 = QUrl("file:///Users/lixiaojuan/Downloads/ThreeMonkey/毕设最终视频/不说 后改.mov")


class GUI(QWidget):
    def __init__(self, Form, flag, start, onlearning, readMe, study, choose, whatdo, allsee, finish, finishlearning, ending):
        super(GUI,self).__init__()
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
        self.onlearning.setupUi(self.Form, self.start, self.onlearning, self.readMe, self.study, self.choose, self.whatdo, self.allsee, self.finish, self.finishlearning, self.ending, flag)
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
            # self.Form.showFullScreen()
            self.onlearning.Game()


class myLabel(QLabel):
    clicked = pyqtSignal()
    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.clicked.emit()

class Choose_Form(object):

    def setupUi(self, Form, start, onlearning, readMe, study, choose, whatdo, allsee, finish, finishlearning, ending):
        self.ending = ending
        Form.setObjectName("Form")
        Form.resize(511, 300)
        try:
            self.choice = self.choose.choice
        except Exception as e:
            self.choice = [False, False, False]
        self.flag = ""
        self.window = None
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
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = myLabel(Form)
        self.label.setStyleSheet("font: 100pt \"FZZhengHeiS-EB-GB\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = myLabel(Form)
        self.label_3.setStyleSheet("font: 120pt \"FZZhengHeiS-EB-GB\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_3.clicked.connect(self.noListen)
        self.label_6 = myLabel(Form)
        self.label_6.setStyleSheet("font: 120pt \"FZZhengHeiS-EB-GB\";")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.label_6.clicked.connect(self.noSee)
        self.label_2 = myLabel(Form)
        self.label_2.setStyleSheet("font: 120pt \"FZZhengHeiS-EB-GB\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_2.clicked.connect(self.noSay)
        # self.label_4 = myLabel(Form)
        # self.label_4.setStyleSheet("font: 36pt \"FZZhengHeiS-EB-GB\";")
        # self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        # self.label_4.setObjectName("label_4")
        # self.horizontalLayout.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        # self.label_4.clicked.connect(self.four)
        self.label_5 = myLabel(Form)
        self.label_5.setStyleSheet("font: 60pt \"MF LiHei (Noncommercial)\";")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_5.clicked.connect(self.Return)
        self.verticalLayout.addWidget(self.label_5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "请选择关卡，点击选择进入"))
        self.label_3.setText(_translate("Form", "1"))
        self.label_6.setText(_translate("Form", "2"))
        self.label_2.setText(_translate("Form", "3"))
        # self.label_4.setText(_translate("Form", "4"))
        self.label_5.setText(_translate("Form", "返回首页"))
        pm = QPixmap('/Users/lixiaojuan/Desktop/不看不听不说.png')
        pm = pm.scaled(30,50)
        cursor = QCursor(pm,-1,-1)
        self.label_2.setCursor(cursor)
        self.label_3.setCursor(cursor)
        self.label_5.setCursor(cursor)
        self.label_6.setCursor(cursor)

    @pyqtSlot()
    def noListen(self):
        self.choice[0] = True
        self.Form.hide()
        self.flag = "NoListen"
        self.window = GUI(self.Form, self.flag, self.start, self.onlearning, self.readMe, self.study, self.choose, self.whatdo, self.allsee, self.finish, self.finishlearning, self.ending)
        self.window.player.setVideoOutput(self.window.vw)
        self.window.player.setMedia(QMediaContent(PATH1))  # 选取视频文件
        self.window.player.play()  # 播放视频
        if self.window.isFirst:
            self.window.player.stateChanged.connect(self.window.Next)
            self.window.isFirst = False

    @pyqtSlot()
    def noSee(self):
        self.choice[1] = True
        self.Form.hide()
        self.flag = "NoSee"
        self.window = GUI(self.Form, self.flag, self.start, self.onlearning, self.readMe, self.study, self.choose, self.whatdo, self.allsee, self.finish, self.finishlearning, self.ending)
        self.window.player.setVideoOutput(self.window.vw)
        self.window.player.setMedia(QMediaContent(PATH2))  # 选取视频文件
        self.window.player.play()  # 播放视频
        if self.window.isFirst:
            self.window.player.stateChanged.connect(self.window.Next)
            self.window.isFirst = False

    @pyqtSlot()
    def noSay(self):
        self.choice[2] = True
        self.Form.hide()
        self.flag = "NoSay"
        self.window = GUI(self.Form, self.flag, self.start, self.onlearning, self.readMe, self.study, self.choose, self.whatdo, self.allsee, self.finish, self.finishlearning, self.ending)
        self.window.player.setVideoOutput(self.window.vw)
        self.window.player.setMedia(QMediaContent(PATH3))  # 选取视频文件
        self.window.player.play()  # 播放视频
        if self.window.isFirst:
            self.window.player.stateChanged.connect(self.window.Next)
            self.window.isFirst = False


    @pyqtSlot()
    def Return(self):
        self.tmp = QWidget()
        self.start.setupUi(self.tmp, self.onlearning, self.readMe, self.study, self.choose, self.whatdo, self.allsee, self.finish, self.finishlearning, self.ending)
        self.Form.hide()
        self.tmp.showFullScreen()


