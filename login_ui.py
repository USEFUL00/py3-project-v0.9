# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/login.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class login(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(975, 815)
        MainWindow.setMinimumSize(QtCore.QSize(975, 815))
        MainWindow.setMaximumSize(QtCore.QSize(975, 815))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(True)
        MainWindow.setStyleSheet(" background-color:rgb(255, 255, 255);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.loginbutton = QtWidgets.QPushButton(self.centralwidget)
        self.loginbutton.setGeometry(QtCore.QRect(330, 360, 342, 53))
        self.loginbutton.setMinimumSize(QtCore.QSize(124, 44))
        self.loginbutton.setStyleSheet("/* Small, horizontally egg-shaped QPushButton with yellow color and effects */\n"
"QPushButton {\n"
"  cursor: pointer;\n"
"  position: relative;\n"
"  padding: 5px 20px;  /* Smaller padding for a compact look */\n"
"  font-size: 14px;  /* Smaller font size */\n"
"  color: #rgb(0, 0, 0);  /* Light text color */\n"
"  border: 2px solid #f8c400;  /* Yellow border */\n"
"  border-radius: 25px;  /* Border-radius for an egg shape */\n"
"  background-color: transparent;  /* Transparent background */\n"
"  font-weight: bold;  /* Bold text */\n"
"  transition: all 0.3s ease-in-out;  /* Smooth transition */\n"
"  min-height: 30px;  /* Smaller height */\n"
"  min-width: 80px;   /* Smaller width for a compact egg shape */\n"
"}\n"
"\n"
"/* Hover effect */\n"
"QPushButton:hover {\n"
"  background-color: #f8c400;  /* Yellow background on hover */\n"
"  color: #212121;  /* Darker text color on hover */\n"
"  box-shadow: 0 0px 10px rgba(248, 196, 0, 0.4);  /* Light shadow on hover */\n"
"  padding: 6px 22px;  /* Simulate slight button scale */\n"
"  border-radius: 25px;  /* Maintain egg shape on hover */\n"
"}\n"
"\n"
"/* Pressed effect */\n"
"QPushButton:pressed {\n"
"  background-color: rgba(248, 196, 0, 0.8);  /* Slightly darker yellow when pressed */\n"
"  padding: 5px 20px;  /* Return to original size */\n"
"  box-shadow: none;  /* Remove shadow when pressed */\n"
"  border-radius: 25px;  /* Maintain egg shape when pressed */\n"
"}\n"
"")
        self.loginbutton.setObjectName("loginbutton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(460, 20, 81, 121))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setStyleSheet("font-size: 24px; /* Larger font size for titles */  \n"
"    font-weight: bold; /* Bold text */  \n"
"    color: #F6A600; /* Lemon color */  font-size: 24px; /* Larger font size for titles */  \n"
"    font-weight: bold; /* Bold text */  \n"
"    color: #F6A600; /* Lemon color */ ")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 160, 141, 31))
        self.label_2.setStyleSheet("QLabel {\n"
"    margin-bottom: 5px;  /* .3rem converted to px (roughly 5px) */\n"
"    font-size: 14px;     /* .9rem is approximately 14px */\n"
"    font-weight: bold;\n"
"    color: rgba(5, 6, 15, 153); /* Equivalent to #05060f99 */\n"
"    transition: color 0.3s cubic-bezier(0.25, 0.01, 0.25, 1);\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    color: rgba(5, 6, 15, 194); /* Equivalent to #05060fc2 */\n"
"}\n"
"")
        self.label_2.setObjectName("label_2")
        self.emailfield = QtWidgets.QLineEdit(self.centralwidget)
        self.emailfield.setGeometry(QtCore.QRect(330, 200, 351, 41))
        self.emailfield.setStyleSheet("QLineEdit {\n"
"    max-width: 342px;\n"
"    height: 53px;\n"
"    background-color: rgba(5, 6, 15, 10); /* #05060f0a */\n"
"    border-radius: 8px;  /* .5rem converted to px (roughly 8px) */\n"
"    padding: 0 10px;     /* Padding equivalent to 1rem */\n"
"    border: 2px solid transparent;\n"
"    font-size: 16px;     /* 1rem is approximately 16px */\n"
"    transition: border-color 0.3s cubic-bezier(0.25, 0.01, 0.25, 1),\n"
"                color 0.3s cubic-bezier(0.25, 0.01, 0.25, 1),\n"
"                background 0.2s cubic-bezier(0.25, 0.01, 0.25, 1);\n"
"}\n"
"\n"
"QLineEdit:hover, QLineEdit:focus {\n"
"    outline: none;\n"
"    border-color: #05060f;\n"
"}\n"
"")
        self.emailfield.setText("")
        self.emailfield.setObjectName("emailfield")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(340, 250, 91, 31))
        self.label_3.setStyleSheet("QLabel {\n"
"    margin-bottom: 5px;  /* .3rem converted to px (roughly 5px) */\n"
"    font-size: 14px;     /* .9rem is approximately 14px */\n"
"    font-weight: bold;\n"
"    color: rgba(5, 6, 15, 153); /* Equivalent to #05060f99 */\n"
"    transition: color 0.3s cubic-bezier(0.25, 0.01, 0.25, 1);\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    color: rgba(5, 6, 15, 194); /* Equivalent to #05060fc2 */\n"
"}\n"
"")
        self.label_3.setObjectName("label_3")
        self.passwordfield = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordfield.setGeometry(QtCore.QRect(330, 280, 351, 41))
        self.passwordfield.setStyleSheet("QLineEdit {\n"
"    max-width: 342px;\n"
"    height: 53px;\n"
"    background-color: rgba(5, 6, 15, 10); /* #05060f0a */\n"
"    border-radius: 8px;  /* .5rem converted to px (roughly 8px) */\n"
"    padding: 0 10px;     /* Padding equivalent to 1rem */\n"
"    border: 2px solid transparent;\n"
"    font-size: 16px;     /* 1rem is approximately 16px */\n"
"    transition: border-color 0.3s cubic-bezier(0.25, 0.01, 0.25, 1),\n"
"                color 0.3s cubic-bezier(0.25, 0.01, 0.25, 1),\n"
"                background 0.2s cubic-bezier(0.25, 0.01, 0.25, 1);\n"
"}\n"
"\n"
"QLineEdit:hover, QLineEdit:focus {\n"
"    outline: none;\n"
"    border-color: #05060f;\n"
"}\n"
"")
        self.passwordfield.setText("")
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.passwordfield.setObjectName("passwordfield")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(410, 500, 171, 31))
        self.label_4.setStyleSheet("QLabel {\n"
"    margin-bottom: 5px;  /* .3rem converted to px (roughly 5px) */\n"
"    font-size: 14px;     /* .9rem is approximately 14px */\n"
"    font-weight: bold;\n"
"    color: rgba(5, 6, 15, 153); /* Equivalent to #05060f99 */\n"
"    transition: color 0.3s cubic-bezier(0.25, 0.01, 0.25, 1);\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    color: rgba(5, 6, 15, 194); /* Equivalent to #05060fc2 */\n"
"}\n"
"")
        self.label_4.setObjectName("label_4")
        self.exitbutton = QtWidgets.QPushButton(self.centralwidget)
        self.exitbutton.setGeometry(QtCore.QRect(330, 590, 341, 51))
        self.exitbutton.setMinimumSize(QtCore.QSize(124, 44))
        self.exitbutton.setStyleSheet("/* Small, horizontally egg-shaped QPushButton with updated red color and hover effects */\n"
"QPushButton {\n"
"  cursor: pointer;\n"
"  position: relative;\n"
"  padding: 5px 20px;  /* Smaller padding for a compact look */\n"
"  font-size: 14px;  /* Smaller font size */\n"
"  color: rgb(0, 0, 0);  /* White text color */\n"
"  border: 2px solid #ff4c4c;  /* Red border color */\n"
"  border-radius: 25px;  /* Border-radius for an egg shape */\n"
"  background-color: transparent;  /* Transparent background */\n"
"  font-weight: bold;  /* Bold text */\n"
"  transition: all 0.3s ease-in-out;  /* Smooth transition */\n"
"  min-height: 30px;  /* Smaller height */\n"
"  min-width: 80px;   /* Smaller width for a compact egg shape */\n"
"}\n"
"\n"
"/* Hover effect */\n"
"QPushButton:hover {\n"
"  background-color: #ff4c4c;  /* Red background color on hover */\n"
"  color: #ffffff;  /* White text color on hover */\n"
"  box-shadow: 0 0px 10px rgba(255, 76, 76, 0.4);  /* Light shadow with red tint on hover */\n"
"  padding: 6px 22px;  /* Simulate slight button scale */\n"
"  border-radius: 25px;  /* Maintain egg shape on hover */\n"
"}\n"
"\n"
"/* Pressed effect */\n"
"QPushButton:pressed {\n"
"  background-color: rgba(255, 76, 76, 0.8);  /* Slightly darker red when pressed */\n"
"  padding: 5px 20px;  /* Return to original size */\n"
"  box-shadow: none;  /* Remove shadow when pressed */\n"
"  border-radius: 25px;  /* Maintain egg shape when pressed */\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("forms\\image/arrow-back.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitbutton.setIcon(icon)
        self.exitbutton.setObjectName("exitbutton")
        self.errorfield = QtWidgets.QLabel(self.centralwidget)
        self.errorfield.setGeometry(QtCore.QRect(340, 330, 331, 31))
        self.errorfield.setStyleSheet("QLabel {\n"
"    margin-bottom: 5px;  /* .3rem converted to px (roughly 5px) */\n"
"    font-size: 14px;     /* .9rem is approximately 14px */\n"
"    font-weight: bold;\n"
"    color: #FF0000;      /* Red color */\n"
"    transition: color 0.3s cubic-bezier(0.25, 0.01, 0.25, 1);\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    color: #FF4C4C;      /* Lighter red color on hover */\n"
"}\n"
"")
        self.errorfield.setText("")
        self.errorfield.setObjectName("errorfield")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 975, 26))
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
        self.loginbutton.setText(_translate("MainWindow", "LOGIN"))
        self.label.setText(_translate("MainWindow", "LOGIN "))
        self.label_2.setText(_translate("MainWindow", "Email or Username"))
        self.label_3.setText(_translate("MainWindow", "password"))
        self.label_4.setText(_translate("MainWindow", "dont have an account ?"))
        self.exitbutton.setText(_translate("MainWindow", "EXIT"))
