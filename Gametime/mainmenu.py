from PyQt5 import QtCore, QtGui, QtWidgets
from ping_pong import Ui_MainWindow
import sys

class Interface(QtWidgets.QMainWindow, QtWidgets.QWidget):
    def setupUi(self, MainWindow):        
        #MainWindow settings
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.resize(400, 600)
        MainWindow.setStyleSheet("background-color: rgb(181, 191, 255)\n"
        "\n"
        "")
        #UI_interface
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.first_game = QtWidgets.QPushButton(self.centralwidget)
        self.first_game.setGeometry(QtCore.QRect(20, 230, 361, 81))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(18)
        self.first_game.setFont(font)
        self.first_game.setStyleSheet("QPushButton{\n"
"    background-color: rgb(219, 223, 234);;\n"
"    border-radius: 10px;\n"
"} \n"
"QPushButton::pressed {\n"
"    background-color : rgb(206, 209, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.first_game.setObjectName("first_game")
        self.second_game = QtWidgets.QPushButton(self.centralwidget)
        self.second_game.setGeometry(QtCore.QRect(20, 320, 361, 81))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(18)
        self.second_game.setFont(font)
        self.second_game.setStyleSheet("QPushButton{\n"
"    background-color: rgb(219, 223, 234);;\n"
"    border-radius: 10px;\n"
"} \n"
"QPushButton::pressed {\n"
"    background-color : rgb(206, 209, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.second_game.setObjectName("second_game")
        self.third_game = QtWidgets.QPushButton(self.centralwidget)
        self.third_game.setGeometry(QtCore.QRect(20, 410, 361, 81))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(18)
        self.third_game.setFont(font)
        self.third_game.setStyleSheet("QPushButton{\n"
"    background-color: rgb(219, 223, 234);;\n"
"    border-radius: 10px;\n"
"} \n"
"QPushButton::pressed {\n"
"    background-color : rgb(206, 209, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.third_game.setObjectName("third_game")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(20, 500, 361, 81))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(18)
        self.exit.setFont(font)
        self.exit.setStyleSheet("QPushButton{\n"
"    background-color: rgb(172, 177, 214);\n"
"    border-radius: 10px;\n"
"} \n"
"QPushButton::pressed {\n"
"    background-color : rgb(206, 209, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"    \n"
"")
        self.exit.setObjectName("exit")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(10, 10, 381, 581))
        self.background.setStyleSheet("border-radius: 20px")
        self.background.setText("")
        self.background.setObjectName("background")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(20, 40, 361, 161))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.name.setFont(font)
        self.name.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(201, 204, 255);\n"
"border-radius: 15px;\n"
"")
        self.name.setObjectName("name")
        self.background.raise_()
        self.first_game.raise_()
        self.second_game.raise_()
        self.third_game.raise_()
        self.exit.raise_()
        self.name.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Connectig buttons to functions
        self.exit.clicked.connect(self.exec_app)
        self.first_game.clicked.connect(self.open_first_game)
        self.second_game.clicked.connect(self.open_second_game)
        self.third_game.clicked.connect(self.open_third_game)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.first_game.setText(_translate("MainWindow", "Game 1"))
        self.second_game.setText(_translate("MainWindow", "Game 2"))
        self.third_game.setText(_translate("MainWindow", "Game 3"))
        self.exit.setText(_translate("MainWindow", "Exit"))
        self.name.setText(_translate("MainWindow", "       Gametime"))
    
    # functions for buttons
    
    def exec_app(self, MainWindow): # - exit the game
        if __name__ == "__main__":            
            app = QtWidgets.QApplication(sys.argv)
            MainWindow = QtWidgets.QMainWindow()
            ui = Interface()
            ui.setupUi(MainWindow)
            MainWindow.show()
    
    def open_first_game(self): # - open irst game        
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()

    def open_second_game(self): # - open second game
        ...

    def open_third_game(self): # - open third game
        ...

#exit
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Interface()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
