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
import threading

FILE1 = "img/1.png"
FILE2 = "img/2.png"
FILE3 = "img/3.png"
WORDS1 = "等待识别中, 请做出左图姿势"
WORDS2 = "识别失败, 请再次做出左图姿势"
WORDS3 = "(识别成功)干得漂亮"

class Onlearn_Form(object):
    def setupUi(self, Form, start, onlearning, readMe, study, choose, whatdo, allsee, finish, finishlearning):
        Form.setObjectName("Form")
        Form.resize(648, 454)
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
        self.words.setMaximumSize(QtCore.QSize(16777215, 20))
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
        self.words.setPalette(palette)
        self.words.setStyleSheet("background-color: rgb(159, 251, 255);\n"
"border-color: rgb(0,0,0);\n"
"font: 14pt \"FZZhengHeiS-EB-GB\";")
        self.words.setAlignment(QtCore.Qt.AlignCenter)
        self.words.setObjectName("words")
        self.verticalLayout.addWidget(self.words)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pictureShow = QtWidgets.QLabel(Form)
        self.pictureShow.setObjectName("pictureShow")
        self.horizontalLayout.addWidget(self.pictureShow)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_4.setStyleSheet("font: 12pt \"FZZhengHeiS-EB-GB\";")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.videoShow = QtWidgets.QLabel(Form)
        self.videoShow.setObjectName("videoShow")
        self.verticalLayout_2.addWidget(self.videoShow)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.timer = QTimer()
        # 定时器结束，触发showTime方法
        self.timer.timeout.connect(self.show_camera)

        self.retranslateUi(Form, None ,FILE1, "等待识别中, 请作出左图姿势")
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form, Qimg, filename, words):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.words.setText(_translate("Form", "TextLabel"))
        self.label_4.setText(_translate("Form", words))
        if Qimg is None:
            self.videoShow.setText(_translate("Form", "Camera_waiting"))
        else:
            self.videoShow.setPixmap(QPixmap.fromImage(Qimg))
        self.timer.start(20)

    def show_camera(self):
        self.test += 1
        flag, image = self.camera.read()
        show = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
        # 缺少模型输入检测模块,本处为测试
        if self.test == 50:
            self.featrure[0] = True

        if self.test == 100:
            self.featrure[1] = True

        if self.test == 150:
            self.featrure[2] = True

        if not self.featrure[0]:
            self.retranslateUi(self.Form, showImage, FILE1, WORDS1)
            # threading.Timer(0.05, self.show_camera).start()
        elif not self.featrure[1]:
            self.retranslateUi(self.Form, showImage, FILE2, WORDS1)
            # threading.Timer(0.05, self.show_camera).start()
        elif not self.featrure[2]:
            self.retranslateUi(self.Form, showImage, FILE3, WORDS1)
            # threading.Timer(0.05, self.show_camera).start()
        if not (False in self.featrure):
            self.timer.stop()
            self.camera.release()
            self.tmp = QWidget()
            self.finishlearning.setupUi(self.tmp, self.start, self.onlearning, self.readMe, self.study, self.choose, self.whatdo, self.allsee, self.finish, self.finishlearning)
            self.tmp.show()
            self.Form.hide()
