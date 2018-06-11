import sys
import UI.testUI
import UI.settingDialog
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    uiMain = UI.testUI.Ui_MainWindow()
    mWindow = QMainWindow()
    uiMain.setupUi(mWindow)

    uiSetting = UI.settingDialog.Ui_settingDialog()
    settingDialog = QDialog()
    uiSetting.setupUi(settingDialog)

    settingAction = uiMain.settingAction.triggered['bool'].connect(settingDialog.show)

    mWindow.show()
    sys.exit(app.exec_())
