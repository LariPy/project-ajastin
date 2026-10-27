import sys
from PySide6.QtCore import QTimer, Qt
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
)


class TimerWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Timer")

        self.seconds = 0

        # QTimer fires its timeout signal every 1000 ms
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.tick)

        self.label = QLabel("00:00")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 48px;")

        self.start_btn = QPushButton("Start")
        self.stop_btn = QPushButton("Stop")
        self.reset_btn = QPushButton("Reset")

        self.start_btn.clicked.connect(self.timer.start)
        self.stop_btn.clicked.connect(self.timer.stop)
        self.reset_btn.clicked.connect(self.reset)

        buttons = QHBoxLayout()
        buttons.addWidget(self.start_btn)
        buttons.addWidget(self.stop_btn)
        buttons.addWidget(self.reset_btn)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addLayout(buttons)

    def tick(self):
        self.seconds += 1
        self.update_label()

    def reset(self):
        self.timer.stop()
        self.seconds = 0
        self.update_label()

    def update_label(self):
        minutes, secs = divmod(self.seconds, 60)
        self.label.setText(f"{minutes:02d}:{secs:02d}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TimerWindow()
    window.show()
    sys.exit(app.exec())