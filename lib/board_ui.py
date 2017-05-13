from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QLabel
from .position import PosProperty
from .gameplay import GameplayPosition, GameplayBoard


class UiPosition(GameplayPosition, QWidget):

    __tile_type_color = {
        PosProperty.normal: QtGui.QColor(192, 192, 192),
        PosProperty.CENTER: QtGui.QColor(81, 0, 102),
        PosProperty.L2: QtGui.QColor(0, 102, 204),
        PosProperty.L3: QtGui.QColor(0, 204, 0),
        PosProperty.W2: QtGui.QColor(255, 51, 51),
        PosProperty.W3: QtGui.QColor(255, 128, 0)}

    def __init__(self, parent, geometry, x, y, pos_property=PosProperty.normal):
        QWidget.__init__(self, parent)
        GameplayPosition.__init__(self, x, y, pos_property)
        self.geometry = geometry
        self.setGeometry(self.geometry)

    def draw(self):
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), self.__tile_type_color[self.property])
        self.setPalette(p)


class UiBoard(GameplayBoard):

    _pos_width = 35
    _pos_height = 35
    _pos_spacing = 2

    _pos_label_size = 30
    _pos_label_ps_w_b = (10, 75, True)  # PointSize, Weight, Bold

    def __init__(self, widget, x_label_widget, y_label_widget, board_configuration):
        self.widget = widget  # Used in UiPosition object construction
        GameplayBoard.__init__(self, board_configuration)
        self._x_label_widget = x_label_widget
        self._y_label_widget = y_label_widget
        self._x_labels = []
        self._y_labels = []

    def _create_position_object(self, position):
        return UiPosition(self.widget, self._pos_geometry(position), position.x, position.y, position.property)

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
            create_label((i, 0), self._x_labels, self._x_label_widget, UiPosition.x_to_alpha(i))
            create_label((0, i), self._y_labels, self._y_label_widget, str(i))

    def _draw_board(self):
        for pos in self.positions():
            pos.draw()

    def initialize_display(self):
        self._draw_labels()
        self._draw_board()

    def update_display(self):
        self._draw_board()
