# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 1010)
        MainWindow.setMinimumSize(QtCore.QSize(960, 800))
        MainWindow.setMaximumSize(QtCore.QSize(960, 1080))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_board_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_board_frame.setGeometry(QtCore.QRect(50, 50, 557, 557))
        self.main_board_frame.setMaximumSize(QtCore.QSize(557, 557))
        self.main_board_frame.setObjectName("main_board_frame")
        self.y_label_widget = QtWidgets.QWidget(self.centralwidget)
        self.y_label_widget.setGeometry(QtCore.QRect(20, 50, 30, 557))
        self.y_label_widget.setObjectName("y_label_widget")
        self.x_label_widget = QtWidgets.QWidget(self.centralwidget)
        self.x_label_widget.setGeometry(QtCore.QRect(50, 20, 557, 30))
        self.x_label_widget.setObjectName("x_label_widget")
        self.settings_widget = QtWidgets.QWidget(self.centralwidget)
        self.settings_widget.setGeometry(QtCore.QRect(620, 50, 321, 131))
        self.settings_widget.setObjectName("settings_widget")
        self.language_box = QtWidgets.QComboBox(self.settings_widget)
        self.language_box.setGeometry(QtCore.QRect(110, 10, 201, 22))
        self.language_box.setObjectName("language_box")
        self.language_label = QtWidgets.QLabel(self.settings_widget)
        self.language_label.setGeometry(QtCore.QRect(20, 10, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.language_label.setFont(font)
        self.language_label.setObjectName("language_label")
        self.dictionary_label = QtWidgets.QLabel(self.settings_widget)
        self.dictionary_label.setGeometry(QtCore.QRect(20, 40, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dictionary_label.setFont(font)
        self.dictionary_label.setObjectName("dictionary_label")
        self.dictionary_box = QtWidgets.QComboBox(self.settings_widget)
        self.dictionary_box.setGeometry(QtCore.QRect(110, 40, 201, 22))
        self.dictionary_box.setObjectName("dictionary_box")
        self.game_type_label = QtWidgets.QLabel(self.settings_widget)
        self.game_type_label.setGeometry(QtCore.QRect(20, 70, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.game_type_label.setFont(font)
        self.game_type_label.setObjectName("game_type_label")
        self.game_type_box = QtWidgets.QComboBox(self.settings_widget)
        self.game_type_box.setGeometry(QtCore.QRect(110, 70, 201, 22))
        self.game_type_box.setObjectName("game_type_box")
        self.debug_mode_button = QtWidgets.QRadioButton(self.settings_widget)
        self.debug_mode_button.setGeometry(QtCore.QRect(210, 100, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.debug_mode_button.setFont(font)
        self.debug_mode_button.setObjectName("debug_mode_button")
        self.player1_stats_widget = QtWidgets.QWidget(self.centralwidget)
        self.player1_stats_widget.setGeometry(QtCore.QRect(620, 210, 321, 191))
        self.player1_stats_widget.setObjectName("player1_stats_widget")
        self.player_name_label_1 = QtWidgets.QLabel(self.player1_stats_widget)
        self.player_name_label_1.setGeometry(QtCore.QRect(10, 10, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.player_name_label_1.setFont(font)
        self.player_name_label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.player_name_label_1.setObjectName("player_name_label_1")
        self.player_selection_box_1 = QtWidgets.QComboBox(self.player1_stats_widget)
        self.player_selection_box_1.setGeometry(QtCore.QRect(110, 10, 201, 22))
        self.player_selection_box_1.setObjectName("player_selection_box_1")
        self.score_label_1 = QtWidgets.QLabel(self.player1_stats_widget)
        self.score_label_1.setGeometry(QtCore.QRect(20, 40, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.score_label_1.setFont(font)
        self.score_label_1.setObjectName("score_label_1")
        self.score_lcd_1 = QtWidgets.QLCDNumber(self.player1_stats_widget)
        self.score_lcd_1.setGeometry(QtCore.QRect(70, 40, 64, 23))
        self.score_lcd_1.setObjectName("score_lcd_1")
        self.avg_word_score_label_1 = QtWidgets.QLabel(self.player1_stats_widget)
        self.avg_word_score_label_1.setGeometry(QtCore.QRect(20, 70, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.avg_word_score_label_1.setFont(font)
        self.avg_word_score_label_1.setObjectName("avg_word_score_label_1")
        self.avg_word_score_lcd_1 = QtWidgets.QLCDNumber(self.player1_stats_widget)
        self.avg_word_score_lcd_1.setGeometry(QtCore.QRect(180, 70, 64, 23))
        self.avg_word_score_lcd_1.setObjectName("avg_word_score_lcd_1")
        self.top_word_label_1 = QtWidgets.QLabel(self.player1_stats_widget)
        self.top_word_label_1.setGeometry(QtCore.QRect(20, 130, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.top_word_label_1.setFont(font)
        self.top_word_label_1.setObjectName("top_word_label_1")
        self.top_word_score_label_1 = QtWidgets.QLabel(self.player1_stats_widget)
        self.top_word_score_label_1.setGeometry(QtCore.QRect(20, 100, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.top_word_score_label_1.setFont(font)
        self.top_word_score_label_1.setObjectName("top_word_score_label_1")
        self.top_word_score_lcd_1 = QtWidgets.QLCDNumber(self.player1_stats_widget)
        self.top_word_score_lcd_1.setGeometry(QtCore.QRect(180, 100, 64, 23))
        self.top_word_score_lcd_1.setObjectName("top_word_score_lcd_1")
        self.top_word_line_1 = QtWidgets.QLineEdit(self.player1_stats_widget)
        self.top_word_line_1.setGeometry(QtCore.QRect(110, 130, 201, 20))
        self.top_word_line_1.setReadOnly(True)
        self.top_word_line_1.setObjectName("top_word_line_1")
        self.turns_label_1 = QtWidgets.QLabel(self.player1_stats_widget)
        self.turns_label_1.setGeometry(QtCore.QRect(170, 40, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.turns_label_1.setFont(font)
        self.turns_label_1.setObjectName("turns_label_1")
        self.turns_lcd_1 = QtWidgets.QLCDNumber(self.player1_stats_widget)
        self.turns_lcd_1.setGeometry(QtCore.QRect(220, 40, 64, 23))
        self.turns_lcd_1.setObjectName("turns_lcd_1")
        self.longest_word_line_1 = QtWidgets.QLineEdit(self.player1_stats_widget)
        self.longest_word_line_1.setGeometry(QtCore.QRect(110, 160, 201, 20))
        self.longest_word_line_1.setText("")
        self.longest_word_line_1.setReadOnly(True)
        self.longest_word_line_1.setObjectName("longest_word_line_1")
        self.longest_word_label_1 = QtWidgets.QLabel(self.player1_stats_widget)
        self.longest_word_label_1.setGeometry(QtCore.QRect(20, 160, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.longest_word_label_1.setFont(font)
        self.longest_word_label_1.setObjectName("longest_word_label_1")
        self.player_area_widget = QtWidgets.QWidget(self.centralwidget)
        self.player_area_widget.setGeometry(QtCore.QRect(20, 620, 921, 231))
        self.player_area_widget.setObjectName("player_area_widget")
        self.player1_label_pa = QtWidgets.QLabel(self.player_area_widget)
        self.player1_label_pa.setGeometry(QtCore.QRect(190, 10, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.player1_label_pa.setFont(font)
        self.player1_label_pa.setAlignment(QtCore.Qt.AlignCenter)
        self.player1_label_pa.setObjectName("player1_label_pa")
        self.player2_label_pq = QtWidgets.QLabel(self.player_area_widget)
        self.player2_label_pq.setGeometry(QtCore.QRect(540, 10, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.player2_label_pq.setFont(font)
        self.player2_label_pq.setAlignment(QtCore.Qt.AlignCenter)
        self.player2_label_pq.setObjectName("player2_label_pq")
        self.player2_show_tiles_button = QtWidgets.QRadioButton(self.player_area_widget)
        self.player2_show_tiles_button.setGeometry(QtCore.QRect(730, 10, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.player2_show_tiles_button.setFont(font)
        self.player2_show_tiles_button.setObjectName("player2_show_tiles_button")
        self.player1_tiles = QtWidgets.QWidget(self.player_area_widget)
        self.player1_tiles.setGeometry(QtCore.QRect(40, 40, 382, 39))
        self.player1_tiles.setObjectName("player1_tiles")
        self.player2_tiles = QtWidgets.QWidget(self.player_area_widget)
        self.player2_tiles.setGeometry(QtCore.QRect(500, 40, 382, 39))
        self.player2_tiles.setObjectName("player2_tiles")
        self.player2_stats_widget = QtWidgets.QWidget(self.centralwidget)
        self.player2_stats_widget.setGeometry(QtCore.QRect(620, 420, 321, 191))
        self.player2_stats_widget.setObjectName("player2_stats_widget")
        self.player_name_label_2 = QtWidgets.QLabel(self.player2_stats_widget)
        self.player_name_label_2.setGeometry(QtCore.QRect(10, 10, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.player_name_label_2.setFont(font)
        self.player_name_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.player_name_label_2.setObjectName("player_name_label_2")
        self.player_selection_box_2 = QtWidgets.QComboBox(self.player2_stats_widget)
        self.player_selection_box_2.setGeometry(QtCore.QRect(110, 10, 201, 22))
        self.player_selection_box_2.setObjectName("player_selection_box_2")
        self.score_label_2 = QtWidgets.QLabel(self.player2_stats_widget)
        self.score_label_2.setGeometry(QtCore.QRect(20, 40, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.score_label_2.setFont(font)
        self.score_label_2.setObjectName("score_label_2")
        self.score_lcd_2 = QtWidgets.QLCDNumber(self.player2_stats_widget)
        self.score_lcd_2.setGeometry(QtCore.QRect(70, 40, 64, 23))
        self.score_lcd_2.setObjectName("score_lcd_2")
        self.avg_word_score_label_2 = QtWidgets.QLabel(self.player2_stats_widget)
        self.avg_word_score_label_2.setGeometry(QtCore.QRect(20, 70, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.avg_word_score_label_2.setFont(font)
        self.avg_word_score_label_2.setObjectName("avg_word_score_label_2")
        self.avg_word_score_lcd_2 = QtWidgets.QLCDNumber(self.player2_stats_widget)
        self.avg_word_score_lcd_2.setGeometry(QtCore.QRect(180, 70, 64, 23))
        self.avg_word_score_lcd_2.setObjectName("avg_word_score_lcd_2")
        self.top_word_label_2 = QtWidgets.QLabel(self.player2_stats_widget)
        self.top_word_label_2.setGeometry(QtCore.QRect(20, 130, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.top_word_label_2.setFont(font)
        self.top_word_label_2.setObjectName("top_word_label_2")
        self.top_word_score_label_2 = QtWidgets.QLabel(self.player2_stats_widget)
        self.top_word_score_label_2.setGeometry(QtCore.QRect(20, 100, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.top_word_score_label_2.setFont(font)
        self.top_word_score_label_2.setObjectName("top_word_score_label_2")
        self.top_word_score_lcd_2 = QtWidgets.QLCDNumber(self.player2_stats_widget)
        self.top_word_score_lcd_2.setGeometry(QtCore.QRect(180, 100, 64, 23))
        self.top_word_score_lcd_2.setObjectName("top_word_score_lcd_2")
        self.top_word_line_2 = QtWidgets.QLineEdit(self.player2_stats_widget)
        self.top_word_line_2.setGeometry(QtCore.QRect(110, 130, 201, 20))
        self.top_word_line_2.setReadOnly(True)
        self.top_word_line_2.setObjectName("top_word_line_2")
        self.turns_label_2 = QtWidgets.QLabel(self.player2_stats_widget)
        self.turns_label_2.setGeometry(QtCore.QRect(170, 40, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.turns_label_2.setFont(font)
        self.turns_label_2.setObjectName("turns_label_2")
        self.turns_lcd_2 = QtWidgets.QLCDNumber(self.player2_stats_widget)
        self.turns_lcd_2.setGeometry(QtCore.QRect(220, 40, 64, 23))
        self.turns_lcd_2.setObjectName("turns_lcd_2")
        self.longest_word_line_2 = QtWidgets.QLineEdit(self.player2_stats_widget)
        self.longest_word_line_2.setGeometry(QtCore.QRect(110, 160, 201, 20))
        self.longest_word_line_2.setText("")
        self.longest_word_line_2.setReadOnly(True)
        self.longest_word_line_2.setObjectName("longest_word_line_2")
        self.longest_word_label_2 = QtWidgets.QLabel(self.player2_stats_widget)
        self.longest_word_label_2.setGeometry(QtCore.QRect(20, 160, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.longest_word_label_2.setFont(font)
        self.longest_word_label_2.setObjectName("longest_word_label_2")
        self.debug_area_widget = QtWidgets.QWidget(self.centralwidget)
        self.debug_area_widget.setGeometry(QtCore.QRect(20, 860, 921, 101))
        self.debug_area_widget.setObjectName("debug_area_widget")
        self.toggle_configuration = QtWidgets.QPushButton(self.debug_area_widget)
        self.toggle_configuration.setGeometry(QtCore.QRect(30, 10, 111, 23))
        self.toggle_configuration.setObjectName("toggle_configuration")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.language_label.setText(_translate("MainWindow", "Language"))
        self.dictionary_label.setText(_translate("MainWindow", "Dictionary"))
        self.game_type_label.setText(_translate("MainWindow", "Game Type"))
        self.debug_mode_button.setText(_translate("MainWindow", "Debug Mode"))
        self.player_name_label_1.setText(_translate("MainWindow", "Player 1"))
        self.score_label_1.setText(_translate("MainWindow", "Score"))
        self.avg_word_score_label_1.setText(_translate("MainWindow", "Avg. Word Score"))
        self.top_word_label_1.setText(_translate("MainWindow", "Top Word"))
        self.top_word_score_label_1.setText(_translate("MainWindow", "Top Word Score"))
        self.turns_label_1.setText(_translate("MainWindow", "Turns"))
        self.longest_word_label_1.setText(_translate("MainWindow", "Longest W."))
        self.player1_label_pa.setText(_translate("MainWindow", "Player 1"))
        self.player2_label_pq.setText(_translate("MainWindow", "Player 2"))
        self.player2_show_tiles_button.setText(_translate("MainWindow", "Show Tiles"))
        self.player_name_label_2.setText(_translate("MainWindow", "Player 2"))
        self.score_label_2.setText(_translate("MainWindow", "Score"))
        self.avg_word_score_label_2.setText(_translate("MainWindow", "Avg. Word Score"))
        self.top_word_label_2.setText(_translate("MainWindow", "Top Word"))
        self.top_word_score_label_2.setText(_translate("MainWindow", "Top Word Score"))
        self.turns_label_2.setText(_translate("MainWindow", "Turns"))
        self.longest_word_label_2.setText(_translate("MainWindow", "Longest W."))
        self.toggle_configuration.setText(_translate("MainWindow", "ToggleConfiguration"))

