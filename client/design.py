# Form implementation generated from reading ui file 'C:\python\design.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(343, 500)
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(80, 310, 181, 81))
        font = QtGui.QFont()
        font.setFamily("MingLiU-ExtB")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 271, 271))
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 343, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.action_2 = QtGui.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtGui.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_3)
        self.menuFile.addAction(self.action_2)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Оповещение АПК \"Русский Мрамор\""))
        self.pushButton.setText(_translate("MainWindow", "Вызов"))
        self.label.setText(_translate("MainWindow", "\"Вызов\" что бы вызвать"))
        self.menuFile.setTitle(_translate("MainWindow", "Файл"))
        self.action_2.setText(_translate("MainWindow", "Выход"))
        self.action_3.setText(_translate("MainWindow", "Настройки"))
