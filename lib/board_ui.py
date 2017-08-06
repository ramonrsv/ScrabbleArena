from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton
from PyQt5.QtCore import QMimeData, Qt
from PyQt5.QtGui import QDrag
from .position import ClassicPositionAttribute as PosAttribute
from .gameplay import GameplayPosition, GameplayBoard, TileTray
from .tile_bag import Tile


class UiTile(Tile, QPushButton):
    _width = 31
    _height = 31
    _font_point_size = 18

    def __init__(self, tile, parent=None):
        if parent:
            QPushButton.__init__(self, parent)
        else:
            QPushButton.__init__(self)
        Tile.__init__(self, tile.letter, tile.is_blank())  # TODO: not really elegant
        self._set_display_properties()

    def _set_display_properties(self):
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)
        self.setText(self.letter if not self.is_blank() else '')
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setBold(True)
        font.setPointSize(self._font_point_size)
        self.setFont(font)

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def mouseMoveEvent(self, event):
        mime_data = QMimeData()
        mime_data.tile_object = self

        drag = QDrag(self)
        drag.setMimeData(mime_data)
        drag.exec_(Qt.MoveAction)


class UiBasicPosition(QWidget):
    __default_color = QtGui.QColor(192, 192, 192)

    def __init__(self, parent, controller, geometry, color=__default_color):
        QWidget.__init__(self, parent)
        self.setAcceptDrops(True)  # Allow drag and drop
        self.controller = controller  # Allow callbacks to controller object on drag and drop
        self.geometry = geometry
        self.setGeometry(self.geometry)
        self._color = color
        self._tile = None  # To hold tile object placed in this position
        self._set_display_properties()

    def _set_display_properties(self):
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), self._color)
        self.setPalette(p)

    @property
    def tile(self):
        return self._tile

    @tile.setter
    def tile(self, tile):
        if not isinstance(tile, UiTile):
            raise TypeError("tile has to be a UiTile object")
        if self._tile:
            raise RuntimeError("position already has a tile object")
        self._tile = tile
        self.tile.setParent(self)
        self.tile.move(self.rect().center() - self.tile.rect().center())  # Center tile in space
        self.tile.parent = self  # Parent UiPosition used for determining 'from' in move events

    def has_tile(self):
        return True if self.tile else False

    def set_tile(self, tile):
        self.tile = tile

    def remove_tile(self):
        if not self.tile:
            raise RuntimeError("position does not currently have a tile")
        self._tile = None

    def dragEnterEvent(self, event):
        self.controller.handle_drag_enter_event(event, self)

    def dropEvent(self, event):
        self.controller.handle_drop_event(event, self)

    def show(self):
        QWidget.show(self)
        if self.has_tile():
            self.tile.show()

    def hide(self):
        QWidget.hide(self)
        if self.has_tile():
            self.tile.hide()


class UiTrayPosition(UiBasicPosition):
    __emptry_tray_position_color = QtGui.QColor(192, 192, 192)

    def __init__(self, parent, controller, geometry, tray_index, color=__emptry_tray_position_color):
        UiBasicPosition.__init__(self, parent, controller, geometry, color)
        self._tray_index = tray_index

    @property
    def index(self):
        return self._tray_index


class UiBoardPosition(GameplayPosition, UiBasicPosition):
    __pos_type_color = {
        PosAttribute.normal: QtGui.QColor(192, 192, 192),
        PosAttribute.CENTER: QtGui.QColor(81, 0, 102),
        PosAttribute.L2: QtGui.QColor(0, 102, 204),
        PosAttribute.L3: QtGui.QColor(0, 204, 0),
        PosAttribute.W2: QtGui.QColor(255, 51, 51),
        PosAttribute.W3: QtGui.QColor(255, 128, 0)}

    def __init__(self, parent, controller, geometry, x, y, pos_attribute=PosAttribute.normal):
        GameplayPosition.__init__(self, x, y, pos_attribute)
        UiBasicPosition.__init__(self, parent, controller, geometry, self.__pos_type_color[self.attribute])


class UiTileTray(TileTray):
    _pos_width = 35
    _pos_height = 35
    _pos_spacing = 2

    def __init__(self, widget, tiles, size, controller):
        TileTray.__init__(self, [UiTile(tile) for tile in tiles], size)
        self._widget = widget
        self._controller = controller
        self._positions = self._generate_positions(self._widget, self._controller)
        for i in range(len(self.tiles)):
            self._positions[i].set_tile(self.tiles[i])

    def _generate_positions(self, widget, controller):  # Needs TileTray to be initialized
        """Creates size UiPositions and sets their geometry"""
        temp_positions = []
        for i in range(self.size):
            temp_positions.append(
                UiTrayPosition(parent=widget, controller=controller, tray_index=i + 1,
                               geometry=QtCore.QRect((self._pos_width + self._pos_spacing) * i, 0,
                                                     self._pos_width, self._pos_height)))
        return temp_positions

    def show(self):
        for pos in self._positions:
            pos.show()

    def hide(self):
        for pos in self._positions:
            pos.hide()


class UiBoard(GameplayBoard):
    _pos_width = 35
    _pos_height = 35
    _pos_spacing = 2

    _pos_label_size = 30
    _pos_label_ps_w_b = (10, 75, True)  # PointSize, Weight, Bold

    def __init__(self, main_board_widget, x_label_widget, y_label_widget, board_configuration, controller):
        # main_board_widget and _controller in BoardPosition object construction, in GameplayBoard construction
        self.controller = controller
        self._main_board_widget = main_board_widget
        GameplayBoard.__init__(self, board_configuration)
        self._x_label_widget = x_label_widget
        self._y_label_widget = y_label_widget
        self._x_labels = []
        self._y_labels = []
        self._set_display_properties()

    def _factory_make_position(self, position):
        return UiBoardPosition(self._main_board_widget, self.controller,
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
            create_label((i, 0), self._x_labels, self._x_label_widget, UiBoardPosition.x_to_alpha(i))
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
