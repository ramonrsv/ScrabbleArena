# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main_window.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 762)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.main_board_widget = QtGui.QWidget(self.centralwidget)
        self.main_board_widget.setGeometry(QtCore.QRect(50, 40, 500, 400))
        self.main_board_widget.setObjectName(_fromUtf8("main_board_widget"))
        self.player1_label = QtGui.QLabel(self.centralwidget)
        self.player1_label.setGeometry(QtCore.QRect(630, 40, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.player1_label.setFont(font)
        self.player1_label.setAlignment(QtCore.Qt.AlignCenter)
        self.player1_label.setObjectName(_fromUtf8("player1_label"))
        self.draw_button = QtGui.QPushButton(self.centralwidget)
        self.draw_button.setGeometry(QtCore.QRect(680, 670, 75, 23))
        self.draw_button.setObjectName(_fromUtf8("draw_button"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.player1_label.setText(_translate("MainWindow", "Player 1", None))
        self.draw_button.setText(_translate("MainWindow", "Draw", None))

