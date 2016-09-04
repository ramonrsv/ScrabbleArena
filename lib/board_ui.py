from PyQt4 import QtCore, QtGui
from .position import PosProperty
from .gameplay import GameplayPosition, GameplayBoard


class UiPosition(GameplayPosition, QtGui.QWidget):

    __tile_type_color = {
        PosProperty.normal: QtGui.QColor(192, 192, 192),
        PosProperty.CENTER: QtGui.QColor(81, 0, 102),
        PosProperty.L2: QtGui.QColor(0, 102, 204),
        PosProperty.L3: QtGui.QColor(0, 204, 0),
        PosProperty.W2: QtGui.QColor(255, 51, 51),
        PosProperty.W3: QtGui.QColor(255, 128, 0)}

    def __init__(self, parent, geometry, x, y, pos_property=PosProperty.normal):
        QtGui.QWidget.__init__(self, parent)
        GameplayPosition.__init__(self, x, y, pos_property)
        self.geometry = geometry
        self.setGeometry(self.geometry)

    def draw(self):
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), self.__tile_type_color[self.property])
        self.setPalette(p)


class UiBoard(GameplayBoard):
    def __init__(self, widget, board_configuration):
        self.widget = widget  # Used in UiPosition object construction
        GameplayBoard.__init__(self, board_configuration)

    def _create_position_object(self, position):
        return UiPosition(self.widget, self._pos_geometry(position), position.x, position.y, position.property)

    def _pos_geometry(self, pos):
        """Will return the geometry of a UiPosition based on board_container (Board) and ui_parent (QWidget)"""
        pos_width = self.widget.width() / self.width
        pos_height = self.widget.height() / self.height
        rect_width = pos_width - 3  # -5 for debugging
        rect_height = pos_height - 3
        return QtCore.QRect((pos.x - 1) * pos_width, (pos.y - 1) * pos_height, rect_width, rect_height)

    def draw(self):
        for pos in self.positions():
            pos.draw()
