
### ---------------------------- ### IMPORTS ### ------ ###

import sys
from pathlib import Path
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QStyle, QPushButton
)



### ---------------------------- ### MAIN WINDOW ### ------ ###
# main window class to be used as window in main()
# contains initial settings
# contains methods
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        ### Window Settings ###
        self.setWindowTitle("Timer")
        self.resize(700, 420)

        ### Contents/Layout ###

        # Layout
        top_layout = QHBoxLayout()
        middle_layout = QHBoxLayout()
        bottom_layout = QHBoxLayout()

        # Add Content to Layout
        button = QPushButton()
        button.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        button.setIconSize(QSize(24, 24))
        bottom_layout.addWidget(button)

        # Root, Container
        root = QVBoxLayout()
        root.addLayout(top_layout)
        root.addLayout(middle_layout)
        root.addLayout(bottom_layout)
        container = QWidget()
        container.setLayout(root)
        self.setCentralWidget(container)

    ### Methods ###


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