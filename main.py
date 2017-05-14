import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from main_window import Ui_MainWindow
from lib.main_manager_ui import UiManager


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = QMainWindow()

    ui_main_window = Ui_MainWindow()
    ui_main_window.setupUi(main_window)

    ui_manager = UiManager(ui_main_window)

    main_window.show()
    sys.exit(app.exec_())
