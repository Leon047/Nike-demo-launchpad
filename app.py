import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import design
from app_requests import App_Requests
from request_urls import *

class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Clicking on a shoe selection.
        self.image1.clicked.connect(self,show_shoes_for_choice)
        self.image1.clicked.connect(self,show_shoes_for_choice)
        self.image1.clicked.connect(self,show_shoes_for_choice)
        self.image1.clicked.connect(self,show_shoes_for_choice)
        self.image1.clicked.connect(self,show_shoes_for_choice)


    def show_shoes_for_choice(self):
            self.photo.setPixmap(QtGui.QPixmap(image1))
            self.photo_2.setPixmap(QtGui.QPixmap(image2))
            self.photo_3.setPixmap(QtGui.QPixmap(image3))
            self.photo_4.setPixmap(QtGui.QPixmap(image4))
            self.photo_5.setPixmap(QtGui.QPixmap(image5))


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
