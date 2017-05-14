import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from main_window import Ui_MainWindow
from lib.board_ui import UiBoard, UiTileTray, UiTile
from lib.settings import Words_with_friends_board_configuration, Words_with_friends_fast_play_board_configuration
from lib.settings import English_classic_100_tile_distribution, Standard_player_tray_size
from lib.tile import Tile, TileBag


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = QMainWindow()

    ui_main_window = Ui_MainWindow()
    ui_main_window.setupUi(main_window)

    ui_board = UiBoard(ui_main_window.main_board_frame,
                       ui_main_window.x_label_widget,
                       ui_main_window.y_label_widget,
                       Words_with_friends_board_configuration)
    ui_board.initialize_display()

    Tile.set_letter_distribution(English_classic_100_tile_distribution.letter_distribution)
    tile_bag = TileBag(English_classic_100_tile_distribution)

    player1_tray = UiTileTray(ui_main_window.player1_tiles,
                              tile_bag.take(Standard_player_tray_size), Standard_player_tray_size)
    player2_tray = UiTileTray(ui_main_window.player2_tiles,
                              tile_bag.take(Standard_player_tray_size), Standard_player_tray_size)
    player1_tray.initialize_display()
    player2_tray.initialize_display()
    #ui.update_display_button.clicked.connect(ui_board.update_display)

    main_window.show()
    sys.exit(app.exec_())
