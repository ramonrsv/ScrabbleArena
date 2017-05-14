import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from main_window import Ui_MainWindow
from lib.settings import Words_with_friends_board_configuration, Words_with_friends_fast_play_board_configuration
from lib.settings import English_classic_100_tile_distribution, Standard_player_tray_size
from lib.game_controller import GameController


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = QMainWindow()

    ui_main_window = Ui_MainWindow()
    ui_main_window.setupUi(main_window)

    game_controller = GameController(English_classic_100_tile_distribution,
                                     Words_with_friends_board_configuration,
                                     Standard_player_tray_size,
                                     ui_main_window.main_board_frame,
                                     ui_main_window.x_label_widget,
                                     ui_main_window.y_label_widget,
                                     ui_main_window.player1_tiles,
                                     ui_main_window.player2_tiles)

    #ui.update_display_button.clicked.connect(ui_board.update_display)

    main_window.show()
    sys.exit(app.exec_())
