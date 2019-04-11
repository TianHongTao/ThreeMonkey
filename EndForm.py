
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EndFrom(object):
    def setupUi(self, EndFrom):
        EndFrom.setObjectName("EndFrom")
        EndFrom.resize(609, 339)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(EndFrom)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(EndFrom)
        self.label.setStyleSheet("font: 30pt \"Wawati SC\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(EndFrom)
        self.label_2.setStyleSheet("font: 30pt \"Wawati SC\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(EndFrom)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton.setMaximumSize(QtCore.QSize(250, 16777215))
        self.pushButton.setStyleSheet("font: 24pt \"Hannotate SC\";")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.pushButton.raise_()
        self.pushButton.raise_()
        self.pushButton.raise_()

        self.retranslateUi(EndFrom)
        QtCore.QMetaObject.connectSlotsByName(EndFrom)

    def retranslateUi(self, EndFrom):
        _translate = QtCore.QCoreApplication.translate
        EndFrom.setWindowTitle(_translate("EndFrom", "Form"))
        self.label.setText(_translate("EndFrom", "恭喜你通过所有关卡"))
        self.label_2.setText(_translate("EndFrom", "经鉴定，你是一名合格的旁观者"))
        self.pushButton.setText(_translate("EndFrom", "点击播放结尾视频"))

