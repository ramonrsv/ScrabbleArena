import sys
from PyQt4 import QtGui
from main_window import Ui_MainWindow
from lib.board_ui import UiBoard
from lib.settings import Words_with_friends_board_configuration


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    main_window = QtGui.QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(main_window)

    ui_board = UiBoard(ui.main_board_widget, Words_with_friends_board_configuration)
    ui.draw_button.clicked.connect(ui_board.draw)

    main_window.show()
    sys.exit(app.exec_())
