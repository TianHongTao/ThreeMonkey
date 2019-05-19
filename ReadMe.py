# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ReadMe.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from Study import Study_Form,myLabel
from  PyQt5.QtGui import *


class ReadMe_Form(object):
    def setupUi(self, Form, start , onlearning, readMe, study, choose, whatdo, allsee, finish, finishlearning, ending):
        self.ending = ending
        self.onlearning = onlearning
        self.readMe = readMe
        self.study = study
        self.choose = choose
        self.whatdo = whatdo
        self.allsee = allsee
        self.finish = finish
        self.finishlearning = finishlearning
        Form.setObjectName("Form")
        Form.resize(539, 313)
        self.start = start
        self.Form = Form
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.tmp = None
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label = myLabel(Form)
        self.label.setStyleSheet("font: 80pt \"MF LiHei (Noncommercial)\";")
        self.label.setIndent(80)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = myLabel(Form)
        self.label_2.setMinimumSize(QtCore.QSize(515, 120))
        self.label_2.setMaximumSize(QtCore.QSize(1000, 300))
        self.label_2.setStyleSheet("font: 30pt \"Songti SC\";")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setIndent(100)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label_3 = myLabel(Form)
        self.label_3.setStyleSheet("font: 80pt \"MF LiHei (Noncommercial)\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_3.clicked.connect(self.Next)
        self.label_4 = myLabel(Form)
        self.label_4.setStyleSheet("font: 60pt \"MF LiHei (Noncommercial)\";")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setIndent(250)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_4.clicked.connect(self.Return)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "游戏简介"))
        self.label_2.setText(_translate("Form", "三不猴，是由三只猴面组成的竖形图案，三只猴子分别\n"
"捂住耳朵，眼睛，嘴，分别代表“不看，不听，不说”\n"
"\n"
"游戏中，每个关卡会播放相应的剧情视频，玩家需要\n"
"通过运用以上三种动作完成游戏\n"
""))
        self.label_3.setText(_translate("Form", "进入游戏"))
        self.label_4.setText(_translate("Form", "返回首页"))
        pm = QPixmap('/Users/denhiroshi/Desktop/不看不听不说.png')
        pm = pm.scaled(30,50)
        cursor = QCursor(pm,-1,-1)
        self.label_3.setCursor(cursor)
        self.label_4.setCursor(cursor)

    @pyqtSlot()
    def Return(self):
        self.tmp = QWidget()
        self.start.setupUi(self.tmp, self.onlearning, self.readMe, self.study, self.choose, self.whatdo, self.allsee, self.finish, self.finishlearning, self.ending)
        self.Form.hide()
        self.tmp.showFullScreen()

    @pyqtSlot()
    def Next(self):
        self.tmp = QWidget()
        self.study.setupUi(self.tmp, self.start, self.onlearning, self.readMe, self.study, self.choose, self.whatdo, self.allsee, self.finish, self.finishlearning, self.ending)
        self.Form.hide()
        self.tmp.showFullScreen()