import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import design
from app_requests import App_Requests
from request_urls import *

class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def app_act(self):
        # Clicking on a shoe selection.
        self.image0.clicked.connect(self,show_shoes_for_choice)
        self.image1.clicked.connect(self,show_shoes_for_choice)
        self.image2.clicked.connect(self,show_shoes_for_choice)
        self.image3.clicked.connect(self,show_shoes_for_choice)
        self.image4.clicked.connect(self,show_shoes_for_choice)

    def base_image(self):
        self.photo.setPixmap(QtGui.QPixmap(image0))
        self.photo_1.setPixmap(QtGui.QPixmap(image1))
        self.photo_2.setPixmap(QtGui.QPixmap(image2))
        self.photo_3.setPixmap(QtGui.QPixmap(image3))
        self.photo_4.setPixmap(QtGui.QPixmap(image4))

    def query_image(self):
        self.photo_5.setPixmap(QtGui.QPixmap(image5))

    def found_images():
        self.photo_6.setPixmap(QtGui.QPixmap(image2))
        self.photo_7.setPixmap(QtGui.QPixmap(image2))
        self.photo_8.setPixmap(QtGui.QPixmap(image2))
        self.photo_9.setPixmap(QtGui.QPixmap(image2))
        self.photo_10.setPixmap(QtGui.QPixmap(image2))

    def gender_combobox(self):
        self.comboBox.setItemText(0, _translate("MainWindow", "All"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Men"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Women"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Unisex"))

    def item_type_combobox(self):
        self.comboBox_1.setItemText(0, _translate("MainWindow", "All"))
        self.comboBox_1.setItemText(1, _translate("MainWindow", "Sports"))
        self.comboBox_1.setItemText(2, _translate("MainWindow", "Casual"))

    def positive_attributes_lineedit(self):
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 260, 781, 31))
        self.lineEdit.setObjectName("lineEdit")

    def negative_attributes_lineedit(self):
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setGeometry(QtCore.QRect(130, 210, 241, 21))
        self.lineEdit_1.setObjectName("lineEdit_2")

    def search_pushbutton(self):
        self.pushButton.setText(_translate("MainWindow", "SEARCH"))


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
