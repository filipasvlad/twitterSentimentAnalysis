from PyQt5.QtWidgets import *
from gui.main_window import MainGUI
import sys
from model.train import run

def runGUI():
    app = QApplication(sys.argv)
    window = MainGUI()
    window.show()
    app.exec()

runGUI()
#run()
