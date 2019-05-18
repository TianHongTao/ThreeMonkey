# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'finishLearn.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class myLabel(QLabel):
    clicked = pyqtSignal()
    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.clicked.emit()

class finishlearning_Form(object):
    def setupUi(self, Form, start, onlearning, readMe, study, choose, whatdo, allsee, finish, finishlearning):
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
        Form.setObjectName("Form")
        Form.resize(520, 331)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = myLabel(Form)
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label.setStyleSheet("font: 16pt \"FZZhengHeiS-EB-GB\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.label_2 = myLabel(Form)
        self.label_2.setStyleSheet("font: 36pt \"MF LiHei (Noncommercial)\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_2.clicked.connect(self.next)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.label_3 = myLabel(Form)
        self.label_3.setStyleSheet("font: 20pt \"MF LiHei (Noncommercial)\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_3.clicked.connect(self.Return)
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
        self.label.setText(_translate("Form", "你已经完成了所有手势的学习，请在接下来的游戏中合理运用所学知识"))
        self.label_2.setText(_translate("Form", "进入游戏"))
        self.label_3.setText(_translate("Form", "返回首页"))

    @pyqtSlot()
    def Return(self):
        print("flag")
        self.tmp = QWidget()
        self.start.setupUi(self.tmp, self.onlearning, self.readMe, self.study, self.choose, self.whatdo, self.allsee, self.finish, self.finishlearning)
        self.Form.hide()
        self.tmp.show()

    @pyqtSlot()
    def next(self):
        self.tmp = QWidget()
        self.choose.setupUi(self.tmp, self.start, self.onlearning, self.readMe, self.study, self.choose, self.whatdo, self.allsee, self.finish, self.finishlearning)
        self.Form.hide()
        self.tmp.show()

