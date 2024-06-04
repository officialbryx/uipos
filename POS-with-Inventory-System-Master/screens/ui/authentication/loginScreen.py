# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 723)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 2, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 2, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem3, 0, 1, 1, 1)
        self.widget = QtWidgets.QWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logoContainer = QtWidgets.QWidget(self.widget)
        self.logoContainer.setObjectName("logoContainer")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.logoContainer)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.logo = QtWidgets.QLabel(self.logoContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMinimumSize(QtCore.QSize(250, 80))
        self.logo.setMaximumSize(QtCore.QSize(250, 80))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/logos/Icons/logo1.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.horizontalLayout_2.addWidget(self.logo)
        self.verticalLayout.addWidget(self.logoContainer)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.loginForm = QtWidgets.QWidget(self.widget)
        self.loginForm.setStyleSheet("QWidget {\n"
"    background-color: #07BEB8;\n"
"    border-radius: 25px;\n"
"}\n"
"")
        self.loginForm.setObjectName("loginForm")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.loginForm)
        self.verticalLayout_2.setContentsMargins(40, 40, 40, 40)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.welcomeLabel = QtWidgets.QLabel(self.loginForm)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.welcomeLabel.setFont(font)
        self.welcomeLabel.setObjectName("welcomeLabel")
        self.verticalLayout_2.addWidget(self.welcomeLabel)
        self.guideLabel = QtWidgets.QLabel(self.loginForm)
        self.guideLabel.setMinimumSize(QtCore.QSize(325, 46))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.guideLabel.setFont(font)
        self.guideLabel.setScaledContents(False)
        self.guideLabel.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.guideLabel.setWordWrap(True)
        self.guideLabel.setObjectName("guideLabel")
        self.verticalLayout_2.addWidget(self.guideLabel)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.userNameLBL = QtWidgets.QLabel(self.loginForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.userNameLBL.setFont(font)
        self.userNameLBL.setObjectName("userNameLBL")
        self.verticalLayout_2.addWidget(self.userNameLBL)
        self.userName = QtWidgets.QLineEdit(self.loginForm)
        self.userName.setMinimumSize(QtCore.QSize(325, 46))
        self.userName.setMaximumSize(QtCore.QSize(325, 46))
        self.userName.setStyleSheet("QLineEdit {\n"
"    padding: 5px;\n"
"    border-radius: 6px;\n"
"    background-color: #FFFFFF;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.userName.setObjectName("userName")
        self.verticalLayout_2.addWidget(self.userName)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem6)
        self.passLBL = QtWidgets.QLabel(self.loginForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.passLBL.setFont(font)
        self.passLBL.setObjectName("passLBL")
        self.verticalLayout_2.addWidget(self.passLBL)
        self.widget_2 = QtWidgets.QWidget(self.loginForm)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.password = QtWidgets.QLineEdit(self.widget_2)
        self.password.setMinimumSize(QtCore.QSize(295, 46))
        self.password.setMaximumSize(QtCore.QSize(295, 46))
        self.password.setStyleSheet("QLineEdit {\n"
"    padding: 5px;\n"
"    border-radius: 6px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    background-color: #FFFFFF;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.password.setObjectName("password")
        self.horizontalLayout_3.addWidget(self.password)
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setMinimumSize(QtCore.QSize(30, 46))
        self.pushButton.setMaximumSize(QtCore.QSize(30, 46))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    padding: 5px;\n"
"    background-color: #FFFFFF;\n"
"    border-radius: 6px;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logos/Icons/visibilityOff.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/logos/Icons/visibilityOn.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.verticalLayout_2.addWidget(self.widget_2)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem7)
        self.loginButton = QtWidgets.QPushButton(self.loginForm)
        self.loginButton.setMinimumSize(QtCore.QSize(325, 46))
        self.loginButton.setMaximumSize(QtCore.QSize(325, 46))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet("QPushButton {\n"
"    padding: 5px;\n"
"    border: 1px solid #036666;\n"
"    border-radius: 6px;\n"
"    background-color: #036666;\n"
"    color: white;\n"
"    font-size: 20px\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #049393;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #024c4c;\n"
"}")
        self.loginButton.setObjectName("loginButton")
        self.verticalLayout_2.addWidget(self.loginButton)
        self.forgotButton = QtWidgets.QPushButton(self.loginForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.forgotButton.setFont(font)
        self.forgotButton.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: #265C42;\n"
"}\n"
"")
        self.forgotButton.setObjectName("forgotButton")
        self.verticalLayout_2.addWidget(self.forgotButton)
        self.verticalLayout.addWidget(self.loginForm)
        self.gridLayout_3.addWidget(self.widget, 2, 1, 1, 1)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.loginButton.clicked.connect(self.redirectToPage)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.welcomeLabel.setText(_translate("MainWindow", "Welcome Back!"))
        self.guideLabel.setText(_translate("MainWindow", "Login your credentials to access the system."))
        self.userNameLBL.setText(_translate("MainWindow", "Username"))
        self.userName.setPlaceholderText(_translate("MainWindow", "Enter Username"))
        self.passLBL.setText(_translate("MainWindow", "Password"))
        self.password.setPlaceholderText(_translate("MainWindow", "Enter Password"))
        self.loginButton.setText(_translate("MainWindow", "Log In"))
        self.forgotButton.setText(_translate("MainWindow", "Forgot your password?"))

    def redirectToPage(self):
        from admin_ui import adminDashboard

        self.dashboardWindow = QtWidgets.QMainWindow()

        self.dashboardUI = adminDashboard()
        self.dashboardUI.setupUi(self.dashboardWindow)
        
        # Show the dashboard window
        self.dashboardWindow.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
