
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LearnForm(object):
    def setupUi(self, LearnForm):
        LearnForm.setObjectName("LearnForm")
        LearnForm.resize(494, 400)
        LearnForm.setMinimumSize(QtCore.QSize(494, 400))
        LearnForm.setMaximumSize(QtCore.QSize(516, 400))
        self.verticalLayout = QtWidgets.QVBoxLayout(LearnForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalFrame_2 = QtWidgets.QFrame(LearnForm)
        self.horizontalFrame_2.setMinimumSize(QtCore.QSize(0, 150))
        self.horizontalFrame_2.setMaximumSize(QtCore.QSize(16777215, 150))
        self.horizontalFrame_2.setObjectName("horizontalFrame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(self.horizontalFrame_2)
        self.label.setMinimumSize(QtCore.QSize(0, 150))
        self.label.setMaximumSize(QtCore.QSize(16777215, 150))
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setStyleSheet("font: 30pt \"Wawati SC\";")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addWidget(self.horizontalFrame_2)
        self.horizontalFrame = QtWidgets.QFrame(LearnForm)
        self.horizontalFrame.setMinimumSize(QtCore.QSize(0, 50))
        self.horizontalFrame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.pushButton = QtWidgets.QPushButton(self.horizontalFrame)
        self.pushButton.setStyleSheet("background-color: rgb(255, 0, 8);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 24pt \"STHeiti\";")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalFrame)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 0, 8);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 24pt \"STHeiti\";\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.verticalLayout.addWidget(self.horizontalFrame)

        self.retranslateUi(LearnForm)
        QtCore.QMetaObject.connectSlotsByName(LearnForm)

    def retranslateUi(self, LearnForm):
        _translate = QtCore.QCoreApplication.translate
        LearnForm.setWindowTitle(_translate("LearnForm", "Form"))
        self.label.setText(_translate("LearnForm", "你已经完成了所有手势的学习，\n"
"接下来的场景游戏中合理运用\n"
"所学手势!"))
        self.pushButton.setText(_translate("LearnForm", "开始游戏"))
        self.pushButton_2.setText(_translate("LearnForm", "返回首页"))

