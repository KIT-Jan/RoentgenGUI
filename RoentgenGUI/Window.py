# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(901, 583)
        MainWindow.setMinimumSize(QtCore.QSize(0, 100))
        MainWindow.setStyleSheet("QLCDNumber#time_lcd{background-color:rgb(137, 1, 37);}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(50, 190, 241, 331))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.grid2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.grid2.setContentsMargins(0, 0, 0, 0)
        self.grid2.setObjectName("grid2")
        self.NoS = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.NoS.setMaximumSize(QtCore.QSize(16777215, 20))
        self.NoS.setObjectName("NoS")
        self.grid2.addWidget(self.NoS, 0, 0, 1, 1)
        self.stepsize = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.stepsize.setMaximumSize(QtCore.QSize(16777215, 20))
        self.stepsize.setObjectName("stepsize")
        self.grid2.addWidget(self.stepsize, 2, 0, 1, 1)
        self.rdose_line = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.rdose_line.setObjectName("rdose_line")
        self.grid2.addWidget(self.rdose_line, 7, 0, 1, 1)
        self.required_dose = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.required_dose.setMaximumSize(QtCore.QSize(16777215, 20))
        self.required_dose.setObjectName("required_dose")
        self.grid2.addWidget(self.required_dose, 6, 0, 1, 1)
        self.stepsize_line = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.stepsize_line.setObjectName("stepsize_line")
        self.grid2.addWidget(self.stepsize_line, 3, 0, 1, 1)
        self.NoS_line = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.NoS_line.setObjectName("NoS_line")
        self.grid2.addWidget(self.NoS_line, 1, 0, 1, 1)
        self.doserate_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.doserate_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.doserate_label.setObjectName("doserate_label")
        self.grid2.addWidget(self.doserate_label, 4, 0, 1, 1)
        self.doserate_line = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.doserate_line.setObjectName("doserate_line")
        self.grid2.addWidget(self.doserate_line, 5, 0, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(350, 435, 155, 71))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.time_grid = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.time_grid.setContentsMargins(0, 0, 0, 0)
        self.time_grid.setObjectName("time_grid")
        self.time = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.time.setObjectName("time")
        self.time_grid.addWidget(self.time)
        self.time_lcd = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.time_lcd.setObjectName("time_lcd")
        self.time_grid.addWidget(self.time_lcd)
        self.time_lcd.setDigitCount(8)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 20, 245, 121))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.start_grid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.start_grid.setContentsMargins(0, 0, 0, 0)
        self.start_grid.setObjectName("start_grid")
        self.Start = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Start.setMinimumSize(QtCore.QSize(0, 100))
        self.Start.setIconSize(QtCore.QSize(100, 100))
        self.Start.setObjectName("Start")
        self.Start.setStyleSheet(
    "QPushButton:pressed{background-color: rgb(0,150,130)} QPushButton{color: black}")
        self.start_grid.addWidget(self.Start, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(570, 380, 248, 175))
        self.label.setObjectName("label")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(335, 20, 221, 351))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.Geometry_Grid = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.Geometry_Grid.setContentsMargins(0, 0, 0, 0)
        self.Geometry_Grid.setObjectName("Geometry_Grid")
        self.Radius_label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.Radius_label.setObjectName("Radius_label")
        self.Geometry_Grid.addWidget(self.Radius_label, 9, 0, 1, 2)
        self.height = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.height.setObjectName("height")
        self.Geometry_Grid.addWidget(self.height, 14, 0, 1, 2)
        self.Width_label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.Width_label.setObjectName("Width_label")
        self.Geometry_Grid.addWidget(self.Width_label, 11, 0, 1, 2)
        self.radius = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.radius.setText("")
        self.radius.setObjectName("radius")
        self.Geometry_Grid.addWidget(self.radius, 10, 0, 1, 2)
        self.width = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.width.setObjectName("width")
        self.Geometry_Grid.addWidget(self.width, 12, 0, 1, 2)
        self.Height_label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.Height_label.setObjectName("Height_label")
        self.Geometry_Grid.addWidget(self.Height_label, 13, 0, 1, 2)
        self.Geometry_label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.Geometry_label.setStyleSheet("font: 87 10pt \"Arial Black\";")
        self.Geometry_label.setObjectName("Geometry_label")
        self.Geometry_Grid.addWidget(self.Geometry_label, 5, 0, 1, 2)
        self.update_button = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.update_button.sizePolicy().hasHeightForWidth())
        self.update_button.setSizePolicy(sizePolicy)
        self.update_button.setMinimumSize(QtCore.QSize(0, 50))
        self.update_button.setMaximumSize(QtCore.QSize(300, 16777215))
        self.update_button.setObjectName("update_button")
        self.Geometry_Grid.addWidget(self.update_button, 3, 0, 2, 2)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(620, 30, 201, 321))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.log_grid = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.log_grid.setContentsMargins(0, 0, 0, 0)
        self.log_grid.setObjectName("log_grid")
        self.log_text = QtWidgets.QTextBrowser(self.gridLayoutWidget_4)
        self.log_text.setObjectName("log_text")
        self.log_grid.addWidget(self.log_text, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_2.setStyleSheet("font: 87 10pt \"Arial Black\";")
        self.label_2.setObjectName("label_2")
        self.log_grid.addWidget(self.label_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gose Irradiation"))
        self.NoS.setText(_translate("MainWindow", "Number of Scans"))
        self.stepsize.setText(_translate("MainWindow", "Step Size (µm)"))
        self.required_dose.setText(_translate("MainWindow", "Required Dose (krad)"))
        self.doserate_label.setText(_translate("MainWindow", "Dose Rate (krad/h)"))
        self.time.setText(_translate("MainWindow", "Estimated Time (min)"))
        self.Start.setText(_translate("MainWindow", "Start"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/Bild/Roentgen.svg\"/></p></body></html>"))
        self.Radius_label.setText(_translate("MainWindow", "Beamspot Radius (mm)"))
        self.update_button.setText(_translate("MainWindow", "Update Properties"))
        self.Height_label.setText(_translate("MainWindow", "Height (y) in mm"))
        self.Width_label.setText(_translate("MainWindow", "Width (x) in mm"))
        self.Geometry_label.setText(_translate("MainWindow", "Geometry"))
        self.log_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Activities"))

import placement_rc