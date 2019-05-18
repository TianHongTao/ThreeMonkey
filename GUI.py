from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import QVideoWidget
from Start_new import StartNew_Form
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtCore import *
from camera import Camera
from ReadMe import ReadMe_Form
from Study import Study_Form
from onLearning import Onlearn_Form
from finishLearn import finishlearning_Form
from choose import Choose_Form
from whatDo import whatDo_Form
from allSee import allSee_Form
from finishConductVideo import finish_Form
import sys


class GUI(QWidget):
    def __init__(self):
        super(GUI,self).__init__()
        self.layout = QVBoxLayout()
        self.vw = QVideoWidget()
        self.player = QMediaPlayer()
        self.vw.setAspectRatioMode(Qt.IgnoreAspectRatio)
        self.vw.setFullScreen(True)
        self.layout.addWidget(self.vw)
        self.setLayout(self.layout)
        self.showMaximized()

    def keyPressEvent(self,event):
        if (event.key() == Qt.Key_Return):
            self.player.play()  # 播放视频
        if (event.key() ==  Qt.Key_Space):
            self.player.pause()
        if event.key() == Qt.Key_S:
            self.player.pause()
            self.hide()
            test = Camera(0)
            test.runCamera()
            self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    start = QWidget()
    StartForm = StartNew_Form()
    readMe =  ReadMe_Form()
    study =  Study_Form()
    onlearn = Onlearn_Form()
    finishlearning = finishlearning_Form()
    choose = Choose_Form()
    whatDo = whatDo_Form()
    allsee = allSee_Form()
    finish = finish_Form()
    StartForm.setupUi(start, onlearn, readMe, study, choose, whatDo, allsee, finish, finishlearning)
    start.show()
    # start.show()
    # window = GUI()
    # fileDialog = QFileDialog()
    # # fileName = QFileDialog.getOpenFileUrl(parent=fileDialog, caption="Video choose", directory="/Users/denhiroshi/Desktop", filter="*.mp4")
    # # print(fileName)
    # PATH = QUrl("file:///Users/denhiroshi/Desktop/＋_＋ 2019-04-04 09.32.05.mp4")
    # window.player.setVideoOutput(window.vw)
    # playlist = QMediaPlaylist()
    # playlist.addMedia(QMediaContent(PATH))
    # playlist.setPlaybackMode(3)
    # window.player.setPlaylist(playlist)  # 选取视频文件
    # window.player.play()  # 播放视频
    sys.exit(app.exec_())
