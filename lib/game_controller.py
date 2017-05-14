from .board_ui import UiTile, UiBasicPosition, UiBoardPosition, UiTrayPosition
from .board_ui import UiBoard, UiTileTray
from .tile import Tile, TileBag


class GameController:
    def __init__(self, tile_distribution, board_configuration, tray_size,
                 main_board_widget, x_label_widget, y_label_widget, player1_tray_widget, player2_tray_widget):
        self._letter_distribution = tile_distribution.letter_distribution
        self._tile_distribution = tile_distribution
        self._board_configuration = board_configuration
        self._tray_size = tray_size
        Tile.set_letter_distribution(self._letter_distribution)

        self._main_board_widget = main_board_widget
        self._x_label_widget = x_label_widget
        self._y_label_widget = y_label_widget
        self._player1_tray_widget = player1_tray_widget
        self._player2_tray_widget = player2_tray_widget

        self._ui_board = UiBoard(self._main_board_widget, self._x_label_widget, self._y_label_widget,
                                 self._board_configuration, self)
        self._tile_bag = TileBag(self._tile_distribution)
        self._player1_ui_tray = UiTileTray(self._player1_tray_widget, self._tile_bag.take(tray_size), tray_size, self)
        self._player2_ui_tray = UiTileTray(self._player2_tray_widget, self._tile_bag.take(tray_size), tray_size, self)

        self._ui_board.update_display()
        self._player1_ui_tray.update_display()
        self._player2_ui_tray.update_display()

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

