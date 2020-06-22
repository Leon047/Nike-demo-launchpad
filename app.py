import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
import app_requests
import design

class App(QtWidgets.QMainWindow, design.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def base_image(self):
        self.photo = ClickableLabel()
        self.photo.setPixmap(QtGui.QPixmap("image/image0.jpg"))
        self.photo.clicked.connect(label_clicked)

        self.photo_1 = ClickableLabel()
        self.photo_1.setPixmap(QtGui.QPixmap("image/image1.jpg"))
        self.photo_1.clicked.connect(label_clicked)

        self.photo_2 = ClickableLabel()
        self.photo_2.setPixmap(QtGui.QPixmap("image/image2.jpg"))
        self.photo_2.clicked.connect(label_clicked)

        self.photo_3 = ClickableLabel()
        self.photo_3.setPixmap(QtGui.QPixmap("image/image3.jpg"))
        self.photo_3.clicked.connect(label_clicked)

        self.photo_4 = ClickableLabel()
        self.photo_4.setPixmap(QtGui.QPixmap("image/image4.jpg"))
        self.photo_4.clicked.connect(label_clicked)

    def query_image(self):
        self.photo_5.setPixmap(QtGui.QPixmap("image/image5.jpg"))

    def found_images():
        self.photo_6 = ClickableLabel()
        self.photo_6.setPixmap(QtGui.QPixmap("image/image6.jpg"))
        self.photo_6.clicked.connect(label_clicked)

        self.photo_7 = ClickableLabel()
        self.photo_7.setPixmap(QtGui.QPixmap("image/image7.jpg"))
        self.photo_7.clicked.connect(label_clicked)

        self.photo_8 = ClickableLabel()
        self.photo_8.setPixmap(QtGui.QPixmap("image/image8.jpg"))
        self.photo_8.clicked.connect(label_clicked)

        self.photo_9 = ClickableLabel()
        self.photo_9.setPixmap(QtGui.QPixmap("image/image9.jpg"))
        self.photo_9.clicked.connect(label_clicked)

        self.photo_10 = ClickableLabel()
        self.photo_10.setPixmap(QtGui.QPixmap("image/image10.jpg"))
        self.photo_10.clicked.connect(label_clicked)



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

    def negative_attributes_lineedit(self):
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)

    def search_pushbutton(self):
        self.pushButton.setText(_translate("MainWindow", "SEARCH"))


    def label_clicked(self, source): pass
        # Events for clicking on the image.


    def search_pushbutton_clicked(self): pass

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app_requests.base_request()
    app.exec_()

if __name__ == '__main__':
    main()
