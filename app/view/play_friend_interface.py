from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from qfluentwidgets import PushButton

from app.widgets.board_widget import BoardWidget


class PlayFriendInterface(QWidget):
    def __init__(self, text, parent):
        super().__init__(parent)
        self.setMinimumSize(600, 400)
        self.setMouseTracking(True)
        self.setObjectName(text.replace(' ', '-'))

        self.board_widget = BoardWidget(text, self)

        self.main_layout = QVBoxLayout()
        self.left_layout = QHBoxLayout()

        self.restart_button = PushButton(self)
        self.restart_button.setText("Restart")
        self.restart_button.clicked.connect(self.board_widget.onRestart)
        self.left_layout.addWidget(self.restart_button)

        self.undo_button = PushButton(self)
        self.undo_button.setText("Undo")
        self.undo_button.clicked.connect(self.board_widget.onUndo)
        self.left_layout.addWidget(self.undo_button)

        self.resign_button = PushButton(self)
        self.resign_button.setText("Resign")
        self.resign_button.clicked.connect(self.board_widget.onResign)
        self.left_layout.addWidget(self.resign_button)

        self.save_button = PushButton(self)
        self.save_button.setText("Save")
        self.save_button.clicked.connect(self.board_widget.onSave)
        self.left_layout.addWidget(self.save_button)

        self.main_layout.addWidget(self.board_widget)
        self.main_layout.addLayout(self.left_layout)

        self.setLayout(self.main_layout)
