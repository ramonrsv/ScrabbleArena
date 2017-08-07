from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QLabel

from lib.gui.position import GUIPosition
from lib.board import Board
from lib.position import ClassicPositionAttribute as PosAttribute


class GUIBoardPosition(GUIPosition):
    __pos_type_color = {
        PosAttribute.normal: QtGui.QColor(192, 192, 192),
        PosAttribute.CENTER: QtGui.QColor(81, 0, 102),
        PosAttribute.L2: QtGui.QColor(0, 102, 204),
        PosAttribute.L3: QtGui.QColor(0, 204, 0),
        PosAttribute.W2: QtGui.QColor(255, 51, 51),
        PosAttribute.W3: QtGui.QColor(255, 128, 0)}

    def __init__(self, parent, controller, geometry, x, y, pos_attribute=PosAttribute.normal):
        GUIPosition.__init__(self, parent, controller, geometry, x, y,
                             pos_attribute, self.__pos_type_color[pos_attribute])


class GUIBoard(Board):
    _pos_width = 35
    _pos_height = 35
    _pos_spacing = 2

    _pos_label_size = 30
    _pos_label_ps_w_b = (10, 75, True)  # PointSize, Weight, Bold

    def __init__(self, main_board_widget, x_label_widget, y_label_widget, board_configuration, controller):
        # main_board_widget and _controller in BoardPosition object construction, in GameplayBoard construction
        self.controller = controller
        self._main_board_widget = main_board_widget
        Board.__init__(self, board_configuration)
        self._x_label_widget = x_label_widget
        self._y_label_widget = y_label_widget
        self._x_labels = []
        self._y_labels = []
        self._set_display_properties()

    def _factory_make_position(self, position):
        return GUIBoardPosition(self._main_board_widget, self.controller,
                                self._pos_geometry(position), position.x, position.y, position.attribute)

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
            create_label((i, 0), self._x_labels, self._x_label_widget, GUIBoardPosition.x_to_alpha(i))
            create_label((0, i), self._y_labels, self._y_label_widget, str(i))

    def _set_display_properties(self):
        self._draw_labels()

    def show(self):
        for obj_list in [self.positions(), self._x_labels, self._y_labels]:
            for obj in obj_list:
                obj.show()

    def hide(self):
        for obj_list in [self.positions(), self._x_labels, self._y_labels]:
            for obj in obj_list:
                obj.hide()
