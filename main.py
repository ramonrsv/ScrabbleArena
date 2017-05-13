import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from main_window import Ui_MainWindow
from lib.board_ui import UiBoard
from lib.settings import Words_with_friends_board_configuration, Words_with_friends_fast_play_board_configuration


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(main_window)

    ui_board = UiBoard(ui.main_board_frame, ui.x_label_widget, ui.y_label_widget,
                       Words_with_friends_board_configuration)
    ui_board.initialize_display()
    #ui.update_display_button.clicked.connect(ui_board.update_display)

    main_window.show()
    sys.exit(app.exec_())
