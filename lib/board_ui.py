from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QLabel
from .position import PosProperty
from .gameplay import GameplayPosition, GameplayBoard, TileTray
from .tile import Tile


class UiTile(Tile, QWidget):
    _width = 25
    _height = 25

    def __init__(self, parent, tile):
        QWidget.__init__(self, parent)
        Tile.__init__(self, tile.letter, tile.isblank())  # TODO: not really elegant


class UiBasicPosition(QWidget):
    __default_color = QtGui.QColor(192, 192, 192)

    def __init__(self, parent, geometry, color=__default_color):
        QWidget.__init__(self, parent)
        self.geometry = geometry
        self.setGeometry(self.geometry)
        self._color = color

    def draw(self):
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), self._color)
        self.setPalette(p)


class UiBoardPosition(GameplayPosition, UiBasicPosition):
    __pos_type_color = {
        PosProperty.normal: QtGui.QColor(192, 192, 192),
        PosProperty.CENTER: QtGui.QColor(81, 0, 102),
        PosProperty.L2: QtGui.QColor(0, 102, 204),
        PosProperty.L3: QtGui.QColor(0, 204, 0),
        PosProperty.W2: QtGui.QColor(255, 51, 51),
        PosProperty.W3: QtGui.QColor(255, 128, 0)}

    def __init__(self, parent, geometry, x, y, pos_property=PosProperty.normal):
        GameplayPosition.__init__(self, x, y, pos_property)
        UiBasicPosition.__init__(self, parent, geometry, self.__pos_type_color[self.property])


class UiTrayPosition(UiBasicPosition):
    __emptry_tray_position_color = QtGui.QColor(192, 192, 192)

    def __init__(self, parent, geometry, color=__emptry_tray_position_color):
        UiBasicPosition.__init__(self, parent, geometry, color)


class UiTileTray(TileTray):
    _pos_width = 35
    _pos_height = 35
    _pos_spacing = 2

    def __init__(self, widget, tiles, size):
        TileTray.__init__(self, tiles, size)
        self._widget = widget
        self._positions = self._generate_positions()

    def _generate_positions(self):  # Needs TileTray and self._widget to be initialized
        """Creates size UiPositions and sets their geometry"""
        temp_positions = []
        for i in range(self.size):
            temp_positions.append(
                UiTrayPosition(self._widget, QtCore.QRect((self._pos_width + self._pos_spacing) * i, 0,
                                                          self._pos_width, self._pos_height)))
        return temp_positions

    def initialize_display(self):
        for pos in self._positions:
            pos.draw()


class UiBoard(GameplayBoard):
    _pos_width = 35
    _pos_height = 35
    _pos_spacing = 2

    _pos_label_size = 30
    _pos_label_ps_w_b = (10, 75, True)  # PointSize, Weight, Bold

    def __init__(self, widget, x_label_widget, y_label_widget, board_configuration):
        self.widget = widget  # Used in BoardPosition object construction, in GameplayBoard construction
        GameplayBoard.__init__(self, board_configuration)
        self._x_label_widget = x_label_widget
        self._y_label_widget = y_label_widget
        self._x_labels = []
        self._y_labels = []

    def _create_position_object(self, position):
        return UiBoardPosition(self.widget, self._pos_geometry(position), position.x, position.y, position.property)

    def _pos_geometry(self, pos):
        """Will return the geometry of a UiPosition based on board_container (Board) and ui_parent (QWidget)"""
        return QtCore.QRect((pos.x - 1) * self._pos_width + self._pos_spacing * pos.x,
                            (pos.y - 1) * self._pos_height + self._pos_spacing * pos.y,
                            self._pos_width, self._pos_height)

    def _label_geometry(self, pos):
        """Takes pos in form (x,0) for x_axis, (0,y) for y_axis"""
        return QtCore.QRect(
            (pos[0] - 1) * self._pos_width + self._pos_spacing * pos[0] +
            ((self._pos_width - self._pos_label_size) / 2) if pos[0] else 0,
            (pos[1] - 1) * self._pos_height + self._pos_spacing * pos[1] +
            ((self._pos_height - self._pos_label_size) / 2) if pos[1] else 0,
            self._pos_label_size, self._pos_label_size)

    def _draw_labels(self):
        def create_label(coo, storage, parent, text):
            l = QLabel(parent)
            l.setGeometry(self._label_geometry(coo))
            l.setText(text)
            l.setAlignment(QtCore.Qt.AlignCenter)
            font = QtGui.QFont()
            font.setPointSize(self._pos_label_ps_w_b[0])
            font.setWeight(self._pos_label_ps_w_b[1])
            font.setBold(self._pos_label_ps_w_b[2])
            l.setFont(font)
            storage.append(l)

        for i in range(1, self.width + 1):
            create_label((i, 0), self._x_labels, self._x_label_widget, UiBoardPosition.x_to_alpha(i))
            create_label((0, i), self._y_labels, self._y_label_widget, str(i))

    def _draw_board(self):
        for pos in self.positions():
            pos.draw()

    def initialize_display(self):
        self._draw_labels()
        self._draw_board()

    def update_display(self):
        self._draw_board()
