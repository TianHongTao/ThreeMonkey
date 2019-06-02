# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'allSee.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import QVideoWidget

PATH = QUrl("file:///Users/lixiaojuan/Downloads/ThreeMonkey/毕设最终视频/彩蛋.mov")

class myLabel(QLabel):
    clicked = pyqtSignal()
    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.clicked.emit()

class allSee_Form(object):
    def setupUi(self, Form, start, onlearning, readMe, study, choose, whatdo, allsee, finish, finishlearning, ending):
        self.ending = ending
        Form.setObjectName("Form")
        Form.resize(463, 288)
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
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.label = myLabel(Form)
        self.label.setStyleSheet("font: 80pt \"MF LiHei (Noncommercial)\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label.clicked.connect(self.next)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.label_2 = myLabel(Form)
        self.label_2.setStyleSheet("font: 60pt \"MF LiHei (Noncommercial)\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_2.clicked.connect(self.Next)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.label_3 = myLabel(Form)
        self.label_3.setStyleSheet("font: 60pt \"MF LiHei (Noncommercial)\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_3.clicked.connect(self.Return)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem9)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem10)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "返回游戏关卡页"))
        self.label_2.setText(_translate("Form", "观看游戏结尾视频(建议通关后选择)"))
        self.label_3.setText(_translate("Form", "返回首页 "))
        pm = QPixmap('/Users/lixiaojuan/Desktop/不看不听不说.png')
        pm = pm.scaled(30,50)
        cursor = QCursor(pm,-1,-1)
        self.label.setCursor(cursor)
        self.label_2.setCursor(cursor)
        self.label_3.setCursor(cursor)


    @pyqtSlot()
    def Return(self):
        self.tmp = QWidget()
        self.start.setupUi(self.tmp, self.onlearning, self.readMe, self.study, self.choose, self.whatdo, self.allsee, self.finish, self.finishlearning, self.ending)
        self.Form.hide()
        self.tmp.showFullScreen()

    @pyqtSlot()
    def next(self):
        self.tmp = QWidget()
        self.choose.setupUi(self.tmp, self.start, self.onlearning, self.readMe, self.study, self.choose, self.whatdo, self.allsee, self.finish, self.finishlearning, self.ending)
        self.Form.hide()
        self.tmp.showFullScreen()

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
        self.start.setupUi(self.tmp, self.onlearning, self.readMe, self.study, self.choose, self.whatdo, self.allsee, self.finish, self.finishlearning, self.ending)
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