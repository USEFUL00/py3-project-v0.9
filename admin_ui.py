# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(975, 815)
        Form.setMinimumSize(QtCore.QSize(975, 815))
        Form.setMaximumSize(QtCore.QSize(975, 815))
        Form.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(90, 10, 851, 101))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tital_label = QtWidgets.QLabel(self.frame)
        self.tital_label.setGeometry(QtCore.QRect(340, 0, 161, 81))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.tital_label.setFont(font)
        self.tital_label.setMouseTracking(False)
        self.tital_label.setStyleSheet("font-size: 24px; /* Larger font size for titles */  \n"
"    font-weight: bold; /* Bold text */  \n"
"    color: #F6A600; /* Lemon color */  font-size: 24px; /* Larger font size for titles */  \n"
"    font-weight: bold; /* Bold text */  \n"
"    color: #F6A600; /* Lemon color */ ")
        self.tital_label.setObjectName("tital_label")
        self.subtital_label = QtWidgets.QLabel(self.frame)
        self.subtital_label.setGeometry(QtCore.QRect(320, 50, 191, 31))
        self.subtital_label.setStyleSheet("QLabel {\n"
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
        self.subtital_label.setObjectName("subtital_label")
        self.result_frame = QtWidgets.QFrame(self.centralwidget)
        self.result_frame.setGeometry(QtCore.QRect(-10, 110, 971, 271))
        self.result_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.result_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.result_frame.setObjectName("result_frame")
        self.tableWidget = QtWidgets.QTableWidget(self.result_frame)
        self.tableWidget.setGeometry(QtCore.QRect(20, 0, 951, 291))
        self.tableWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget.setStyleSheet("/* Styling the overall QTableWidget with a transparent edge and soft rounded corners */\n"
"QTableWidget {\n"
"    background-color: rgba(240, 240, 240, 0.9); /* Soft gray with 90% opacity */\n"
"    font-family: \"Courier New\", Courier, monospace;\n"
"    border-radius: 8px; /* Soft rounded corners */\n"
"    border: 1px solid rgba(200, 200, 200, 0.5); /* Light gray border with 50% opacity */\n"
"    color: black; /* Black text */\n"
"    gridline-color: rgba(200, 200, 200, 0.5); /* Transparent gridlines */\n"
"}\n"
"\n"
"/* Styling the viewport with a transparent background */\n"
"QTableView {\n"
"    background-color: rgba(240, 240, 240, 0.9); /* Same semi-transparent gray */\n"
"}\n"
"\n"
"/* Styling the header with a slightly darker transparent gray */\n"
"QHeaderView::section {\n"
"    background-color: rgba(220, 220, 220, 0.9); /* Darker gray with transparency */\n"
"    color: black; /* Black text */\n"
"    font-weight: bold;\n"
"    padding: 5px 10px;\n"
"    font-size: 0.95rem;\n"
"    border-bottom: 1px solid rgba(180, 180, 180, 0.5); /* Transparent gray border */\n"
"    border-top-left-radius: 8px;\n"
"    border-top-right-radius: 8px;\n"
"}\n"
"\n"
"/* Styling individual table cells with semi-transparent background */\n"
"QTableWidget::item {\n"
"    padding: 3px 0;\n"
"    background-color: rgba(240, 240, 240, 0.9); /* Soft gray with transparency */\n"
"    color: black; /* Black text */\n"
"}\n"
"\n"
"/* Alternating row colors for a striped effect with transparency */\n"
"QTableWidget::item:nth-child(even) {\n"
"    background-color: rgba(230, 230, 230, 0.9); /* Slightly darker transparent gray */\n"
"}\n"
"\n"
"/* Adding transparent side and bottom borders */\n"
"QTableWidget::item {\n"
"    border-right: 1px solid rgba(200, 200, 200, 0.5);\n"
"    border-left: 1px solid rgba(200, 200, 200, 0.5);\n"
"    border-bottom: 1px solid rgba(200, 200, 200, 0.5);\n"
"}\n"
"\n"
"/* Selected item style with stronger contrast */\n"
"QTableWidget::item:selected {\n"
"    background-color: rgba(160, 160, 160, 0.8); /* Darker transparent gray */\n"
"    color: white; /* White text for selected items */\n"
"}\n"
"\n"
"/* Styling the corner button (top-left of the table) */\n"
"QTableCornerButton::section {\n"
"    background-color: rgba(220, 220, 220, 0.9); /* Transparent gray background */\n"
"    border-top-left-radius: 8px;\n"
"    border-top-right-radius: 8px;\n"
"    border: 1px solid rgba(180, 180, 180, 0.5); /* Transparent gray border */\n"
"}\n"
"QHeaderView::section{\n"
"    border: none;\n"
"    border-bottom:1px solid #d0c6ff;\n"
"    text-align:left;\n"
"    padding: 3px 5px;\n"
"}\n"
"#result_frame {\n"
"    border-radius: 5px;\n"
"    background-color: #fff;\n"
"}")
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(238)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(60)
        self.tableWidget.verticalHeader().setVisible(False)
        self.function_frame = QtWidgets.QFrame(self.centralwidget)
        self.function_frame.setGeometry(QtCore.QRect(0, 370, 971, 121))
        self.function_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.function_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.function_frame.setObjectName("function_frame")
        self.add_btn = QtWidgets.QPushButton(self.function_frame)
        self.add_btn.setGeometry(QtCore.QRect(70, 30, 124, 53))
        self.add_btn.setMinimumSize(QtCore.QSize(124, 44))
        self.add_btn.setStyleSheet("/* Small, horizontally egg-shaped QPushButton with green color and hover effects */\n"
"QPushButton {\n"
"  cursor: pointer;\n"
"  position: relative;\n"
"  padding: 5px 20px;  /* Smaller padding for a compact look */\n"
"  font-size: 14px;  /* Smaller font size */\n"
"  color: rgb(0, 0, 0);  /* Text color */\n"
"  border: 2px solid #4CAF50;  /* Green border color */\n"
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
"  background-color: #4CAF50;  /* Green background on hover */\n"
"  color: #212121;  /* Darker text color on hover */\n"
"  box-shadow: 0 0px 10px rgba(76, 175, 80, 0.4);  /* Light green shadow on hover */\n"
"  padding: 6px 22px;  /* Simulate slight button scale */\n"
"  border-radius: 25px;  /* Maintain egg shape on hover */\n"
"}\n"
"\n"
"/* Pressed effect */\n"
"QPushButton:pressed {\n"
"  background-color: rgba(76, 175, 80, 0.8);  /* Slightly darker green when pressed */\n"
"  padding: 5px 20px;  /* Return to original size */\n"
"  box-shadow: none;  /* Remove shadow when pressed */\n"
"  border-radius: 25px;  /* Maintain egg shape when pressed */\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/moaza/Downloads/add_24dp_000000_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_btn.setIcon(icon)
        self.add_btn.setObjectName("add_btn")
        self.search_btn = QtWidgets.QPushButton(self.function_frame)
        self.search_btn.setGeometry(QtCore.QRect(350, 30, 131, 51))
        self.search_btn.setMinimumSize(QtCore.QSize(124, 44))
        self.search_btn.setStyleSheet("/* Small, horizontally egg-shaped QPushButton with soft blue, softer black text, and icon */\n"
"QPushButton {\n"
"  cursor: pointer;\n"
"  position: relative;\n"
"  padding: 5px 20px;  /* Compact padding */\n"
"  font-size: 14px;  /* Font size */\n"
"  color: #333333;  /* Softer black (deep gray) text */\n"
"  font-weight: bold;  /* Bold text */\n"
"  border: 2px solid #5a8fd6;  /* Softer blue border */\n"
"  border-radius: 25px;  /* Egg shape */\n"
"  background-color: transparent;  /* Transparent background */\n"
"  transition: all 0.3s ease-in-out;  /* Smooth transition */\n"
"  min-height: 30px;  /* Small height */\n"
"  min-width: 80px;   /* Compact width */\n"
"}\n"
"\n"
"/* Hover effect */\n"
"QPushButton:hover {\n"
"  background-color: #5a8fd6;  /* Softer blue background on hover */\n"
"  color: #333333;  /* Softer black (deep gray) text remains on hover */\n"
"  box-shadow: 0 0px 10px rgba(90, 143, 214, 0.4);  /* Softer blue shadow */\n"
"  padding: 6px 22px;  /* Simulate button scale */\n"
"  border-radius: 25px;  /* Maintain egg shape */\n"
"}\n"
"\n"
"/* Pressed effect */\n"
"QPushButton:pressed {\n"
"  background-color: rgba(90, 143, 214, 0.8);  /* Slightly darker blue background when pressed */\n"
"  padding: 5px 20px;  /* Return to original size */\n"
"  box-shadow: none;  /* No shadow on press */\n"
"  border-radius: 25px;  /* Maintain egg shape */\n"
"}\n"
"\n"
"/* Icon styling */\n"
"QPushButton::icon {\n"
"  color: #333333;  /* Icon color matches softer black (deep\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/moaza/Downloads/search_24dp_000000_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_btn.setIcon(icon1)
        self.search_btn.setObjectName("search_btn")
        self.update_btn = QtWidgets.QPushButton(self.function_frame)
        self.update_btn.setGeometry(QtCore.QRect(210, 30, 124, 51))
        self.update_btn.setMinimumSize(QtCore.QSize(124, 44))
        self.update_btn.setStyleSheet("/* Small, horizontally egg-shaped QPushButton with solid yellow color and updated effects */\n"
"QPushButton {\n"
"  cursor: pointer;\n"
"  position: relative;\n"
"  padding: 5px 20px;  /* Smaller padding for a compact look */\n"
"  font-size: 14px;  /* Smaller font size */\n"
"  color: rgb(0, 0, 0);  /* Text color */\n"
"  border: 2px solid #FFD700;  /* Solid yellow border */\n"
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
"  background-color: #FFD700;  /* Solid yellow background on hover */\n"
"  color: #212121;  /* Darker text color on hover */\n"
"  box-shadow: 0 0px 10px rgba(255, 215, 0, 0.4);  /* Light shadow on hover */\n"
"  padding: 6px 22px;  /* Simulate slight button scale */\n"
"  border-radius: 25px;  /* Maintain egg shape on hover */\n"
"}\n"
"\n"
"/* Pressed effect */\n"
"QPushButton:pressed {\n"
"  background-color: #FFC107;  /* Slightly darker yellow when pressed */\n"
"  padding: 5px 20px;  /* Return to original size */\n"
"  box-shadow: none;  /* Remove shadow when pressed */\n"
"  border-radius: 25px;  /* Maintain egg shape when pressed */\n"
"}\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/moaza/Downloads/edit_24dp_000000_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.update_btn.setIcon(icon2)
        self.update_btn.setObjectName("update_btn")
        self.select_btn = QtWidgets.QPushButton(self.function_frame)
        self.select_btn.setGeometry(QtCore.QRect(490, 30, 124, 51))
        self.select_btn.setMinimumSize(QtCore.QSize(124, 44))
        self.select_btn.setStyleSheet("/* Small, horizontally egg-shaped QPushButton with solid orange color and updated effects */\n"
"QPushButton {\n"
"  cursor: pointer;\n"
"  position: relative;\n"
"  padding: 5px 20px;  /* Smaller padding for a compact look */\n"
"  font-size: 14px;  /* Smaller font size */\n"
"  color: rgb(0, 0, 0);  /* Text color */\n"
"  border: 2px solid #FFA500;  /* Solid orange border */\n"
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
"  background-color: #FFA500;  /* Solid orange background on hover */\n"
"  color: #212121;  /* Darker text color on hover */\n"
"  box-shadow: 0 0px 10px rgba(255, 165, 0, 0.4);  /* Light shadow on hover */\n"
"  padding: 6px 22px;  /* Simulate slight button scale */\n"
"  border-radius: 25px;  /* Maintain egg shape on hover */\n"
"}\n"
"\n"
"/* Pressed effect */\n"
"QPushButton:pressed {\n"
"  background-color: #FF8C00;  /* Slightly darker orange when pressed */\n"
"  padding: 5px 20px;  /* Return to original size */\n"
"  box-shadow: none;  /* Remove shadow when pressed */\n"
"  border-radius: 25px;  /* Maintain egg shape when pressed */\n"
"}\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:/Users/moaza/Downloads/check_circle_24dp_000000_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.select_btn.setIcon(icon3)
        self.select_btn.setObjectName("select_btn")
        self.delete_btn = QtWidgets.QPushButton(self.function_frame)
        self.delete_btn.setGeometry(QtCore.QRect(630, 30, 124, 51))
        self.delete_btn.setMinimumSize(QtCore.QSize(124, 44))
        self.delete_btn.setStyleSheet("/* Small, horizontally egg-shaped QPushButton with updated red color and hover effects */\n"
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
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("C:/Users/moaza/Downloads/delete_24dp_000000_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_btn.setIcon(icon4)
        self.delete_btn.setObjectName("delete_btn")
        self.exit_btn = QtWidgets.QPushButton(self.function_frame)
        self.exit_btn.setGeometry(QtCore.QRect(770, 30, 124, 51))
        self.exit_btn.setMinimumSize(QtCore.QSize(124, 44))
        self.exit_btn.setStyleSheet("/* Small, horizontally egg-shaped QPushButton with updated red color and hover effects */\n"
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
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("C:/Users/moaza/Downloads/logout_24dp_000000_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_btn.setIcon(icon5)
        self.exit_btn.setObjectName("exit_btn")
        self.info_frame = QtWidgets.QFrame(self.centralwidget)
        self.info_frame.setGeometry(QtCore.QRect(0, 460, 971, 311))
        self.info_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.info_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.info_frame.setObjectName("info_frame")
        self.label_5 = QtWidgets.QLabel(self.info_frame)
        self.label_5.setGeometry(QtCore.QRect(250, 190, 51, 41))
        self.label_5.setStyleSheet("QLabel {\n"
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
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.info_frame)
        self.label_6.setGeometry(QtCore.QRect(250, 140, 51, 41))
        self.label_6.setStyleSheet("QLabel {\n"
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
        self.label_6.setObjectName("label_6")
        self.studentage = QtWidgets.QLineEdit(self.info_frame)
        self.studentage.setGeometry(QtCore.QRect(310, 190, 351, 41))
        self.studentage.setStyleSheet("QLineEdit {\n"
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
        self.studentage.setText("")
        self.studentage.setObjectName("studentage")
        self.studentsalary = QtWidgets.QLineEdit(self.info_frame)
        self.studentsalary.setGeometry(QtCore.QRect(310, 140, 351, 41))
        self.studentsalary.setStyleSheet("QLineEdit {\n"
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
        self.studentsalary.setText("")
        self.studentsalary.setObjectName("studentsalary")
        self.label_3 = QtWidgets.QLabel(self.info_frame)
        self.label_3.setGeometry(QtCore.QRect(250, 90, 51, 41))
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
        self.studentid = QtWidgets.QLineEdit(self.info_frame)
        self.studentid.setGeometry(QtCore.QRect(310, 40, 351, 41))
        self.studentid.setStyleSheet("QLineEdit {\n"
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
        self.studentid.setText("")
        self.studentid.setObjectName("studentid")
        self.studentname = QtWidgets.QLineEdit(self.info_frame)
        self.studentname.setGeometry(QtCore.QRect(310, 90, 351, 41))
        self.studentname.setStyleSheet("QLineEdit {\n"
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
        self.studentname.setText("")
        self.studentname.setObjectName("studentname")
        self.label_2 = QtWidgets.QLabel(self.info_frame)
        self.label_2.setGeometry(QtCore.QRect(250, 40, 51, 41))
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
        self.cleare_btn = QtWidgets.QPushButton(self.info_frame)
        self.cleare_btn.setGeometry(QtCore.QRect(310, 250, 351, 51))
        self.cleare_btn.setMinimumSize(QtCore.QSize(124, 44))
        self.cleare_btn.setStyleSheet("/* Small, horizontally egg-shaped QPushButton with updated red color and hover effects */\n"
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
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("image/arrow-back.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cleare_btn.setIcon(icon6)
        self.cleare_btn.setObjectName("cleare_btn")
        Form.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Form)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 975, 26))
        self.menubar.setObjectName("menubar")
        Form.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Form)
        self.statusbar.setObjectName("statusbar")
        Form.setStatusBar(self.statusbar)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MainWindow"))
        self.tital_label.setText(_translate("Form", "ADMIN PAGE"))
        self.subtital_label.setText(_translate("Form", " To Manage Students Data"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "NAME"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "SALARY"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "AGE"))
        self.add_btn.setText(_translate("Form", "Add "))
        self.search_btn.setText(_translate("Form", "SEARCH"))
        self.update_btn.setText(_translate("Form", "Edit "))
        self.select_btn.setText(_translate("Form", "SELECT"))
        self.delete_btn.setText(_translate("Form", "Remove "))
        self.exit_btn.setText(_translate("Form", "EXIT"))
        self.label_5.setText(_translate("Form", "Age"))
        self.label_6.setText(_translate("Form", "Salary"))
        self.label_3.setText(_translate("Form", "Name"))
        self.label_2.setText(_translate("Form", "ID"))
        self.cleare_btn.setText(_translate("Form", "CLEAR"))
