from PyQt5 import QtCore, QtGui, QtWidgets
import pygame
import sys
import keyboard


preset_name = "piano"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MiniSynth")
        MainWindow.resize(634, 637)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.c_note = QtWidgets.QPushButton(self.centralwidget)
        self.c_note.setGeometry(QtCore.QRect(70, 190, 61, 351))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(24)
        self.c_note.setFont(font)
        self.c_note.setStyleSheet("QPushButton{\n"
"    background-color:rgb(212, 212, 212);\n"
"    border-radius: 20px;\n"
"} \n"
"QPushButton::pressed {\n"
"    background-color : rgb(200, 200, 200);\n"
"    border-radius: 20px;\n"
"}")
        self.c_note.setText("")
        self.c_note.setObjectName("c")
        self.d_note = QtWidgets.QPushButton(self.centralwidget)
        self.d_note.setGeometry(QtCore.QRect(140, 190, 61, 351))
        self.d_note.setStyleSheet("QPushButton{\n"
"    background-color:rgb(212, 212, 212);\n"
"    border-radius: 20px;\n"
"} \n"
"QPushButton::pressed {\n"
"    background-color : rgb(200, 200, 200);\n"
"    border-radius: 20px;\n"
"}")
        self.d_note.setText("")
        self.d_note.setObjectName("d")
        self.e_note = QtWidgets.QPushButton(self.centralwidget)
        self.e_note.setGeometry(QtCore.QRect(210, 190, 61, 351))
        self.e_note.setStyleSheet("QPushButton{\n"
"    background-color:rgb(212, 212, 212);\n"
"    border-radius: 20px;\n"
"} \n"
"QPushButton::pressed {\n"
"    background-color : rgb(200, 200, 200);\n"
"    border-radius: 20px;\n"
"}")
        self.e_note.setText("")
        self.e_note.setObjectName("e")
        self.f_note = QtWidgets.QPushButton(self.centralwidget)
        self.f_note.setGeometry(QtCore.QRect(280, 190, 61, 351))
        self.f_note.setStyleSheet("QPushButton{\n"
"    background-color:rgb(212, 212, 212);\n"
"    border-radius: 20px;\n"
"} \n"
"QPushButton::pressed {\n"
"    background-color : rgb(200, 200, 200);\n"
"    border-radius: 20px;\n"
"}")
        self.f_note.setText("")
        self.f_note.setObjectName("f")
        self.g_note = QtWidgets.QPushButton(self.centralwidget)
        self.g_note.setGeometry(QtCore.QRect(350, 190, 61, 351))
        self.g_note.setStyleSheet("QPushButton{\n"
"    background-color:rgb(212, 212, 212);\n"
"    border-radius: 20px;\n"
"} \n"
"QPushButton::pressed {\n"
"    background-color : rgb(200, 200, 200);\n"
"    border-radius: 20px;\n"
"}")
        self.g_note.setText("")
        self.g_note.setObjectName("g")
        self.a_note = QtWidgets.QPushButton(self.centralwidget)
        self.a_note.setGeometry(QtCore.QRect(420, 190, 61, 351))
        self.a_note.setStyleSheet("QPushButton{\n"
"    background-color:rgb(212, 212, 212);\n"
"    border-radius: 20px;\n"
"} \n"
"QPushButton::pressed {\n"
"    background-color : rgb(200, 200, 200);\n"
"    border-radius: 20px;\n"
"}")
        self.a_note.setText("")
        self.a_note.setObjectName("a")
        self.b_note = QtWidgets.QPushButton(self.centralwidget)
        self.b_note.setGeometry(QtCore.QRect(490, 190, 61, 351))
        self.b_note.setStyleSheet("QPushButton{\n"
"    background-color:rgb(212, 212, 212);\n"
"    border-radius: 20px;\n"
"} \n"
"QPushButton::pressed {\n"
"    background-color : rgb(200, 200, 200);\n"
"    border-radius: 20px;\n"
"}")
        self.b_note.setText("")
        self.b_note.setObjectName("b")
        self.background_label = QtWidgets.QLabel(self.centralwidget)
        self.background_label.setGeometry(QtCore.QRect(50, 40, 521, 531))
        self.background_label.setStyleSheet("background-color: rgb(102, 102, 102);\n"
"border-radius: 30px")
        self.background_label.setText("")
        self.background_label.setObjectName("background_label")
        self.cd_note = QtWidgets.QPushButton(self.centralwidget)
        self.cd_note.setGeometry(QtCore.QRect(110, 190, 51, 211))
        self.cd_note.setStyleSheet("QPushButton{\n"
"    background-color:rgb(45, 45, 45);\n"
"    border-radius: 20px;\n"
"} \n"
"QPushButton::pressed {\n"
"    background-color : rgb(200, 200, 200);\n"
"    border-radius: 20px;\n"
"}")
        self.cd_note.setText("")
        self.cd_note.setObjectName("cd")
        self.dd_note = QtWidgets.QPushButton(self.centralwidget)
        self.dd_note.setGeometry(QtCore.QRect(180, 190, 51, 211))
        self.dd_note.setStyleSheet("QPushButton{\n"
"    background-color:rgb(45, 45, 45);\n"
"    border-radius: 20px;\n"
"} \n"
"QPushButton::pressed {\n"
"    background-color : rgb(200, 200, 200);\n"
"    border-radius: 20px;\n"
"}")
        self.dd_note.setText("")
        self.dd_note.setObjectName("dd")
        self.fd_note = QtWidgets.QPushButton(self.centralwidget)
        self.fd_note.setGeometry(QtCore.QRect(320, 190, 51, 211))
        self.fd_note.setStyleSheet("QPushButton{\n"
"    background-color:rgb(45, 45, 45);\n"
"    border-radius: 20px;\n"
"} \n"
"QPushButton::pressed {\n"
"    background-color : rgb(200, 200, 200);\n"
"    border-radius: 20px;\n"
"}")
        self.fd_note.setText("")
        self.fd_note.setObjectName("fd")
        self.gd_note = QtWidgets.QPushButton(self.centralwidget)
        self.gd_note.setGeometry(QtCore.QRect(390, 190, 51, 211))
        self.gd_note.setStyleSheet("QPushButton{\n"
"    background-color:rgb(45, 45, 45);\n"
"    border-radius: 20px;\n"
"} \n"
"QPushButton::pressed {\n"
"    background-color : rgb(200, 200, 200);\n"
"    border-radius: 20px;\n"
"}")
        self.gd_note.setText("")
        self.gd_note.setObjectName("gd")
        self.ad_note = QtWidgets.QPushButton(self.centralwidget)
        self.ad_note.setGeometry(QtCore.QRect(460, 190, 51, 211))
        self.ad_note.setStyleSheet("QPushButton{\n"
"    background-color:rgb(45, 45, 45);\n"
"    border-radius: 20px;\n"
"} \n"
"QPushButton::pressed {\n"
"    background-color : rgb(200, 200, 200);\n"
"    border-radius: 20px;\n"
"}")
        self.ad_note.setText("")
        self.ad_note.setObjectName("ad")
        self.q_key = QtWidgets.QLabel(self.centralwidget)
        self.q_key.setGeometry(QtCore.QRect(90, 460, 21, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(22)
        self.q_key.setFont(font)
        self.q_key.setObjectName("q_key")
        self.w_key = QtWidgets.QLabel(self.centralwidget)
        self.w_key.setGeometry(QtCore.QRect(150, 460, 41, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(22)
        self.w_key.setFont(font)
        self.w_key.setObjectName("w_key")
        self.e_key = QtWidgets.QLabel(self.centralwidget)
        self.e_key.setGeometry(QtCore.QRect(230, 460, 21, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(22)
        self.e_key.setFont(font)
        self.e_key.setObjectName("e_key")
        self.y_key = QtWidgets.QLabel(self.centralwidget)
        self.y_key.setGeometry(QtCore.QRect(440, 460, 21, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(22)
        self.y_key.setFont(font)
        self.y_key.setObjectName("y_key")
        self.t_key = QtWidgets.QLabel(self.centralwidget)
        self.t_key.setGeometry(QtCore.QRect(370, 460, 21, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(22)
        self.t_key.setFont(font)
        self.t_key.setObjectName("t_key")
        self.r_key = QtWidgets.QLabel(self.centralwidget)
        self.r_key.setGeometry(QtCore.QRect(300, 460, 21, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(22)
        self.r_key.setFont(font)
        self.r_key.setObjectName("r_key")
        self.u_key = QtWidgets.QLabel(self.centralwidget)
        self.u_key.setGeometry(QtCore.QRect(510, 460, 21, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(22)
        self.u_key.setFont(font)
        self.u_key.setObjectName("u_key")
        self.key_2 = QtWidgets.QLabel(self.centralwidget)
        self.key_2.setGeometry(QtCore.QRect(112, 320, 35, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(18)
        self.key_2.setFont(font)
        self.key_2.setStyleSheet("color: rgb(243, 243, 243);")
        self.key_2.setObjectName("key_2")
        self.key_3 = QtWidgets.QLabel(self.centralwidget)
        self.key_3.setGeometry(QtCore.QRect(182, 320, 35, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(18)
        self.key_3.setFont(font)
        self.key_3.setStyleSheet("color: rgb(243, 243, 243);")
        self.key_3.setObjectName("key_3")
        self.key_5 = QtWidgets.QLabel(self.centralwidget)
        self.key_5.setGeometry(QtCore.QRect(325, 320, 35, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(18)
        self.key_5.setFont(font)
        self.key_5.setStyleSheet("color: rgb(243, 243, 243);")
        self.key_5.setObjectName("key_5")
        self.key_6 = QtWidgets.QLabel(self.centralwidget)
        self.key_6.setGeometry(QtCore.QRect(394, 320, 35, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(18)
        self.key_6.setFont(font)
        self.key_6.setStyleSheet("color: rgb(243, 243, 243);")
        self.key_6.setObjectName("key_6")
        self.key_7 = QtWidgets.QLabel(self.centralwidget)
        self.key_7.setGeometry(QtCore.QRect(464, 320, 35, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(18)
        self.key_7.setFont(font)
        self.key_7.setStyleSheet("color: rgb(243, 243, 243);")
        self.key_7.setObjectName("key_7")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 60, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color:rgb(212, 212, 212);\n"
"    border-radius: 20px;\n"
"} \n"
"QPushButton::pressed {\n"
"    background-color : rgb(200, 200, 200);\n"
"    border-radius: 20px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 60, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(22)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    background-color:rgb(212, 212, 212);\n"
"    border-radius: 20px;\n"
"} \n"
"QPushButton::pressed {\n"
"    background-color : rgb(200, 200, 200);\n"
"    border-radius: 20px;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(370, 60, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(22)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    background-color:rgb(212, 212, 212);\n"
"    border-radius: 20px;\n"
"} \n"
"QPushButton::pressed {\n"
"    background-color : rgb(200, 200, 200);\n"
"    border-radius: 20px;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(70, 110, 311, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(36)
        self.logo.setFont(font)
        self.logo.setStyleSheet("color: rgb(255, 255, 255)")
        self.logo.setObjectName("logo")
        self.background_label.raise_()
        self.c_note.raise_()
        self.d_note.raise_()
        self.e_note.raise_()
        self.f_note.raise_()
        self.g_note.raise_()
        self.a_note.raise_()
        self.b_note.raise_()
        self.cd_note.raise_()
        self.dd_note.raise_()
        self.fd_note.raise_()
        self.gd_note.raise_()
        self.ad_note.raise_()
        self.q_key.raise_()
        self.w_key.raise_()
        self.e_key.raise_()
        self.y_key.raise_()
        self.t_key.raise_()
        self.r_key.raise_()
        self.u_key.raise_()
        self.key_2.raise_()
        self.key_3.raise_()
        self.key_5.raise_()
        self.key_6.raise_()
        self.key_7.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.logo.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.active_keyboards()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MiniSynth 2", "MiniSynth 2"))
        self.q_key.setText(_translate("MainWindow", "C"))
        self.w_key.setText(_translate("MainWindow", " D"))
        self.e_key.setText(_translate("MainWindow", "E"))
        self.y_key.setText(_translate("MainWindow", "A"))
        self.t_key.setText(_translate("MainWindow", "G"))
        self.r_key.setText(_translate("MainWindow", "F"))
        self.u_key.setText(_translate("MainWindow", "B"))
        self.key_2.setText(_translate("MainWindow", " Cd"))
        self.key_3.setText(_translate("MainWindow", " Dd"))
        self.key_5.setText(_translate("MainWindow", " Fd"))
        self.key_6.setText(_translate("MainWindow", " Gd"))
        self.key_7.setText(_translate("MainWindow", " Ad"))
        self.pushButton.setText(_translate("MainWindow", "Exit"))
        self.pushButton_2.setText(_translate("MainWindow", "Preset"))
        self.pushButton_3.setText(_translate("MainWindow", "Help"))
        self.logo.setText(_translate("MainWindow", "MiniSynth 2"))

    def main_keyboard(self):
        self.c_note.clicked.connect(lambda: self.play_note(self.c_note.objectName()))
        self.d_note.clicked.connect(lambda: self.play_note(self.d_note.objectName()))
        self.e_note.clicked.connect(lambda: self.play_note(self.e_note.objectName()))
        self.f_note.clicked.connect(lambda: self.play_note(self.f_note.objectName()))
        self.g_note.clicked.connect(lambda: self.play_note(self.g_note.objectName()))
        self.a_note.clicked.connect(lambda: self.play_note(self.a_note.objectName()))
        self.b_note.clicked.connect(lambda: self.play_note(self.b_note.objectName()))
        self.cd_note.clicked.connect(lambda: self.play_note(self.cd_note.objectName()))
        self.dd_note.clicked.connect(lambda: self.play_note(self.dd_note.objectName()))
        self.fd_note.clicked.connect(lambda: self.play_note(self.fd_note.objectName()))
        self.gd_note.clicked.connect(lambda: self.play_note(self.gd_note.objectName()))
        self.ad_note.clicked.connect(lambda: self.play_note(self.ad_note.objectName()))

    def option_buttons(self):
        self.pushButton.clicked.connect(self.exit)
        self.pushButton_2.clicked.connect(self.pressets)
        self.pushButton_3.clicked.connect(self.help_window)

    def play_note(self, object_name):
        global preset_name
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(f"sounds\{preset_name}\{object_name}.mp3")
        pygame.mixer.music.play()

    def pressets(self):
        self.pressets_window = QtWidgets.QMainWindow()
        self.pressets_window.resize(634, 637)
        self.pressets_window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.pressets_window.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.background_label = QtWidgets.QLabel(self.pressets_window)
        self.background_label.setGeometry(QtCore.QRect(156, 150, 300, 300))
        self.background_label.setStyleSheet("background-color: rgb(158, 158, 158);\n"
        "border-radius: 30px")
        self.background_label.setText("")
        self.background_label.setObjectName("background_label")
        self.help_label = QtWidgets.QLabel(self.pressets_window)
        self.help_label.setGeometry(QtCore.QRect(220, 380, 250, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(20)
        self.help_label.setFont(font)
        self.help_label.setText("Choose Presset")


        self.preset1 = QtWidgets.QPushButton(self.pressets_window)
        self.preset1.setGeometry(QtCore.QRect(182, 180, 250, 40))
        self.preset1.setStyleSheet("QPushButton{\n"
        "    background-color:rgb(212, 212, 212);\n"
        "    border-radius: 20px;\n"
        "} \n"
        "QPushButton::pressed {\n"
        "    background-color : rgb(200, 200, 200);\n"
        "    border-radius: 20px;\n"
        "}")
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(22)
        self.preset1.setFont(font)
        self.preset1.setText("Piano")
        self.preset1.setObjectName("piano")

        self.preset2 = QtWidgets.QPushButton(self.pressets_window)
        self.preset2.setGeometry(QtCore.QRect(182, 230, 250, 40))
        self.preset2.setStyleSheet("QPushButton{\n"
        "    background-color:rgb(212, 212, 212);\n"
        "    border-radius: 20px;\n"
        "} \n"
        "QPushButton::pressed {\n"
        "    background-color : rgb(200, 200, 200);\n"
        "    border-radius: 20px;\n"
        "}")
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(22)
        self.preset2.setFont(font)
        self.preset2.setText("Bass")
        self.preset2.setObjectName("bass")

        self.preset3 = QtWidgets.QPushButton(self.pressets_window)
        self.preset3.setGeometry(QtCore.QRect(182, 280, 250, 40))
        self.preset3.setStyleSheet("QPushButton{\n"
        "    background-color:rgb(212, 212, 212);\n"
        "    border-radius: 20px;\n"
        "} \n"
        "QPushButton::pressed {\n"
        "    background-color : rgb(200, 200, 200);\n"
        "    border-radius: 20px;\n"
        "}")
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(22)
        self.preset3.setFont(font)
        self.preset3.setText("Synth 1")
        self.preset3.setObjectName("synth1")

        self.preset4 = QtWidgets.QPushButton(self.pressets_window)
        self.preset4.setGeometry(QtCore.QRect(182, 330, 250, 40))
        self.preset4.setStyleSheet("QPushButton{\n"
        "    background-color:rgb(212, 212, 212);\n"
        "    border-radius: 20px;\n"
        "} \n"
        "QPushButton::pressed {\n"
        "    background-color : rgb(200, 200, 200);\n"
        "    border-radius: 20px;\n"
        "}")
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(22)
        self.preset4.setFont(font)
        self.preset4.setText("Synth 2")
        self.preset4.setObjectName("synth2")

        self.presset_buttons()

        self.pressets_window.show()

    def help_window(self):
        self.window = QtWidgets.QMainWindow()
        self.window.resize(634, 637)
        self.window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.window.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.background_label = QtWidgets.QLabel(self.window)
        self.background_label.setGeometry(QtCore.QRect(156, 150, 300, 200))
        self.background_label.setStyleSheet("background-color: rgb(158, 158, 158);\n"
        "border-radius: 20px")
        self.info_label = QtWidgets.QLabel(self.window)
        self.info_label.setGeometry(QtCore.QRect(165, 120, 700, 200))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(11)
        self.info_label.setFont(font)
        self.info_label.setText("1.Play MiniSynth by pressing buttosn\n2.Choose instrument in pressets window\n3.Exit MiniSynth by pressing exit button\nСпасибо за то, что играйте на MiniSynth2!\n@Героиновый_Наркоман")
        self.exit_button = QtWidgets.QPushButton(self.window)
        self.exit_button.setGeometry(QtCore.QRect(182, 290, 250, 40))
        self.exit_button.setStyleSheet("QPushButton{\n"
        "    background-color:rgb(212, 212, 212);\n"
        "    border-radius: 20px;\n"
        "} \n"
        "QPushButton::pressed {\n"
        "    background-color : rgb(200, 200, 200);\n"
        "    border-radius: 20px;\n"
        "}")
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(22)
        self.exit_button.setFont(font)
        self.exit_button.setText("Exit")
        self.help_button()
        self.window.show()

    def presset_buttons(self):
        self.preset1.clicked.connect(lambda: self.presset_choosing(self.preset1.objectName()))
        self.preset2.clicked.connect(lambda: self.presset_choosing(self.preset2.objectName()))
        self.preset3.clicked.connect(lambda: self.presset_choosing(self.preset3.objectName()))
        self.preset4.clicked.connect(lambda: self.presset_choosing(self.preset4.objectName()))

    def presset_choosing(self, objectName):
        global preset_name
        preset_name = objectName
        self.pressets_window.destroy()
        print(preset_name)

    def help_button(self):
        self.exit_button.clicked.connect(self.exit_help)

    def exit_help(self):
        self.window.destroy()

    def active_keyboards(self):
        self.main_keyboard()
        self.option_buttons()

    def exit(self):
        sys.exit()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())