from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtCore import *
from camera import Camera
from StartForm import Ui_StartForm
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
    StartForm = Ui_StartForm()
    StartForm.setupUi(start)
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
