# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nike-launchpad.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(802, 758)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 410, 131, 41))
        self.pushButton.setObjectName("pushButton")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(600, 240, 71, 51))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(700, 240, 71, 51))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 340, 781, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 240, 241, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(330, 240, 231, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 781, 191))
        self.groupBox.setObjectName("groupBox")

        self.photo = QtWidgets.QLabel(self.groupBox)
        self.photo.setGeometry(QtCore.QRect(0, 30, 131, 161))
        self.photo.setObjectName("photo")

        self.photo_2 = QtWidgets.QLabel(self.groupBox)
        self.photo_2.setGeometry(QtCore.QRect(150, 30, 131, 161))
        self.photo_2.setObjectName("photo_2")

        self.photo_3 = QtWidgets.QLabel(self.groupBox)
        self.photo_3.setGeometry(QtCore.QRect(310, 20, 131, 161))
        self.photo_3.setObjectName("photo_3")

        self.photo_4 = QtWidgets.QLabel(self.groupBox)
        self.photo_4.setGeometry(QtCore.QRect(480, 20, 141, 161))
        self.photo_4.setObjectName("photo_4")

        self.photo_5 = QtWidgets.QLabel(self.groupBox)
        self.photo_5.setGeometry(QtCore.QRect(650, 30, 121, 161))
        self.photo_5.setObjectName("photo_5")

        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(190, 490, 601, 191))
        self.groupBox_2.setObjectName("groupBox_2")

        self.photo_7 = QtWidgets.QLabel(self.groupBox_2)
        self.photo_7.setGeometry(QtCore.QRect(10, 30, 121, 161))
        self.photo_7.setObjectName("photo_7")

        self.photo_8 = QtWidgets.QLabel(self.groupBox_2)
        self.photo_8.setGeometry(QtCore.QRect(160, 30, 141, 161))
        self.photo_8.setObjectName("photo_8")

        self.photo_9 = QtWidgets.QLabel(self.groupBox_2)
        self.photo_9.setGeometry(QtCore.QRect(330, 20, 131, 161))
        self.photo_9.setObjectName("photo_9")

        self.photo_10 = QtWidgets.QLabel(self.groupBox_2)
        self.photo_10.setGeometry(QtCore.QRect(480, 20, 121, 161))
        self.photo_10.setObjectName("photo_10")

        self.photo_6 = QtWidgets.QLabel(self.centralwidget)
        self.photo_6.setGeometry(QtCore.QRect(10, 470, 171, 231))
        self.photo_6.setObjectName("photo_6")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(600, 220, 67, 17))
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(700, 220, 67, 17))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 320, 67, 17))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 380, 111, 17))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 440, 91, 17))
        self.label_5.setObjectName("label_5")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 22))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "SEARCH"))
        self.comboBox.setItemText(0, _translate("MainWindow", "All"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Men"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Women"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Unisex"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "All"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Sports"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Casual"))
        self.groupBox.setTitle(_translate("MainWindow", "Multimodal search"))
        self.photo.setText(_translate("MainWindow", "TextLabel"))
        self.photo_2.setText(_translate("MainWindow", "TextLabel"))
        self.photo_3.setText(_translate("MainWindow", "TextLabel"))
        self.photo_4.setText(_translate("MainWindow", "TextLabel"))
        self.photo_5.setText(_translate("MainWindow", "TextLabel"))
        self.groupBox_2.setTitle(_translate("MainWindow", "GroupBox"))
        self.photo_7.setText(_translate("MainWindow", "TextLabel"))
        self.photo_8.setText(_translate("MainWindow", "TextLabel"))
        self.photo_9.setText(_translate("MainWindow", "TextLabel"))
        self.photo_10.setText(_translate("MainWindow", "TextLabel"))
        self.photo_6.setText(_translate("MainWindow", "TextLabel"))
        self.label.setText(_translate("MainWindow", "Gender"))
        self.label_2.setText(_translate("MainWindow", "Item Type"))
        self.label_3.setText(_translate("MainWindow", "Query URL"))
        self.label_4.setText(_translate("MainWindow", "Input image URL"))
        self.label_5.setText(_translate("MainWindow", "Query Image"))