# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Abhinav\Downloads\json\PyQtGui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import json_parse


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        listTypes = [
            ('Area'),
            ('Version'),
            ('Hostname'),
        ]

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(981, 817)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(140, 50, 551, 631))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButtonArea = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonArea.setObjectName("pushButtonArea")
        self.verticalLayout.addWidget(self.pushButtonArea)
        self.pushButtonVersion = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonVersion.setObjectName("pushButtonVersion")
        self.verticalLayout.addWidget(self.pushButtonVersion)
        self.pushButtonHist = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonHist.setObjectName("pushButtonHist")
        self.verticalLayout.addWidget(self.pushButtonHist)
        self.pushButtonPie = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonPie.setObjectName("pushButtonPie")
        self.verticalLayout.addWidget(self.pushButtonPie)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(0, 16))
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEditName = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEditName.setObjectName("lineEditName")
        self.horizontalLayout_2.addWidget(self.lineEditName)
        self.comboBoxType = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBoxType.setMinimumSize(QtCore.QSize(200, 0))
        self.comboBoxType.setObjectName("comboBoxType")
        self.comboBoxType.addItems(listTypes)
        self.horizontalLayout_2.addWidget(self.comboBoxType)
        self.pushButtonGo1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonGo1.setObjectName("pushButtonGo1")
        self.horizontalLayout_2.addWidget(self.pushButtonGo1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 200))
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 200))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_4.addWidget(self.textBrowser)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.spinBoxIndex = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBoxIndex.setEnabled(True)
        self.spinBoxIndex.setMinimum(1)
        self.spinBoxIndex.setMaximum(3053)
        self.spinBoxIndex.setObjectName("spinBoxIndex")
        self.horizontalLayout_5.addWidget(self.spinBoxIndex)
        self.pushButtonGo2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonGo2.setMaximumSize(QtCore.QSize(75, 16777215))
        self.pushButtonGo2.setObjectName("pushButtonGo2")
        self.horizontalLayout_5.addWidget(self.pushButtonGo2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser_2.setMinimumSize(QtCore.QSize(0, 200))
        self.textBrowser_2.setMaximumSize(QtCore.QSize(16777215, 200))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout_3.addWidget(self.textBrowser_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 981, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButtonHist.clicked.connect(self.showHist)
        self.pushButtonPie.clicked.connect(self.showPie)
        self.pushButtonArea.clicked.connect(self.showArea)
        self.pushButtonVersion.clicked.connect(self.showVerison)
        self.pushButtonGo1.clicked.connect(self.getInfo)
        self.pushButtonGo2.clicked.connect(self.getIndex)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SBHSData"))
        self.pushButtonArea.setText(_translate("MainWindow", "Average Uptime of Each Area"))
        self.pushButtonVersion.setText(_translate("MainWindow", "Average Uptime of Each Version"))
        self.pushButtonHist.setText(_translate("MainWindow", "Histogram of Uptime"))
        self.pushButtonPie.setText(_translate("MainWindow", "Pie Chart of Area"))
        self.label.setText(_translate("MainWindow", "Enter the name and type of parameter"))
        self.pushButtonGo1.setText(_translate("MainWindow", "GO"))
        self.label_2.setText(_translate("MainWindow", "Enter index"))
        self.pushButtonGo2.setText(_translate("MainWindow", "GO"))

    def showHist(self):
        json_parse.histogram()

    def showPie(self):
        json_parse.pie()

    def showArea(self):
        json_parse.area()

    def showVerison(self):
        json_parse.version()

    def getInfo(self):
        text = str(self.comboBoxType.currentText())
        if (text == "Hostname"):
            try:
                editText1 = json_parse.infoHostname(self.lineEditName.text())
                self.textBrowser.setText(editText1)
            except:
                self.textBrowser.setText("Invalid Input")
        if (text == "Area"):
            try:
                editText1 = json_parse.infoArea1(self.lineEditName.text())
                editText2 = json_parse.infoArea2(self.lineEditName.text())
                self.textBrowser.setText("There are " + str(editText1) + " instances of " + self.lineEditName.text() + "\nThe most commonly used version is " + editText2)
            except:
                self.textBrowser.setText("Invalid Input")
        if (text == "Version"):
            try:
                editText1 = json_parse.infoVersion1(self.lineEditName.text())
                editText2 = json_parse.infoVersion2(self.lineEditName.text())
                self.textBrowser.setText("There are " + str(editText1) + " instances of " + self.lineEditName.text() + "\nThe area using this version the most is " + editText2)
            except:
                self.textBrowser.setText("Invalid Input")

    def getIndex(self):
        indexArea = json_parse.infoIndexArea(self.spinBoxIndex.value())
        indexVersion = json_parse.infoIndexVersion(self.spinBoxIndex.value())
        indexUptime = json_parse.infoIndexUptime(self.spinBoxIndex.value())
        indexHostname = json_parse.infoIndexHostname(self.spinBoxIndex.value())

        self.textBrowser_2.setText("Area: " + indexArea + "\nVersion: " + indexVersion + "\nUptime: " + indexUptime + "\nHostname: " + indexHostname)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
