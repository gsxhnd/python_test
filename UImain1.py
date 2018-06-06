import sys
import UI.testUI
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mWindow = QMainWindow()
    ui = UI.testUI.Ui_MainWindow()
    ui.setupUi(mWindow)
    mWindow.show()
    sys.exit(app.exec())