# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(929, 519)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 931, 521))
        self.label.setStyleSheet("            font-family: \"Arial\";\n"
"            font-size: 24px;\n"
"            font-weight: bold;\n"
"            color: white;\n"
"            background-color: green;  /* 绿色背景 */\n"
"            border: 2px solid white;\n"
"            border-radius: 10px;\n"
"            padding: 10px;\n"
"            text-align: center;\n"
"            background-image: url(\"D:/大三下/企业实训/第一周_图像识别api调用/project1/data/背景0.JPG\");\n"
"            background-position: center;\n"
"            background-repeat: no-repeat;\n"
"            background-size: cover;  /* 调整背景图片的大小，使其覆盖标签 */\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(280, 60, 371, 51))
        self.label_2.setStyleSheet("    font-family: \"Arial\";\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: white;\n"
"    background-color: green;\n"
"    border: 2px solid white;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    text-align: center;")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(140, 380, 151, 61))
        self.pushButton.setStyleSheet("    font-family: \"Arial\";\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    color: white;\n"
"    background-color: #4CAF50;  /* 绿色背景 */\n"
"    border: 2px solid #4CAF50;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    margin: 5px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 380, 161, 61))
        self.pushButton_2.setStyleSheet("    font-family: \"Arial\";\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    color: white;\n"
"    background-color: #4CAF50;  /* 绿色背景 */\n"
"    border: 2px solid #4CAF50;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    margin: 5px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(650, 380, 161, 61))
        self.pushButton_3.setStyleSheet("    font-family: \"Arial\";\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    color: white;\n"
"    background-color: #4CAF50;  /* 绿色背景 */\n"
"    border: 2px solid #4CAF50;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    margin: 5px;")
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.landgoin) # type: ignore
        self.pushButton_2.clicked.connect(Dialog.animalgoin) # type: ignore
        self.pushButton_3.clicked.connect(Dialog.plantgoin) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "穷游世界——您身边的安全管家"))
        self.pushButton.setText(_translate("Dialog", "迷路-地标识别"))
        self.pushButton_2.setText(_translate("Dialog", "危险-动物识别"))
        self.pushButton_3.setText(_translate("Dialog", "有毒-植物识别"))