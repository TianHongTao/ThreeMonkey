# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Start_new.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from  PyQt5.QtGui import *


class myLabel(QLabel):
    clicked = pyqtSignal()
    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.clicked.emit()

class StartNew_Form(object):
    def setupUi(self, Form, onlearning, readMe, study, choose, whatdo, allsee, finish, finishlearning, ending):
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
        Form.resize(520, 383)
        self.Form  = Form
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label = myLabel(Form)
        font = QtGui.QFont()
        font.setFamily("STKaiti")
        font.setPointSize(64)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tmp = None
        self.label.setFont(font)
        self.label.setStyleSheet("font: 240pt \"字魂24号-镇魂手书\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 =myLabel(Form)
        self.label_2.setStyleSheet("font: 40pt \"Weibei SC\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.label_3 = myLabel(Form)
        self.label_3.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.label_3.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.label_3.setStyleSheet("font: 80pt \"MF LiHei (Noncommercial)\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_3.clicked.connect(self.readME)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.label_4 = myLabel(Form)
        self.label_4.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.label_4.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.label_4.setStyleSheet("font: 60pt \"MF LiHei (Noncommercial)\";")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_4.clicked.connect(self.startGame)

        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">三不猴</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "在校园暴力面前你会怎么做"))
        pm = QPixmap('/Users/denhiroshi/Desktop/不看不听不说.png')
        pm = pm.scaled(30,50)
        cursor = QCursor(pm,-1,-1)
        self.label_3.setText(_translate("Form", "游戏简介"))
        self.label_3.setCursor(cursor)
        self.label_4.setText(_translate("Form", "开始游戏"))
        self.label_4.setCursor(cursor)

    @pyqtSlot()
    def readME(self):
        self.tmp = QWidget()
        self.readMe.setupUi(self.tmp, self, self.onlearning, self.readMe, self.study, self.choose, self.whatdo, self.allsee, self.finish, self.finishlearning, self.ending)
        self.Form.hide()
        self.tmp.showFullScreen()

    @pyqtSlot()
    def startGame(self):
        self.tmp = QWidget()
        self.study.setupUi(self.tmp, self, self.onlearning, self.readMe, self.study, self.choose, self.whatdo, self.allsee, self.finish, self.finishlearning, self.ending)
        self.tmp.showFullScreen()
        self.Form.hide()


