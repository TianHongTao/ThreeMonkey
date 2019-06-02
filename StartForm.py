from camera import Camera
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget
from LearnForm import Ui_LearnForm
from learning import Ui_Form
from PyQt5.QtCore import QTimer, QObject

class Ui_StartForm(object):
    def setupUi(self, StartForm):
        # 姿势学习结束页面
        self.learnForm = None
        # 姿势学习页面
        self.learning = None
        StartForm.setObjectName("StartForm")
        StartForm.resize(734, 498)
        StartForm.setMinimumSize(QtCore.QSize(734, 498))
        StartForm.setAutoFillBackground(False)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(StartForm)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(StartForm)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMinimumSize(QtCore.QSize(0, 79))
        font = QtGui.QFont()
        font.setFamily("Wawati TC")
        font.setPointSize(56)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 56pt \"Wawati TC\";")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setStyleSheet("font: 20pt \"Wawati SC\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setStyleSheet("font: 20pt \"Wawati SC\";")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.verticalLayout_3.addWidget(self.frame)
        self.frame1 = QtWidgets.QFrame(StartForm)
        self.frame1.setMinimumSize(QtCore.QSize(0, 150))
        self.frame1.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame1.setObjectName("frame1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.learn = QtWidgets.QPushButton(self.frame1)
        self.learn.setMinimumSize(QtCore.QSize(232, 40))
        self.learn.setMaximumSize(QtCore.QSize(16777215, 40))
        self.learn.setStyleSheet("font: 24pt \"Wawati SC\";")
        self.learn.setObjectName("learn")
        self.learn.clicked.connect(self.learnFeature)
        self.verticalLayout_2.addWidget(self.learn)
        self.start = QtWidgets.QPushButton(self.frame1)
        self.start.setMinimumSize(QtCore.QSize(0, 40))
        self.start.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Wawati SC")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.start.setFont(font)
        self.start.setStyleSheet("font: 24pt \"Wawati SC\";")
        self.start.setObjectName("start")
        self.start.clicked.connect(self.startGame)
        self.verticalLayout_2.addWidget(self.start)
        self.verticalLayout_3.addWidget(self.frame1)

        self.retranslateUi(StartForm)
        QtCore.QMetaObject.connectSlotsByName(StartForm)

    def retranslateUi(self, StartForm):
        _translate = QtCore.QCoreApplication.translate
        StartForm.setWindowTitle(_translate("StartForm", "ThreeMonkey"))
        self.label.setText(_translate("StartForm", "三不猴"))
        self.label_2.setText(_translate("StartForm", "我就是我，最冷漠的旁观者"))
        self.label_3.setText(_translate("StartForm", "游戏中请你尽量不要多管闲事，非礼勿听，非礼勿看，非礼勿言"))
        self.learn.setText(_translate("StartForm", "· 进入游戏说明阶段（手势学习）"))
        self.start.setText(_translate("StartForm", "· 直接进入游戏"))

    # 开始游戏
    @pyqtSlot()
    def startGame(self):
        camera = Camera(0)
        flag = camera.startRunCamera(True)
        if flag:
            self.learnForm = QWidget()
            learnForm = Ui_LearnForm()
            learnForm.setupUi(self.learnForm)
            self.learnForm.show()



    # 启动摄像头，进入学习模块
    @pyqtSlot()
    def learnFeature(self):
        # 进入姿势学习界面
        self.learning = QWidget()
        learning = Ui_Form()
        learning.setupUi(self.learning)
        self.learning.show()
        learning.show_camera()
            # camera.learnRunCamera(learning,self.learning)
        # if flag: # 进入游戏开始界面
        #     self.learnForm = QWidget()
        #     learnForm = Ui_LearnForm()
        #     learnForm.setupUi(self.learnForm)
        #     self.learnForm.show()



