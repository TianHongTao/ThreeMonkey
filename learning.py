# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'learning.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QFont, QPixmap, QPainter, QImage
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cv2
import threading
import time
from LearnForm import Ui_LearnForm

FILE1 = "img/1.png"
FILE2 = "img/2.png"
FILE3 = "img/3.png"
WORDS1 = "等待识别中, 请做出左图姿势"
WORDS2 = "识别失败, 请再次做出左图姿势"
WORDS3 = "(识别成功)干得漂亮"

class Ui_Form(QObject):

    def setupUi(self, Form):
        self.test = 0
        self.Form = Form
        Form.setObjectName("Form")
        Form.resize(1123, 656)
        self.featrure = [False,False,False]
        self.camera = cv2.VideoCapture(0)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalWidget = QtWidgets.QWidget(Form)
        self.verticalWidget.setMinimumSize(QtCore.QSize(500, 50))
        self.verticalWidget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalWidget)
        self.label.setStyleSheet("font: 24pt \"Hannotate SC\";\n"
"background-color: rgb(0, 255, 222);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout_3.addWidget(self.verticalWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.retranslateUi(Form, None ,"img/1.png", "等待识别中, 请作出左图姿势")
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form, Qimg, filename, words):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", words))
        self.label_2.setPixmap(QtGui.QPixmap(filename))
        if Qimg is None:
            self.label_3.setText(_translate("Form", "Camera_waiting"))
        else:
            self.label_3.setPixmap(QPixmap.fromImage(Qimg))

    @pyqtSlot()
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
            threading.Timer(0.05, self.show_camera).start()
        elif not self.featrure[1]:
            self.retranslateUi(self.Form, showImage, FILE2, WORDS1)
            threading.Timer(0.05, self.show_camera).start()
        elif not self.featrure[2]:
            self.retranslateUi(self.Form, showImage, FILE3, WORDS1)
            threading.Timer(0.05, self.show_camera).start()
        if not (False in self.featrure):
            self.Form.close()



    def end_camera(self):
        self.timer.stop()
        self.camera.release()
        self.label_3.clear()


