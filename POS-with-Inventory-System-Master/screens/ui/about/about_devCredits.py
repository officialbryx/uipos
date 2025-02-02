# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about_devCredits.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(963, 749)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.navBar = QtWidgets.QWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.navBar.sizePolicy().hasHeightForWidth())
        self.navBar.setSizePolicy(sizePolicy)
        self.navBar.setStyleSheet("QWidget {\n"
"    border-right: 3px solid #D8DBD9;\n"
"}\n"
"")
        self.navBar.setObjectName("navBar")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.navBar)
        self.verticalLayout_7.setSpacing(7)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem)
        self.editUserButton = QtWidgets.QPushButton(self.navBar)
        self.editUserButton.setMinimumSize(QtCore.QSize(100, 100))
        self.editUserButton.setMaximumSize(QtCore.QSize(100, 100))
        self.editUserButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.editUserButton.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid #67B99A;\n"
"    color: black;\n"
"    padding: 8px 16px;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #4D926D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #F0F0F0;\n"
"    border: 2px solid #265C42;\n"
"}")
        self.editUserButton.setAutoRepeat(False)
        self.editUserButton.setAutoExclusive(False)
        self.editUserButton.setObjectName("editUserButton")
        self.verticalLayout_7.addWidget(self.editUserButton)
        self.pushButton = QtWidgets.QPushButton(self.navBar)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid #67B99A;\n"
"    color: black;\n"
"    padding: 8px 16px;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #4D926D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #F0F0F0;\n"
"    border: 2px solid #265C42;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_7.addWidget(self.pushButton)
        self.backButton = QtWidgets.QPushButton(self.navBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backButton.sizePolicy().hasHeightForWidth())
        self.backButton.setSizePolicy(sizePolicy)
        self.backButton.setMinimumSize(QtCore.QSize(100, 100))
        self.backButton.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.backButton.setFont(font)
        self.backButton.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid #67B99A;\n"
"    color: black;\n"
"    padding: 8px 16px;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #4D926D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #F0F0F0;\n"
"    border: 2px solid #265C42;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logos/Icons/entypo_back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backButton.setIcon(icon)
        self.backButton.setAutoRepeat(False)
        self.backButton.setObjectName("backButton")
        self.verticalLayout_7.addWidget(self.backButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem1)
        self.gridLayout_2.addWidget(self.navBar, 1, 0, 1, 1)
        self.header = QtWidgets.QWidget(self.frame)
        self.header.setStyleSheet("QWidget {\n"
"    border-bottom: 3px solid #D8DBD9; \n"
"}\n"
"")
        self.header.setObjectName("header")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.titleLabel = QtWidgets.QLabel(self.header)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.titleLabel.setFont(font)
        self.titleLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.titleLabel.setStyleSheet("QLabel {\n"
"    color: #67B99A;\n"
"    font-size: 45px;\n"
"}")
        self.titleLabel.setScaledContents(False)
        self.titleLabel.setObjectName("titleLabel")
        self.horizontalLayout_13.addWidget(self.titleLabel)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem2)
        self.systemLabel = QtWidgets.QFrame(self.header)
        self.systemLabel.setObjectName("systemLabel")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.systemLabel)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.sysTimeDate = QtWidgets.QLabel(self.systemLabel)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sysTimeDate.setFont(font)
        self.sysTimeDate.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.sysTimeDate.setObjectName("sysTimeDate")
        self.verticalLayout_12.addWidget(self.sysTimeDate)
        self.userName = QtWidgets.QLabel(self.systemLabel)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.userName.setFont(font)
        self.userName.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.userName.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.userName.setObjectName("userName")
        self.verticalLayout_12.addWidget(self.userName)
        self.horizontalLayout_13.addWidget(self.systemLabel)
        self.gridLayout_2.addWidget(self.header, 0, 0, 1, 2)
        self.mainContent = QtWidgets.QWidget(self.frame)
        self.mainContent.setObjectName("mainContent")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.mainContent)
        self.verticalLayout_8.setContentsMargins(50, 50, 50, 50)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label = QtWidgets.QLabel(self.mainContent)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_8.addWidget(self.label)
        self.layoutContainer = QtWidgets.QWidget(self.mainContent)
        self.layoutContainer.setObjectName("layoutContainer")
        self.formLayout = QtWidgets.QFormLayout(self.layoutContainer)
        self.formLayout.setContentsMargins(0, 25, 0, 0)
        self.formLayout.setSpacing(25)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutContainer)
        self.label_3.setMinimumSize(QtCore.QSize(150, 150))
        self.label_3.setMaximumSize(QtCore.QSize(150, 150))
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.widget = QtWidgets.QWidget(self.layoutContainer)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.widget.setFont(font)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_8 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.label_8.setTextFormat(QtCore.Qt.AutoText)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_8.setWordWrap(False)
        self.label_8.setOpenExternalLinks(False)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.widget)
        self.widget_3 = QtWidgets.QWidget(self.layoutContainer)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.widget_3.setFont(font)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.label_10 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.widget_3)
        self.widget_2 = QtWidgets.QWidget(self.layoutContainer)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.widget_2.setFont(font)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setWordWrap(False)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_9 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.widget_2)
        self.label_4 = QtWidgets.QLabel(self.layoutContainer)
        self.label_4.setMinimumSize(QtCore.QSize(150, 150))
        self.label_4.setMaximumSize(QtCore.QSize(150, 150))
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_2 = QtWidgets.QLabel(self.layoutContainer)
        self.label_2.setMinimumSize(QtCore.QSize(150, 150))
        self.label_2.setMaximumSize(QtCore.QSize(150, 150))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/devCredits/Dev Credits/devCredits_VIllatura.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.verticalLayout_8.addWidget(self.layoutContainer)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem3)
        self.gridLayout_2.addWidget(self.mainContent, 1, 1, 1, 1)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.editUserButton.setText(_translate("MainWindow", "Info"))
        self.pushButton.setText(_translate("MainWindow", "Credits"))
        self.backButton.setText(_translate("MainWindow", "Back"))
        self.titleLabel.setText(_translate("MainWindow", "About"))
        self.sysTimeDate.setText(_translate("MainWindow", "November 28th 2023, 12:07AM"))
        self.userName.setText(_translate("MainWindow", "Juan Dela Cruz"))
        self.label.setText(_translate("MainWindow", "Development Credits"))
        self.label_3.setText(_translate("MainWindow", "Dev 1"))
        self.label_6.setText(_translate("MainWindow", "Ymnwl Jan P. Faurillo"))
        self.label_8.setText(_translate("MainWindow", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut\n"
" labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco\n"
" laboris nisi ut aliquip ex ea commodo consequat. "))
        self.label_7.setText(_translate("MainWindow", "Bryan Dominick A. TIamzon"))
        self.label_10.setText(_translate("MainWindow", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut\n"
" labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco\n"
" laboris nisi ut aliquip ex ea commodo consequat. "))
        self.label_5.setText(_translate("MainWindow", "Leah Desiree B. Villatura"))
        self.label_9.setText(_translate("MainWindow", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut\n"
" labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco\n"
" laboris nisi ut aliquip ex ea commodo consequat. "))
        self.label_4.setText(_translate("MainWindow", "Dev 2"))
import resourceFile_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
