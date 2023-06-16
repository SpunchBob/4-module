from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys

class MainWindow(QMainWindow):
   def __init__(self):
      super(MainWindow, self).__init__()
      uic.loadUi('C:\Users\User\Desktop\Programming\мои приколы\ui.ui', self)

app = QApplication([])
application = MainWindow()
application.show()

sys.exit(app.exec())



