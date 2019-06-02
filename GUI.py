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
from ending import Ending_Form
from finishConductVideo import finish_Form
import sys
from sklearn.externals import joblib


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
    ending = Ending_Form()
    StartForm.setupUi(start, onlearn, readMe, study, choose, whatDo, allsee, finish, finishlearning, ending)
    start.showFullScreen()
    sys.exit(app.exec_())

