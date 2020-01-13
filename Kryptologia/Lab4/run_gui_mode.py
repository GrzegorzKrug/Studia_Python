from PyQt5 import QtCore, QtGui, QtWidgets
from stream_key import (LinearFeedbackShiftRegister,
                        GeffeGenerator,
                        StopAndGoGenerator,
                        ShrinkingGenerator)
from GUI_ReadOnly import Ui_MainWindow
import sys


class GUIApplication(Ui_MainWindow):
    def __init__(self, mainWindow):
        Ui_MainWindow.__init__(self)
        self.setupUi(mainWindow)

# def runGUI():
#     ui = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     app = GUIApplication(MainWindow)

#     error_dialog = QtWidgets.QErrorMessage()
#     MainWindow.show()
#     sys.exit(ui.exec_())


if QtCore.QT_VERSION >= 0x50501:  # Showing traceback from crashes
    def excepthook(type_, value, traceback_):
        traceback.print_exception(type_, value, traceback_)
        QtCore.qFatal('')
sys.excepthook = excepthook

def runGUI():
    ui = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    app = GUIApplication(MainWindow)
    
    error_dialog = QtWidgets.QErrorMessage()
    MainWindow.show()
    sys.exit(ui.exec_())
    

if __name__ == "__main__":
    print("Running gui.")
    runGUI()
