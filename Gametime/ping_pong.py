from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 600)
        MainWindow.setMinimumSize(QtCore.QSize(400, 600))
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setMaximumSize(QtCore.QSize(400, 600))
        MainWindow.setStyleSheet("background-color: rgb(181, 191, 255)\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.backmenu = QtWidgets.QPushButton(self.centralwidget)
        self.backmenu.setGeometry(QtCore.QRect(20, 480, 361, 101))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(18)
        self.backmenu.setFont(font)
        self.backmenu.setStyleSheet("QPushButton{\n"
"    background-color: rgb(172, 177, 214);\n"
"    border-radius: 10px;\n"
"} \n"
"QPushButton::pressed {\n"
"    background-color : rgb(206, 209, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"")
        self.backmenu.setObjectName("backmenu")
        self.downbackground = QtWidgets.QLabel(self.centralwidget)
        self.downbackground.setGeometry(QtCore.QRect(-4, 460, 411, 141))
        self.downbackground.setStyleSheet("background-color: rgb(219, 223, 234)")
        self.downbackground.setText("")
        self.downbackground.setObjectName("downbackground")
        self.upbackground = QtWidgets.QLabel(self.centralwidget)
        self.upbackground.setGeometry(QtCore.QRect(0, 0, 401, 81))
        self.upbackground.setStyleSheet("background-color: rgb(219, 223, 234)")
        self.upbackground.setText("")
        self.upbackground.setObjectName("upbackground")
        self.count = QtWidgets.QLabel(self.centralwidget)
        self.count.setGeometry(QtCore.QRect(160, 20, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(20)
        self.count.setFont(font)
        self.count.setStyleSheet("border-radius: 20px")
        self.count.setObjectName("count")
        self.player = QtWidgets.QLabel(self.centralwidget)
        self.player.setGeometry(QtCore.QRect(140, 410, 111, 20))
        self.player.setStyleSheet("QLabel{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 10px\n"
"}")
        self.player.setText("")
        self.player.setObjectName("player")
        self.player_2 = QtWidgets.QLabel(self.centralwidget)
        self.player_2.setGeometry(QtCore.QRect(140, 110, 111, 20))
        self.player_2.setStyleSheet("QLabel{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 10px\n"
"}")
        self.player_2.setText("")
        self.player_2.setObjectName("player_2")
        self.ball = QtWidgets.QLabel(self.centralwidget)
        self.ball.setGeometry(QtCore.QRect(180, 250, 21, 20))
        self.ball.setStyleSheet("QLabel{\n"
"    background-color:rgb(112, 119, 255);\n"
"    border-radius: 10px;\n"
"}")
        self.ball.setText("")
        self.ball.setObjectName("ball")
        self.downbackground.raise_()
        self.backmenu.raise_()
        self.upbackground.raise_()
        self.count.raise_()
        self.player.raise_()
        self.player_2.raise_()
        self.ball.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.backmenu.setText(_translate("MainWindow", "Menu"))
        self.count.setText(_translate("MainWindow", "    0 "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
