
### ---------------------------- ### IMPORTS ### ------ ###

import sys
from PySide6.QtWidgets import (
    QApplication
)
from main_window import MainWindow



### ---------------------------- ### MAIN ### ------ ###
def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Timer")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())



### ---------------------------- ### TEST ### ------ ###
if __name__=="__main__":
    main()