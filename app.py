import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QComboBox
from PyQt5.QtGui import QIcon, QPixmap
import app_requests
import request_data
import design

class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def base_image(self):
        # Basic definitions of photo
        self.photo = ClickableLabel(self)
        self.photo_link=self.photo.setPixmap(QtGui.QPixmap("image/image0.jpg"))
        self.photo.clicked.connect(self.label_clicked)

        self.photo_1 = ClickableLabel(self)
        self.photo1_link=self.photo_1.setPixmap(QtGui.QPixmap("image/image1.jpg"))
        self.photo_1.clicked.connect(self.label_clicked)

        self.photo_2 = ClickableLabel(self)
        self.photo2_link=self.photo_2.setPixmap(QtGui.QPixmap("image/image2.jpg"))
        self.photo_2.clicked.connect(self.label_clicked)

        self.photo_3 = ClickableLabel(self)
        self.photo3_link=self.photo_3.setPixmap(QtGui.QPixmap("image/image3.jpg"))
        self.photo_3.clicked.connect(self.label_clicked)

        self.photo_4 = ClickableLabel(self)
        self.photo4_link=self.photo_4.setPixmap(QtGui.QPixmap("image/image4.jpg"))
        self.photo_4.clicked.connect(self.label_clicked)

    def query_image(self):
        # Target photo
        self.photo5_link=self.photo_5.setPixmap(QtGui.QPixmap("image/image5.jpg"))

    def found_images():
        # Basic definitions for found photos
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
        self.comboBox = qt.QComboBox()
        self.comboBox = str(self.comboBox.currentText())
        self.comboBox.setItemText(0, _translate("MainWindow", "All"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Men"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Women"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Unisex"))

    def item_type_combobox(self):
        self.comboBox_1 = qt.QComboBox()
        self.comboBox_1 = str(self.comboBox_1.currentText())
        self.comboBox_1.setItemText(0, _translate("MainWindow", "All"))
        self.comboBox_1.setItemText(1, _translate("MainWindow", "Sports"))
        self.comboBox_1.setItemText(2, _translate("MainWindow", "Casual"))

    def positive_lineedit(self):
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.positive_text = self.lineEdit.text()

    def negative_lineedit(self):
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.negative_text = self.lineEdit_1.text()

    def search_pushbutton(self):
        self.pushButton = QPushButton()
        self.pushButton.setText(_translate("MainWindow", "SEARCH"))
        self.pushButton.clicked.connect(search_pushbutton_clicked)

    def label_clicked(self):
        # Events for clicking on the photo.
        if self.photo.clicked.connect():
            self.photo_5 = self.photo
            self.add_image_url(0)

    def add_image_url(self, url_index):
        # Overrides URL in the request_data module
        base_url_data = request_data.base_shoes_url[url_index]
        request_data.image_url = list(base_url_data)

    def add_lineedit_data(self):
        # Overrides positive and negative atribuds in the request_data module
        request_data.add_positive_attributes.append(self.positive_text)
        request_data.add_negative_attributes.append(self.negative_lineedit)

    def add_combobox_data(self):
        # Overrides the values of the Gender string in the request_data module
        if self.comboBox ==  "All":
            request_data.gender = "All"
        elif self.comboBox ==  "Men":
            request_data.gender = "Men"
        elif self.comboBox ==  "Women":
            request_data.gender = "Women"
        else:
            request_data.gender = "Unisex"

    def add_combobox1_data(self):
        # Overrides the values of the Item Type string in the request_data module
        if self.comboBox_1 == "Sports":
            request_data.sport = "True"
            request_data.casual = "False"
        elif self.comboBox_1 == "Casual":
            request_data.sport = "False"
            request_data.casual = "True"
        else:
            request_data.casual = "False"
            request_data.casual = "False"

    def search_pushbutton_clicked(self):
        app_requests.create_json()
        app_requests.post_request()
        app_requests.sarch_request()
        self.lineEdit.text(create)
        self.lineEdit.setText(self.lineEdit.text(app_requests.create_json.all))

        self.lineEdit.clicked.connect(self.lineEdit.clear)
        self.lineEdit_1.clicked.connect(self.lineEdit_1.clear)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.setFixedSize(879, 513)
    window.show()
    app_requests.base_request()
    app.exec_()

if __name__ == '__main__':
    main()
