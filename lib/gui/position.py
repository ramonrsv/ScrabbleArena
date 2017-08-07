from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget

from lib.position import Position, ClassicPositionAttribute as PosAttribute


class GUIPosition(Position, QWidget):
    __default_color = QtGui.QColor(192, 192, 192)

    def __init__(self, parent, controller, geometry, x, y, pos_attribute=PosAttribute.normal, color=__default_color):
        Position.__init__(self, x, y, pos_attribute)
        QWidget.__init__(self, parent)
        self.setAcceptDrops(True)  # Allow drag and drop
        self.controller = controller  # Allow callbacks to controller object on drag and drop
        self.geometry = geometry
        self.setGeometry(self.geometry)
        self._color = color
        self._set_display_properties()

    def _set_display_properties(self):
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), self._color)
        self.setPalette(p)

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

    def set_tile(self, tile):
        Position.set_tile(self, tile)
        self.tile.setParent(self)
        self.tile.move(self.rect().center() - self.tile.rect().center())  # Center tile in space
        self.tile.parent = self
