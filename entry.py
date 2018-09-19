# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import requests
import json
APICODE='2698ed7ecba778c1917a16363cc15b48'
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(668, 912)
        Dialog.setMinimumSize(QtCore.QSize(668, 912))
        Dialog.setMaximumSize(QtCore.QSize(668, 912))
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setStyleSheet(" border-radius: 10px;\n"
"background-color: rgb(105, 8, 51);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logoLayoutH = QtWidgets.QHBoxLayout()
        self.logoLayoutH.setObjectName("logoLayoutH")
        spacerItem = QtWidgets.QSpacerItem(40, 300, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.logoLayoutH.addItem(spacerItem)
        self.logo = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMinimumSize(QtCore.QSize(300, 300))
        self.logo.setMaximumSize(QtCore.QSize(300, 300))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("owm.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.logoLayoutH.addWidget(self.logo)
        spacerItem1 = QtWidgets.QSpacerItem(40, 300, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.logoLayoutH.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.logoLayoutH)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.enterNameLabel = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.enterNameLabel.sizePolicy().hasHeightForWidth())
        self.enterNameLabel.setSizePolicy(sizePolicy)
        self.enterNameLabel.setMinimumSize(QtCore.QSize(0, 70))
        self.enterNameLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.enterNameLabel.setFont(font)
        self.enterNameLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.enterNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.enterNameLabel.setObjectName("enterNameLabel")
        self.verticalLayout.addWidget(self.enterNameLabel)
        self.cityNameEntry = QtWidgets.QLineEdit(self.frame)
        self.cityNameEntry.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cityNameEntry.setFont(font)
        self.cityNameEntry.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"border-color: rgb(205, 205, 205);\n"
"border-width: 2px;")
        self.cityNameEntry.setAlignment(QtCore.Qt.AlignCenter)
        self.cityNameEntry.setObjectName("cityNameEntry")
        self.verticalLayout.addWidget(self.cityNameEntry)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.confirmBtn = QtWidgets.QPushButton(self.frame)
        self.confirmBtn.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.confirmBtn.setFont(font)
        self.confirmBtn.setStyleSheet("background-color: rgba(255, 100,10);\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);")
        self.confirmBtn.setObjectName("confirmBtn")
        self.verticalLayout.addWidget(self.confirmBtn)
        self.horizontalLayout.addWidget(self.frame)

        self.confirmBtn.clicked.connect(lambda:self.findWeather(self.cityNameEntry.text()))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.enterNameLabel.setText(_translate("Dialog", "Enter name of a city:"))
        self.confirmBtn.setText(_translate("Dialog", "Show Weather"))

    def findWeather(self,city):
        if city!="":
            str="http://api.openweathermap.org/data/2.5/weather?q={}&APPID={}".format(city,APICODE)
            r = requests.get(str)
            data = json.loads(r.text)
            if data['cod']=='404':
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText("City not found")
                msg.setWindowTitle("Error")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
            else:
                import show
                Dialog = QtWidgets.QDialog()
                ui = show.Ui_Dialog()
                cityname=data['name']
                weather=data['weather'][0]['main']
                temp=data['main']['temp']
                ui.setupUi(Dialog,cityname,weather,temp)
                Dialog.show()
                Dialog.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
