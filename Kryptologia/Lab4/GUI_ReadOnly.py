# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_QT.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(946, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setObjectName("gridLayout")
        self.MainGrid = QtWidgets.QGridLayout()
        self.MainGrid.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.MainGrid.setContentsMargins(0, -1, -1, -1)
        self.MainGrid.setObjectName("MainGrid")
        self.grid_Generators = QtWidgets.QGridLayout()
        self.grid_Generators.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.grid_Generators.setObjectName("grid_Generators")
        self.grid_config_stopandgo = QtWidgets.QGridLayout()
        self.grid_config_stopandgo.setObjectName("grid_config_stopandgo")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.grid_config_stopandgo.addItem(spacerItem, 3, 0, 1, 1)
        self.lineEdit_stopandgo_init_state = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_stopandgo_init_state.sizePolicy().hasHeightForWidth())
        self.lineEdit_stopandgo_init_state.setSizePolicy(sizePolicy)
        self.lineEdit_stopandgo_init_state.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit_stopandgo_init_state.setObjectName("lineEdit_stopandgo_init_state")
        self.grid_config_stopandgo.addWidget(self.lineEdit_stopandgo_init_state, 5, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.grid_config_stopandgo.addItem(spacerItem1, 0, 0, 1, 1)
        self.spinBox_stopandgo_size = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_stopandgo_size.sizePolicy().hasHeightForWidth())
        self.spinBox_stopandgo_size.setSizePolicy(sizePolicy)
        self.spinBox_stopandgo_size.setFrame(True)
        self.spinBox_stopandgo_size.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.spinBox_stopandgo_size.setMinimum(1)
        self.spinBox_stopandgo_size.setProperty("value", 16)
        self.spinBox_stopandgo_size.setObjectName("spinBox_stopandgo_size")
        self.grid_config_stopandgo.addWidget(self.spinBox_stopandgo_size, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_9.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_9.setObjectName("label_9")
        self.grid_config_stopandgo.addWidget(self.label_9, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.grid_config_stopandgo.addItem(spacerItem2, 6, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_7.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_7.setObjectName("label_7")
        self.grid_config_stopandgo.addWidget(self.label_7, 7, 0, 1, 1)
        self.lineEdit_stopandgo_config = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_stopandgo_config.sizePolicy().hasHeightForWidth())
        self.lineEdit_stopandgo_config.setSizePolicy(sizePolicy)
        self.lineEdit_stopandgo_config.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit_stopandgo_config.setObjectName("lineEdit_stopandgo_config")
        self.grid_config_stopandgo.addWidget(self.lineEdit_stopandgo_config, 8, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_8.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_8.setObjectName("label_8")
        self.grid_config_stopandgo.addWidget(self.label_8, 4, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.grid_config_stopandgo.addItem(spacerItem3, 9, 0, 1, 1)
        self.grid_Generators.addLayout(self.grid_config_stopandgo, 1, 0, 1, 1)
        self.grid_config_geffe = QtWidgets.QGridLayout()
        self.grid_config_geffe.setObjectName("grid_config_geffe")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_2.setObjectName("label_2")
        self.grid_config_geffe.addWidget(self.label_2, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label.setObjectName("label")
        self.grid_config_geffe.addWidget(self.label, 2, 0, 1, 1)
        self.lineEdit_geffe_config = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_geffe_config.sizePolicy().hasHeightForWidth())
        self.lineEdit_geffe_config.setSizePolicy(sizePolicy)
        self.lineEdit_geffe_config.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit_geffe_config.setObjectName("lineEdit_geffe_config")
        self.grid_config_geffe.addWidget(self.lineEdit_geffe_config, 9, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.grid_config_geffe.addItem(spacerItem4, 10, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.grid_config_geffe.addItem(spacerItem5, 7, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_3.setObjectName("label_3")
        self.grid_config_geffe.addWidget(self.label_3, 8, 0, 1, 1)
        self.spinBox_geffe_size = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_geffe_size.sizePolicy().hasHeightForWidth())
        self.spinBox_geffe_size.setSizePolicy(sizePolicy)
        self.spinBox_geffe_size.setFrame(True)
        self.spinBox_geffe_size.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.spinBox_geffe_size.setMinimum(1)
        self.spinBox_geffe_size.setProperty("value", 16)
        self.spinBox_geffe_size.setObjectName("spinBox_geffe_size")
        self.grid_config_geffe.addWidget(self.spinBox_geffe_size, 3, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.grid_config_geffe.addItem(spacerItem6, 4, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.grid_config_geffe.addItem(spacerItem7, 0, 0, 1, 1)
        self.lineEdit_geffe_init_state = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_geffe_init_state.sizePolicy().hasHeightForWidth())
        self.lineEdit_geffe_init_state.setSizePolicy(sizePolicy)
        self.lineEdit_geffe_init_state.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit_geffe_init_state.setObjectName("lineEdit_geffe_init_state")
        self.grid_config_geffe.addWidget(self.lineEdit_geffe_init_state, 6, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.grid_config_geffe.addItem(spacerItem8, 1, 0, 1, 1)
        self.grid_config_geffe.setRowStretch(0, 1)
        self.grid_Generators.addLayout(self.grid_config_geffe, 0, 0, 1, 1)
        self.verticalLayout_geffe = QtWidgets.QVBoxLayout()
        self.verticalLayout_geffe.setObjectName("verticalLayout_geffe")
        self.pushButton_new_Geffe = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_new_Geffe.sizePolicy().hasHeightForWidth())
        self.pushButton_new_Geffe.setSizePolicy(sizePolicy)
        self.pushButton_new_Geffe.setStyleSheet("background-color: rgb(138, 226, 52);")
        self.pushButton_new_Geffe.setObjectName("pushButton_new_Geffe")
        self.verticalLayout_geffe.addWidget(self.pushButton_new_Geffe)
        self.pushButton_geffe_next = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_geffe_next.setObjectName("pushButton_geffe_next")
        self.verticalLayout_geffe.addWidget(self.pushButton_geffe_next)
        self.pushButton_geffe_next_15times = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_geffe_next_15times.setObjectName("pushButton_geffe_next_15times")
        self.verticalLayout_geffe.addWidget(self.pushButton_geffe_next_15times)
        self.pushButton_geffe_fill = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_geffe_fill.setObjectName("pushButton_geffe_fill")
        self.verticalLayout_geffe.addWidget(self.pushButton_geffe_fill)
        self.grid_Generators.addLayout(self.verticalLayout_geffe, 0, 1, 1, 1)
        self.verticalLayout_stopandgo = QtWidgets.QVBoxLayout()
        self.verticalLayout_stopandgo.setObjectName("verticalLayout_stopandgo")
        self.pushButton_new_stopandgo = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_new_stopandgo.setStyleSheet("background-color: rgb(138, 226, 52);")
        self.pushButton_new_stopandgo.setObjectName("pushButton_new_stopandgo")
        self.verticalLayout_stopandgo.addWidget(self.pushButton_new_stopandgo)
        self.pushButton_stopandgo_next = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_stopandgo_next.setObjectName("pushButton_stopandgo_next")
        self.verticalLayout_stopandgo.addWidget(self.pushButton_stopandgo_next)
        self.pushButton_stopandgo_next_15times = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_stopandgo_next_15times.setObjectName("pushButton_stopandgo_next_15times")
        self.verticalLayout_stopandgo.addWidget(self.pushButton_stopandgo_next_15times)
        self.pushButton_stopandgo_fill = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_stopandgo_fill.setObjectName("pushButton_stopandgo_fill")
        self.verticalLayout_stopandgo.addWidget(self.pushButton_stopandgo_fill)
        self.grid_Generators.addLayout(self.verticalLayout_stopandgo, 1, 1, 1, 1)
        self.verticalLayout_shrinking = QtWidgets.QVBoxLayout()
        self.verticalLayout_shrinking.setObjectName("verticalLayout_shrinking")
        self.pushButton_new_shrinking = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_new_shrinking.setStyleSheet("background-color: rgb(138, 226, 52);")
        self.pushButton_new_shrinking.setObjectName("pushButton_new_shrinking")
        self.verticalLayout_shrinking.addWidget(self.pushButton_new_shrinking)
        self.pushButton_shrinking_next = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_shrinking_next.setObjectName("pushButton_shrinking_next")
        self.verticalLayout_shrinking.addWidget(self.pushButton_shrinking_next)
        self.pushButton_shrinking_next_15times = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_shrinking_next_15times.setObjectName("pushButton_shrinking_next_15times")
        self.verticalLayout_shrinking.addWidget(self.pushButton_shrinking_next_15times)
        self.pushButton_shrinking_fill = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_shrinking_fill.setObjectName("pushButton_shrinking_fill")
        self.verticalLayout_shrinking.addWidget(self.pushButton_shrinking_fill)
        self.grid_Generators.addLayout(self.verticalLayout_shrinking, 2, 1, 1, 1)
        self.grid_config_shrinking = QtWidgets.QGridLayout()
        self.grid_config_shrinking.setObjectName("grid_config_shrinking")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_4.setObjectName("label_4")
        self.grid_config_shrinking.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_5.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_5.setObjectName("label_5")
        self.grid_config_shrinking.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_6.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_6.setObjectName("label_6")
        self.grid_config_shrinking.addWidget(self.label_6, 7, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.grid_config_shrinking.addItem(spacerItem9, 6, 0, 1, 1)
        self.lineEdit_shrinking_init_state = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_shrinking_init_state.sizePolicy().hasHeightForWidth())
        self.lineEdit_shrinking_init_state.setSizePolicy(sizePolicy)
        self.lineEdit_shrinking_init_state.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_shrinking_init_state.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit_shrinking_init_state.setObjectName("lineEdit_shrinking_init_state")
        self.grid_config_shrinking.addWidget(self.lineEdit_shrinking_init_state, 5, 0, 1, 1)
        self.spinBox_shrinking_size = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_shrinking_size.sizePolicy().hasHeightForWidth())
        self.spinBox_shrinking_size.setSizePolicy(sizePolicy)
        self.spinBox_shrinking_size.setFrame(True)
        self.spinBox_shrinking_size.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.spinBox_shrinking_size.setMinimum(1)
        self.spinBox_shrinking_size.setProperty("value", 16)
        self.spinBox_shrinking_size.setObjectName("spinBox_shrinking_size")
        self.grid_config_shrinking.addWidget(self.spinBox_shrinking_size, 2, 0, 1, 1)
        self.lineEdit_shrinking_config = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_shrinking_config.sizePolicy().hasHeightForWidth())
        self.lineEdit_shrinking_config.setSizePolicy(sizePolicy)
        self.lineEdit_shrinking_config.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit_shrinking_config.setObjectName("lineEdit_shrinking_config")
        self.grid_config_shrinking.addWidget(self.lineEdit_shrinking_config, 8, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.grid_config_shrinking.addItem(spacerItem10, 0, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.grid_config_shrinking.addItem(spacerItem11, 3, 0, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.grid_config_shrinking.addItem(spacerItem12, 9, 0, 1, 1)
        self.grid_Generators.addLayout(self.grid_config_shrinking, 2, 0, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem13)
        self.pushButton_shrinking_test_monobit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_shrinking_test_monobit.setObjectName("pushButton_shrinking_test_monobit")
        self.verticalLayout_6.addWidget(self.pushButton_shrinking_test_monobit)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_6.addWidget(self.pushButton_5)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_6.addWidget(self.pushButton_3)
        self.grid_Generators.addLayout(self.verticalLayout_6, 2, 3, 1, 1)
        self.verticalLayout_out_stopandgo = QtWidgets.QVBoxLayout()
        self.verticalLayout_out_stopandgo.setObjectName("verticalLayout_out_stopandgo")
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_out_stopandgo.addItem(spacerItem14)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_out_stopandgo.addWidget(self.label_12)
        self.text_stopandgo_state = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_stopandgo_state.sizePolicy().hasHeightForWidth())
        self.text_stopandgo_state.setSizePolicy(sizePolicy)
        self.text_stopandgo_state.setObjectName("text_stopandgo_state")
        self.verticalLayout_out_stopandgo.addWidget(self.text_stopandgo_state)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_out_stopandgo.addWidget(self.label_13)
        self.text_stopandgo_stream = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_stopandgo_stream.sizePolicy().hasHeightForWidth())
        self.text_stopandgo_stream.setSizePolicy(sizePolicy)
        self.text_stopandgo_stream.setObjectName("text_stopandgo_stream")
        self.verticalLayout_out_stopandgo.addWidget(self.text_stopandgo_stream)
        self.grid_Generators.addLayout(self.verticalLayout_out_stopandgo, 1, 2, 1, 1)
        self.verticalLayout_out_geffe = QtWidgets.QVBoxLayout()
        self.verticalLayout_out_geffe.setObjectName("verticalLayout_out_geffe")
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_out_geffe.addItem(spacerItem15)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_out_geffe.addWidget(self.label_10)
        self.text_geffe_state = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_geffe_state.sizePolicy().hasHeightForWidth())
        self.text_geffe_state.setSizePolicy(sizePolicy)
        self.text_geffe_state.setObjectName("text_geffe_state")
        self.verticalLayout_out_geffe.addWidget(self.text_geffe_state)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_out_geffe.addWidget(self.label_11)
        self.text_geffe_stream = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_geffe_stream.sizePolicy().hasHeightForWidth())
        self.text_geffe_stream.setSizePolicy(sizePolicy)
        self.text_geffe_stream.setObjectName("text_geffe_stream")
        self.verticalLayout_out_geffe.addWidget(self.text_geffe_stream)
        self.verticalLayout_out_geffe.setStretch(1, 1)
        self.verticalLayout_out_geffe.setStretch(2, 1)
        self.verticalLayout_out_geffe.setStretch(3, 1)
        self.verticalLayout_out_geffe.setStretch(4, 1)
        self.grid_Generators.addLayout(self.verticalLayout_out_geffe, 0, 2, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem16)
        self.pushButton_stopandgo_test_monobit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_stopandgo_test_monobit.setObjectName("pushButton_stopandgo_test_monobit")
        self.verticalLayout_5.addWidget(self.pushButton_stopandgo_test_monobit)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_5.addWidget(self.pushButton_2)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_5.addWidget(self.pushButton_8)
        self.grid_Generators.addLayout(self.verticalLayout_5, 1, 3, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem17)
        self.pushButton_gefe_test_monobit = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_gefe_test_monobit.sizePolicy().hasHeightForWidth())
        self.pushButton_gefe_test_monobit.setSizePolicy(sizePolicy)
        self.pushButton_gefe_test_monobit.setObjectName("pushButton_gefe_test_monobit")
        self.verticalLayout_4.addWidget(self.pushButton_gefe_test_monobit)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_4.addWidget(self.pushButton_7)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_4.addWidget(self.pushButton_6)
        self.grid_Generators.addLayout(self.verticalLayout_4, 0, 3, 1, 1)
        self.verticalLayout_out_shrikning = QtWidgets.QVBoxLayout()
        self.verticalLayout_out_shrikning.setObjectName("verticalLayout_out_shrikning")
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_out_shrikning.addItem(spacerItem18)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_out_shrikning.addWidget(self.label_14)
        self.text_shrinking_state = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_shrinking_state.sizePolicy().hasHeightForWidth())
        self.text_shrinking_state.setSizePolicy(sizePolicy)
        self.text_shrinking_state.setObjectName("text_shrinking_state")
        self.verticalLayout_out_shrikning.addWidget(self.text_shrinking_state)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_out_shrikning.addWidget(self.label_15)
        self.text_shrinking_stream = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_shrinking_stream.sizePolicy().hasHeightForWidth())
        self.text_shrinking_stream.setSizePolicy(sizePolicy)
        self.text_shrinking_stream.setObjectName("text_shrinking_stream")
        self.verticalLayout_out_shrikning.addWidget(self.text_shrinking_stream)
        self.grid_Generators.addLayout(self.verticalLayout_out_shrikning, 2, 2, 1, 1)
        self.textBrowser_geffe_results = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_geffe_results.setObjectName("textBrowser_geffe_results")
        self.grid_Generators.addWidget(self.textBrowser_geffe_results, 0, 4, 1, 1)
        self.textBrowser_stopandgo_results = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_stopandgo_results.setObjectName("textBrowser_stopandgo_results")
        self.grid_Generators.addWidget(self.textBrowser_stopandgo_results, 1, 4, 1, 1)
        self.textBrowser_shrinking_results = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_shrinking_results.setObjectName("textBrowser_shrinking_results")
        self.grid_Generators.addWidget(self.textBrowser_shrinking_results, 2, 4, 1, 1)
        self.grid_Generators.setColumnMinimumWidth(0, 50)
        self.grid_Generators.setColumnMinimumWidth(1, 50)
        self.grid_Generators.setColumnMinimumWidth(2, 50)
        self.grid_Generators.setColumnMinimumWidth(3, 50)
        self.grid_Generators.setColumnStretch(0, 1)
        self.grid_Generators.setColumnStretch(1, 1)
        self.grid_Generators.setColumnStretch(2, 100)
        self.grid_Generators.setColumnStretch(3, 1)
        self.grid_Generators.setRowStretch(0, 1)
        self.grid_Generators.setRowStretch(1, 1)
        self.grid_Generators.setRowStretch(2, 1)
        self.MainGrid.addLayout(self.grid_Generators, 0, 0, 1, 1)
        self.MainGrid.setColumnStretch(0, 2)
        self.gridLayout.addLayout(self.MainGrid, 0, 0, 1, 1)
        self.gridLayout.setColumnStretch(0, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 946, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit_stopandgo_init_state.setToolTip(_translate("MainWindow", "0 is random value."))
        self.lineEdit_stopandgo_init_state.setText(_translate("MainWindow", "0"))
        self.label_9.setText(_translate("MainWindow", "Registers Size"))
        self.label_7.setText(_translate("MainWindow", "LFSR Config"))
        self.lineEdit_stopandgo_config.setToolTip(_translate("MainWindow", "Specify active bits in LFSR. 0 is random value. Use deciaml values."))
        self.lineEdit_stopandgo_config.setText(_translate("MainWindow", "0"))
        self.label_8.setText(_translate("MainWindow", "Initial state"))
        self.label_2.setText(_translate("MainWindow", "Initial state"))
        self.label.setText(_translate("MainWindow", "Registers Size"))
        self.lineEdit_geffe_config.setToolTip(_translate("MainWindow", "Specify active bits in LFSR. 0 is random value. Use deciaml values."))
        self.lineEdit_geffe_config.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "LFSR Config"))
        self.lineEdit_geffe_init_state.setToolTip(_translate("MainWindow", "0 is random value."))
        self.lineEdit_geffe_init_state.setText(_translate("MainWindow", "0"))
        self.pushButton_new_Geffe.setText(_translate("MainWindow", "New\n"
"Generator Geffe’go"))
        self.pushButton_geffe_next.setText(_translate("MainWindow", "Next"))
        self.pushButton_geffe_next_15times.setText(_translate("MainWindow", "Next x15"))
        self.pushButton_geffe_fill.setText(_translate("MainWindow", "Fill to 20.000"))
        self.pushButton_new_stopandgo.setText(_translate("MainWindow", "New\n"
"Stop-and-Go"))
        self.pushButton_stopandgo_next.setText(_translate("MainWindow", "Next"))
        self.pushButton_stopandgo_next_15times.setText(_translate("MainWindow", "Next x 15"))
        self.pushButton_stopandgo_fill.setText(_translate("MainWindow", "Fill to 20.000"))
        self.pushButton_new_shrinking.setText(_translate("MainWindow", "New\n"
"Shrinking Generator"))
        self.pushButton_shrinking_next.setText(_translate("MainWindow", "Next"))
        self.pushButton_shrinking_next_15times.setText(_translate("MainWindow", "Next x 15"))
        self.pushButton_shrinking_fill.setText(_translate("MainWindow", "Fill to 20.000"))
        self.label_4.setText(_translate("MainWindow", "Registers Size"))
        self.label_5.setText(_translate("MainWindow", "Initial state"))
        self.label_6.setText(_translate("MainWindow", "LFSR Config"))
        self.lineEdit_shrinking_init_state.setToolTip(_translate("MainWindow", "0 is random value."))
        self.lineEdit_shrinking_init_state.setText(_translate("MainWindow", "0"))
        self.lineEdit_shrinking_config.setToolTip(_translate("MainWindow", "Specify active bits in LFSR. 0 is random value. Use deciaml values."))
        self.lineEdit_shrinking_config.setText(_translate("MainWindow", "0"))
        self.pushButton_shrinking_test_monobit.setText(_translate("MainWindow", "Test Mono Bit"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.label_12.setText(_translate("MainWindow", "State"))
        self.label_13.setText(_translate("MainWindow", "Stream"))
        self.label_10.setText(_translate("MainWindow", "State"))
        self.label_11.setText(_translate("MainWindow", "Stream"))
        self.pushButton_stopandgo_test_monobit.setText(_translate("MainWindow", "Test Mono Bit"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_8.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_gefe_test_monobit.setText(_translate("MainWindow", "Test Mono Bit"))
        self.pushButton_7.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton"))
        self.label_14.setText(_translate("MainWindow", "State"))
        self.label_15.setText(_translate("MainWindow", "Stream"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
