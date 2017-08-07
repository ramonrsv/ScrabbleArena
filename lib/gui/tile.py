from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QMimeData, Qt
from PyQt5.QtGui import QDrag
from PyQt5.QtWidgets import QPushButton

from lib.gui.position import GUIPosition
from lib.tile import Tile, TileTray


class GUITile(Tile, QPushButton):
    _width = 31
    _height = 31

    _default_stylesheet_background_color = "background-color: yellow"

    _font_point_size = 18

    def __init__(self, tile, parent=None):
        Tile.__init__(self, tile.letter, tile.is_blank())  # TODO: not really elegant
        if parent:
            QPushButton.__init__(self, parent)
        else:
            QPushButton.__init__(self)
        self._set_display_properties()

    def _set_display_properties(self):
        self.setFixedWidth(self._width)
        self.setFixedHeight(self._height)

        self.setStyleSheet(self._default_stylesheet_background_color)

        self.setText(self.letter if not self.is_blank() else '')
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setBold(True)
        font.setPointSize(self._font_point_size)
        self.setFont(font)

    def mouseMoveEvent(self, event):
        mime_data = QMimeData()
        mime_data.tile_object = self

        drag = QDrag(self)
        drag.setMimeData(mime_data)
        drag.exec_(Qt.MoveAction)


class GUITileTrayPosition(GUIPosition):
    _default_tray_position_color = QtGui.QColor(192, 192, 192)

    def __init__(self, parent, controller, geometry, tray_index, color=_default_tray_position_color):
        GUIPosition.__init__(self, parent, controller, geometry, x=1, y=tray_index, color=color)

    @property
    def index(self):
        return self.y


class GUITileTray(TileTray):
    _pos_width = 35
    _pos_height = 35
    _pos_spacing = 2

    def __init__(self, widget, tiles, size, controller):
        TileTray.__init__(self, size, [GUITile(tile) for tile in tiles])
        self._widget = widget
        self._controller = controller
        self._positions = self._generate_positions(self._widget, self._controller)
        for i in range(len(self.tiles())):
            self._positions[i].set_tile(self.tiles()[i])

    def _generate_positions(self, widget, controller):  # Needs TileTray to be initialized
        """Creates size UiPositions and sets their geometry"""
        temp_positions = []
        for i in range(self.size()):
            temp_positions.append(
                GUITileTrayPosition(parent=widget, controller=controller, tray_index=i + 1,
                                    geometry=QtCore.QRect((self._pos_width + self._pos_spacing) * i, 0,
                                                          self._pos_width, self._pos_height)))
        return temp_positions

    def show(self):
        for pos in self._positions:
            pos.show()

    def hide(self):
        for pos in self._positions:
            pos.hide()