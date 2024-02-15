#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt6 import QtCore
from PyQt6 import QtWidgets

import sys

from rustdavinci.ui.views.main import MainWindow


def run():

    # Set some application settings for QSettings
    QtCore.QCoreApplication.setOrganizationName("RustDaVinci")
    QtCore.QCoreApplication.setApplicationName("RustDaVinci")

    # Setup the application and start
    app = QtWidgets.QApplication(sys.argv)

    main = MainWindow()
    main.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    run()
