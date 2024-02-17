#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QDialog, QListWidgetItem

from rustdavinci.lib.color_functions import blend_alpha, rgb_to_hex
from rustdavinci.lib.rustPaletteData import rust_palette
from rustdavinci.ui.dialogs.colors.colorsui import Ui_ColorsUI


class Colors(QDialog):

    def __init__(self, parent):
        """ init Colors module """
        QDialog.__init__(self, parent)
        self.ui = Ui_ColorsUI()
        self.ui.setupUi(self)
        self.setWindowTitle("Colors")
        self.parent = parent
        self.populate_list()


    # todo: refactor
    def populate_list(self):
        """ Populates the colors list """
        for i, color in enumerate(rust_palette):
            hex = rgb_to_hex(color)
            i = QListWidgetItem(str(i) + "\t" + str(hex))
            i.setBackground(QColor(color[0], color[1], color[2]))
            if (color[0]*0.299 + color[1]*0.587 + color[2]*0.114) > 186:
                i.setForeground(QColor(0, 0, 0))
            else:
                i.setForeground(QColor(255, 255, 255))
            self.ui.colors_ListWidget.addItem(i)


        for offset, opacity_level in enumerate((0.25, 0.50, 0.75)):
            for i, color in enumerate(rust_palette):
                idx = i+64*(offset+1)
                color = blend_alpha(color, (255,255,255), opacity_level)
                hex = rgb_to_hex(color)
                item = QListWidgetItem(str(idx) + "\t" + str(hex))
                item.setBackground(QColor(color[0], color[1], color[2]))
                if (color[0]*0.299 + color[1]*0.587 + color[2]*0.114) > 186:
                    item.setForeground(QColor(0, 0, 0))
                else:
                    item.setForeground(QColor(255, 255, 255))
                self.ui.colors_ListWidget.addItem(item)
                if idx % 63 == 0:
                    print(hex)
