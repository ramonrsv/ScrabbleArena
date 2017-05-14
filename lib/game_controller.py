from .board_ui import UiBoardPosition
from .board_ui import UiBoard, UiTileTray
from .tile import Tile, TileBag


class GameController:
    def __init__(self, main_board_widget, x_label_widget, y_label_widget, player1_tray_widget, player2_tray_widget,
                 tile_distribution=None, board_configuration=None, tray_size=None):
        self._main_board_widget = main_board_widget
        self._x_label_widget = x_label_widget
        self._y_label_widget = y_label_widget
        self._player1_tray_widget = player1_tray_widget
        self._player2_tray_widget = player2_tray_widget

        self._letter_distribution = None
        self._tile_distribution = None
        self._board_configuration = None
        self._tray_size = None

        self._tile_bag = None
        self._ui_board = None
        self._player1_ui_tray = None
        self._player2_ui_tray = None

        if tile_distribution and board_configuration and tray_size:
            self.setup_new_game(tile_distribution, board_configuration, tray_size)

    def setup_new_game(self, tile_distribution, board_configuration, tray_size):
        self._letter_distribution = tile_distribution.letter_distribution
        self._tile_distribution = tile_distribution
        self._board_configuration = board_configuration
        self._tray_size = tray_size

        Tile.set_letter_distribution(self._letter_distribution)
        self._tile_bag = TileBag(self._tile_distribution)

        self._create_new_board()
        self._player1_ui_tray = self._create_new_player_tray(self._player1_tray_widget, self._player1_ui_tray)
        self._player2_ui_tray = self._create_new_player_tray(self._player2_tray_widget, self._player2_ui_tray)

    def _create_new_board(self):
        # TODO: the old object isn't deleted and memory leaks, something preventing garbage collection?
        if self._ui_board:
            self._ui_board.hide()
        self._ui_board = UiBoard(self._main_board_widget, self._x_label_widget, self._y_label_widget,
                                 self._board_configuration, self)

    def _create_new_player_tray(self, player_ui_tray_widget, old_tray):
        # TODO: the old object isn't deleted and memory leaks, something preventing garbage collection?
        if old_tray:
            old_tray.hide()
        return UiTileTray(player_ui_tray_widget,
                          self._tile_bag.take(self._tray_size), self._tray_size, self)

    def show(self):
        for obj in [self._ui_board, self._player1_ui_tray, self._player2_ui_tray]:
            if obj:
                obj.show()

    def hide(self):
        for obj in [self._ui_board, self._player1_ui_tray, self._player2_ui_tray]:
            if obj:
                obj.hide()

    @staticmethod
    def _extract_tile_and_from(event):
        mime_data = event.mimeData()
        return mime_data.tile_object, mime_data.tile_object.parent

    def handle_drag_enter_event(self, event, pos_to):
        tile, pos_from = self._extract_tile_and_from(event)
        if pos_to.has_tile():
            event.ignore()
        else:
            event.accept()

    def handle_drop_event(self, event, pos_to):
        tile, pos_from = self._extract_tile_and_from(event)
        pos_from.remove_tile()
        pos_to.set_tile(tile)
        pos_to.tile.show()

        print("drop event on " + (str(pos_to.coo) if isinstance(pos_to, UiBoardPosition) else str(pos_to.index)))
        print("Tile: " + str(tile))
        print("From: " + str(pos_from))
        print("To: " + str(pos_to))

