from PyQt5 import QtCore, QtGui, QtWidgets
from stream_key import (LinearFeedbackShiftRegister,
                        GeffeGenerator,
                        StopAndGoGenerator,
                        ShrinkingGenerator)
from GUI_ReadOnly import Ui_MainWindow
import sys
import traceback


class GUIApplication(Ui_MainWindow):
    def __init__(self, mainWindow):
        Ui_MainWindow.__init__(self)
        self.setupUi(mainWindow)

        self._geffe = None
        self._stopandgo = None
        self._shrinking = None

        self._init_triggers()

    def _init_triggers(self):
        self.pushButton_new_Geffe.clicked.connect(self.new_geffe)
        self.pushButton_geffe_next.clicked.connect(self.next_geffe)
        self.pushButton_geffe_next_xtimes.clicked.connect(
            lambda: self.next_geffe_xtimes(15))

        self.pushButton_new_stopandgo.clicked.connect(self.new_stopandgo)
        self.pushButton_stopandgo_next.clicked.connect(self.next_stopandgo)
        self.pushButton_stopandgo_next_xtimes.clicked.connect(
            lambda: self.next_stopandgo_xtimes(15))

        self.pushButton_new_shrinking.clicked.connect(self.new_shrinking)
        self.pushButton_shrinking_next.clicked.connect(self.next_shrinking)
        self.pushButton_shrinking_next_xtimes.clicked.connect(
            lambda: self.next_shrinking_xtimes(15))

    def new_geffe(self):
        size = int(self.spinBox_geffe_size.value())

        init_state = int(self.lineEdit_geffe_init_state.displayText())
        config = int(self.lineEdit_geffe_config.displayText())

        self._geffe = GeffeGenerator(
            bit_size=size, init_state=init_state, config=config)
        self.show_geffe()
        self.text_geffe_stream.setText("")

    def next_geffe(self):
        try:
            self._geffe.next()
            self.show_geffe()
        except AttributeError:
            self.show_geffe(empty=True)

    def next_geffe_xtimes(self, n):
        try:
            for _ in range(n):
                # print(_)
                self._geffe.next()
                self.show_geffe()
        except AttributeError:
            self.show_geffe(empty=True)

    def show_geffe(self, empty=False):
        if empty:
            self.text_geffe_stream.setText("Generator is not defined")
            self.text_geffe_state.setText("Generator is not defined")

        else:
            text = self.text_geffe_stream.toPlainText()
            text = str(self._geffe.last_bit) + text
            self.text_geffe_stream.setText(text)

            state_list = self._geffe.get_state()
            text = "\n".join(state_list)
            self.text_geffe_state.setText(text)

    def new_stopandgo(self):
        size = int(self.spinBox_stopandgo_size.value())

        init_state = int(self.lineEdit_stopandgo_init_state.displayText())
        config = int(self.lineEdit_stopandgo_config.displayText())

        self._stopandgo = StopAndGoGenerator(
            bit_size=size, init_state=init_state, config=config)
        self.show_stopandgo()
        self.text_stopandgo_stream.setText("")

    def next_stopandgo(self):
        try:
            self._stopandgo.next()
            self.show_stopandgo()
        except AttributeError:
            self.show_stopandgo(empty=True)

    def next_stopandgo_xtimes(self, n):
        try:
            for _ in range(n):
                # print(_)
                self._stopandgo.next()
                self.show_stopandgo()
        except AttributeError:
            self.show_stopandgo(empty=True)

    def show_stopandgo(self, empty=False):
        if empty:
            self.text_stopandgo_stream.setText("Generator is not defined")
            self.text_stopandgo_state.setText("Generator is not defined")

        else:
            text = self.text_stopandgo_stream.toPlainText()
            text = str(self._stopandgo.last_bit) + text
            self.text_stopandgo_stream.setText(text)

            state_list = self._stopandgo.get_state()
            text = "\n".join(state_list)
            self.text_stopandgo_state.setText(text)

    def new_shrinking(self):
        size = int(self.spinBox_shrinking_size.value())

        init_state = int(self.lineEdit_shrinking_init_state.displayText())
        config = int(self.lineEdit_shrinking_config.displayText())

        self._shrinking = ShrinkingGenerator(
            bit_size=size, init_state=init_state, config=config)
        self.show_shrinking()
        self.text_shrinking_stream.setText("")

    def next_shrinking(self):
        try:
            self._shrinking.next()
            self.show_shrinking()
        except AttributeError:
            self.show_shrinking(empty=True)

    def next_shrinking_xtimes(self, n):
        try:
            for _ in range(n):                
                self._shrinking.next()
                self.show_shrinking()
        except AttributeError:
            self.show_shrinking(empty=True)

    def show_shrinking(self, empty=False):
        if empty:
            self.text_shrinking_stream.setText("Generator is not defined")
            self.text_shrinking_state.setText("Generator is not defined")

        else:
            text = self.text_shrinking_stream.toPlainText()
            text = str(self._shrinking.last_bit) + text
            self.text_shrinking_stream.setText(text)

            state_list = self._shrinking.get_state()
            text = "\n".join(state_list)
            self.text_shrinking_state.setText(text)


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
