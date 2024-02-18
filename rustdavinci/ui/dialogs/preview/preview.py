import os

from PyQt6.QtCore import QPoint, Qt
from PyQt6.QtGui import QMouseEvent, QPixmap, QResizeEvent
from PyQt6.QtWidgets import QDialog
from PIL import Image, ImageQt

from rustdavinci.ui.dialogs.preview.previewui import Ui_PreviewDialog


class Preview(QDialog):
    def __init__(self, parent, canvas_image: Image):
        QDialog.__init__(self, parent)
        self.ui = Ui_PreviewDialog()
        self.ui.setupUi(self)
        self.setWindowTitle('Preview')
        self.parent = parent
        self.old_position = None  # point of origin for dragged
        self.is_dragging = False  # if window is currently being dragged
        self.wanted_aspect_ratio = Qt.AspectRatioMode.KeepAspectRatio
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        # self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        # self.setWindowOpacity(0.9)
        self.setAttribute(Qt.WidgetAttribute.WA_StaticContents)
        self.setAttribute(Qt.WidgetAttribute.WA_AlwaysStackOnTop)
        self.ui.imagePreviewLabel.mouseMoveEvent = self.mouseMoveEvent
        self.ui.imagePreviewLabel.mousePressEvent = self.mousePressEvent
        self.ui.imagePreviewLabel.mouseReleaseEvent = self.mouseReleaseEvent
        self.window().resizeEvent = self.resizeEvent
        self.image = QPixmap(ImageQt.toqpixmap(canvas_image))
        self.ui.imagePreviewLabel.setScaledContents(False)
        resizedImage = self.image.scaled(400, 400, Qt.AspectRatioMode.KeepAspectRatio)
        self.resize(resizedImage.width(), resizedImage.height())
        self.ui.imagePreviewLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.ui.imagePreviewLabel.setPixmap(resizedImage)
        self.ui.aspectratioCheckBox.stateChanged.connect(self.update_aspect_ratio)
        self.ui.doneButton.clicked.connect(self.close)

    def update_aspect_ratio(self, state: Qt.CheckState):
        if state == Qt.CheckState.Checked.value:
            self.wanted_aspect_ratio = Qt.AspectRatioMode.KeepAspectRatio
            self.ui.imagePreviewLabel.setScaledContents(False)
        else:
            self.wanted_aspect_ratio = Qt.AspectRatioMode.IgnoreAspectRatio
            self.ui.imagePreviewLabel.setScaledContents(True)
        self.rescalePixmap()

    def rescalePixmap(self):
        new = self.image.scaled(
            self.ui.imagePreviewLabel.width(),
            self.ui.imagePreviewLabel.height(),
            self.wanted_aspect_ratio,
            Qt.TransformationMode.FastTransformation,
        )
        self.ui.imagePreviewLabel.setPixmap(new)

    def resizeEvent(self, event: QResizeEvent | None) -> None:
        self.rescalePixmap()
        event.accept()
        return super().resizeEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent):
        self.old_position = None
        self.is_dragging = False
        event.accept()

    def mousePressEvent(self, event: QMouseEvent):
        self.old_position = event.globalPosition().toPoint()
        self.is_dragging = True
        event.accept()

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.old_position is None:
            return
        if not self.is_dragging:
            return
        delta = QPoint(event.globalPosition().toPoint() - self.old_position)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.old_position = event.globalPosition().toPoint()
        event.accept()
