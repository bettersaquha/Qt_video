# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plant_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(932, 520)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-7, -8, 941, 531))
        self.label.setStyleSheet("            font-family: \"Arial\";\n"
"            font-size: 24px;\n"
"            font-weight: bold;\n"
"            color: white;\n"
"            background-color: green;  /* 绿色背景 */\n"
"            border: 2px solid white;\n"
"            border-radius: 10px;\n"
"            padding: 10px;\n"
"            text-align: center;\n"
"            background-image: url(\"D:/大三下/企业实训/第一周_图像识别api调用/project1/data/植物0.JPG\");\n"
"            background-position: center;\n"
"            background-repeat: no-repeat;\n"
"            background-size: cover;  /* 调整背景图片的大小，使其覆盖标签 */")
        self.label.setText("")
        self.label.setObjectName("label")
        self.plant_video = QtWidgets.QLabel(Dialog)
        self.plant_video.setGeometry(QtCore.QRect(200, 190, 531, 301))
        self.plant_video.setText("")
        self.plant_video.setObjectName("plant_video")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(140, 50, 111, 41))
        self.label_2.setStyleSheet("font-family: \"Arial\";\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    color: white;  /* 白色文字 */\n"
"    background-color: #228B22;  /* 森林绿色背景 */\n"
"    border: 2px solid #006400;  /* 深绿色边框 */\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    text-align: center;\n"
"    box-shadow: 2px 2px 10px rgba(0, 64, 0, 0.5);  /* 添加深绿色阴影效果 */")
        self.label_2.setObjectName("label_2")
        self.plant_pro1 = QtWidgets.QLabel(Dialog)
        self.plant_pro1.setGeometry(QtCore.QRect(250, 50, 111, 41))
        self.plant_pro1.setStyleSheet("font-family: \"Arial\";\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    color: white;  /* 白色文字 */\n"
"    background-color: #228B22;  /* 森林绿色背景 */\n"
"    border: 2px solid #006400;  /* 深绿色边框 */\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    text-align: center;\n"
"    box-shadow: 2px 2px 10px rgba(0, 64, 0, 0.5);  /* 添加深绿色阴影效果 */")
        self.plant_pro1.setObjectName("plant_pro1")
        self.plant1 = QtWidgets.QLabel(Dialog)
        self.plant1.setGeometry(QtCore.QRect(30, 50, 111, 41))
        self.plant1.setStyleSheet("font-family: \"Arial\";\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    color: white;  /* 白色文字 */\n"
"    background-color: #228B22;  /* 森林绿色背景 */\n"
"    border: 2px solid #006400;  /* 深绿色边框 */\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    text-align: center;\n"
"    box-shadow: 2px 2px 10px rgba(0, 64, 0, 0.5);  /* 添加深绿色阴影效果 */")
        self.plant1.setObjectName("plant1")
        self.plant_pro2 = QtWidgets.QLabel(Dialog)
        self.plant_pro2.setGeometry(QtCore.QRect(250, 110, 111, 41))
        self.plant_pro2.setStyleSheet("font-family: \"Arial\";\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    color: white;  /* 白色文字 */\n"
"    background-color: #228B22;  /* 森林绿色背景 */\n"
"    border: 2px solid #006400;  /* 深绿色边框 */\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    text-align: center;\n"
"    box-shadow: 2px 2px 10px rgba(0, 64, 0, 0.5);  /* 添加深绿色阴影效果 */")
        self.plant_pro2.setObjectName("plant_pro2")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(140, 110, 111, 41))
        self.label_6.setStyleSheet("font-family: \"Arial\";\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    color: white;  /* 白色文字 */\n"
"    background-color: #228B22;  /* 森林绿色背景 */\n"
"    border: 2px solid #006400;  /* 深绿色边框 */\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    text-align: center;\n"
"    box-shadow: 2px 2px 10px rgba(0, 64, 0, 0.5);  /* 添加深绿色阴影效果 */")
        self.label_6.setObjectName("label_6")
        self.plant2 = QtWidgets.QLabel(Dialog)
        self.plant2.setGeometry(QtCore.QRect(30, 110, 111, 41))
        self.plant2.setStyleSheet("font-family: \"Arial\";\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    color: white;  /* 白色文字 */\n"
"    background-color: #228B22;  /* 森林绿色背景 */\n"
"    border: 2px solid #006400;  /* 深绿色边框 */\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    text-align: center;\n"
"    box-shadow: 2px 2px 10px rgba(0, 64, 0, 0.5);  /* 添加深绿色阴影效果 */")
        self.plant2.setObjectName("plant2")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(650, 50, 111, 41))
        self.label_8.setStyleSheet("font-family: \"Arial\";\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    color: white;  /* 白色文字 */\n"
"    background-color: #228B22;  /* 森林绿色背景 */\n"
"    border: 2px solid #006400;  /* 深绿色边框 */\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    text-align: center;\n"
"    box-shadow: 2px 2px 10px rgba(0, 64, 0, 0.5);  /* 添加深绿色阴影效果 */")
        self.label_8.setObjectName("label_8")
        self.plant_pro3 = QtWidgets.QLabel(Dialog)
        self.plant_pro3.setGeometry(QtCore.QRect(760, 50, 111, 41))
        self.plant_pro3.setStyleSheet("font-family: \"Arial\";\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    color: white;  /* 白色文字 */\n"
"    background-color: #228B22;  /* 森林绿色背景 */\n"
"    border: 2px solid #006400;  /* 深绿色边框 */\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    text-align: center;\n"
"    box-shadow: 2px 2px 10px rgba(0, 64, 0, 0.5);  /* 添加深绿色阴影效果 */")
        self.plant_pro3.setObjectName("plant_pro3")
        self.plant3 = QtWidgets.QLabel(Dialog)
        self.plant3.setGeometry(QtCore.QRect(540, 50, 111, 41))
        self.plant3.setStyleSheet("font-family: \"Arial\";\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    color: white;  /* 白色文字 */\n"
"    background-color: #228B22;  /* 森林绿色背景 */\n"
"    border: 2px solid #006400;  /* 深绿色边框 */\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    text-align: center;\n"
"    box-shadow: 2px 2px 10px rgba(0, 64, 0, 0.5);  /* 添加深绿色阴影效果 */")
        self.plant3.setObjectName("plant3")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(650, 110, 111, 41))
        self.label_11.setStyleSheet("font-family: \"Arial\";\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    color: white;  /* 白色文字 */\n"
"    background-color: #228B22;  /* 森林绿色背景 */\n"
"    border: 2px solid #006400;  /* 深绿色边框 */\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    text-align: center;\n"
"    box-shadow: 2px 2px 10px rgba(0, 64, 0, 0.5);  /* 添加深绿色阴影效果 */")
        self.label_11.setObjectName("label_11")
        self.plant_pro4 = QtWidgets.QLabel(Dialog)
        self.plant_pro4.setGeometry(QtCore.QRect(760, 110, 111, 41))
        self.plant_pro4.setStyleSheet("font-family: \"Arial\";\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    color: white;  /* 白色文字 */\n"
"    background-color: #228B22;  /* 森林绿色背景 */\n"
"    border: 2px solid #006400;  /* 深绿色边框 */\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    text-align: center;\n"
"    box-shadow: 2px 2px 10px rgba(0, 64, 0, 0.5);  /* 添加深绿色阴影效果 */")
        self.plant_pro4.setObjectName("plant_pro4")
        self.plant4 = QtWidgets.QLabel(Dialog)
        self.plant4.setGeometry(QtCore.QRect(540, 110, 111, 41))
        self.plant4.setStyleSheet("font-family: \"Arial\";\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    color: white;  /* 白色文字 */\n"
"    background-color: #228B22;  /* 森林绿色背景 */\n"
"    border: 2px solid #006400;  /* 深绿色边框 */\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    text-align: center;\n"
"    box-shadow: 2px 2px 10px rgba(0, 64, 0, 0.5);  /* 添加深绿色阴影效果 */")
        self.plant4.setObjectName("plant4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "可能性为："))
        self.plant_pro1.setText(_translate("Dialog", "0"))
        self.plant1.setText(_translate("Dialog", "？"))
        self.plant_pro2.setText(_translate("Dialog", "0"))
        self.label_6.setText(_translate("Dialog", "可能性为："))
        self.plant2.setText(_translate("Dialog", "？"))
        self.label_8.setText(_translate("Dialog", "可能性为："))
        self.plant_pro3.setText(_translate("Dialog", "0"))
        self.plant3.setText(_translate("Dialog", "？"))
        self.label_11.setText(_translate("Dialog", "可能性为："))
        self.plant_pro4.setText(_translate("Dialog", "0"))
        self.plant4.setText(_translate("Dialog", "？"))
