# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ending.ui'
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

PATH = QUrl("file:///Users/denhiroshi/Desktop/＋_＋ 2019-04-04 09.32.05.mp4")

class myLabel(QLabel):
    clicked = pyqtSignal()
    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.clicked.emit()

class Ending_Form(object):
    def setupUi(self, Form, start, onlearning, readMe, study, choose, whatdo, allsee, finish, finishlearning, ending):
        Form.setObjectName("Form")
        Form.resize(924, 414)
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
        self.Form = Form
        self.tmp = None
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label = myLabel(Form)
        self.label.setStyleSheet("font: 60pt \"MF LiHei (Noncommercial)\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.label_2 = myLabel(Form)
        self.label_2.setStyleSheet("font: 100pt \"MF LiHei (Noncommercial)\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_2.clicked.connect(self.Next)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "恭喜你已经成为一名合格的旁观者"))
        self.label_2.setText(_translate("Form", "播放游戏结尾视频"))
        pm = QPixmap('/Users/denhiroshi/Desktop/不看不听不说.png')
        pm = pm.scaled(30,50)
        cursor = QCursor(pm,-1,-1)
        self.label_2.setCursor(cursor)
        self.label.setCursor(cursor)

    @pyqtSlot()
    def Next(self):
        self.Form.hide()
        self.flag = "NoSee"
        self.window = GUI(self.Form, self.flag, self.start, self.onlearning, self.readMe, self.study, self.choose, self.whatdo, self.allsee, self.finish, self.finishlearning, self.ending)
        self.window.player.setVideoOutput(self.window.vw)
        self.window.player.setMedia(QMediaContent(PATH))  # 选取视频文件
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
        self.tmp = QWidget()
        self.choose.setupUi(self.tmp, self.start, self.onlearning, self.readMe, self.study, self.choose, self.whatdo, self.allsee, self.finish, self.finishlearning, self.ending)
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

    @pyqtSlot()
    def Next(self):
        self.vw.hide()
        self.hide()
        self.choose.choice = [False, False, False]
        self.tmp.showFullScreen()