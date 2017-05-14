from .settings import Words_with_friends_board_configuration, Words_with_friends_fast_play_board_configuration
from .settings import English_classic_100_tile_distribution, Standard_player_tray_size
from .game_controller import GameController


class UiManager:
    _default_tile_distribution = English_classic_100_tile_distribution
    _default_board_configuration = Words_with_friends_board_configuration
    _default_tray_size = Standard_player_tray_size

    def __init__(self, ui_main_window):
        self._ui_main_window = ui_main_window

        self._game_controller = GameController(self._ui_main_window.main_board_frame,
                                               self._ui_main_window.x_label_widget,
                                               self._ui_main_window.y_label_widget,
                                               self._ui_main_window.player1_tiles,
                                               self._ui_main_window.player2_tiles)

        self._register_debug_actions()
        self._game_controller.setup_new_game(self._default_tile_distribution,
                                             self._default_board_configuration,
                                             self._default_tray_size)
        self._temp = True

    def _register_debug_actions(self):
        self._ui_main_window.toggle_configuration.clicked.connect(self._temp_toggle_board_config)

    def _temp_toggle_board_config(self):
        print("_temp_toggle_board_config")
        if self._temp:
            self._temp = False
            self._game_controller.hide()
            print("hidding")
        else:
            self._temp = True
            self._game_controller.show()
            print("showing")