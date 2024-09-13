#####################################
#                                   #
#  @author      : 00xWolf           #
#    GitHub    : @mmsaeed509       #
#    Developer : Mahmoud Mohamed   #
#  﫥  Copyright : Exodia OS         #
#                                   #
#####################################

import sys
import os
from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtGui import QPainter, QColor, QRegion, QPolygon, QPen, QFont, QFontDatabase
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class CustomButton(QPushButton):
    def __init__(self, text, points, x, y, width, height, color="#121212", border_color="#00B0C8", border_thickness=3, parent=None):
        super().__init__(text, parent)
        self.predator_font = None
        self.setFixedSize(200, 100)  # Set the fixed size for the button
        self.polygon = QPolygon(points)
        self.color = color
        self.border_color = border_color
        self.border_thickness = border_thickness
        self.setGeometry(QRect(x, y, width, height))  # Set the geometry of the button
        self.setAttribute(Qt.WA_TranslucentBackground)  # Make the button background transparent
        self.setMask(QRegion(self.polygon))  # Apply the mask to create the custom shape

        # Load custom fonts
        self.loadPredatorFont()

    def loadPredatorFont(self):
        # Load the font from the Fonts directory
        font_path = os.path.join(os.path.dirname(__file__), '../Fonts', 'Squares-Bold.otf')
        font_id = QFontDatabase.addApplicationFont(font_path)
        if font_id == -1:
            print("Failed to load Predator font.")
        else:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            self.predator_font = QFont(font_family, 12, QFont.Bold)

    def paintEvent(self, event):
        # Handle custom painting of the button
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw the background of the button
        painter.setBrush(QColor(self.color))
        painter.setPen(Qt.NoPen)
        painter.drawPolygon(self.polygon)

        # Draw the border of the button
        pen = QPen(QColor(self.border_color))
        pen.setWidth(self.border_thickness)
        painter.setPen(pen)
        painter.drawPolygon(self.polygon)

        # Draw the text with the Predator font if available
        pen = QPen(QColor("#acacac"))
        painter.setPen(pen)
        if self.predator_font:
            painter.setFont(self.predator_font)
        painter.drawText(self.rect(), Qt.AlignCenter, self.text())

class CustomButtonPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(200, 400)  # Adjust the size of the main window as needed
        self.setGeometry(100, 200, 400, 400)
        self.setAttribute(Qt.WA_TranslucentBackground) # Make the background transparent

        # Set up a layout for the panel with zero spacing
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)

        # Define the shape points, positions, and sizes for each button
        buttons_config = [
            # Welcome Button
            {
                'text': 'Welcome',
                'points': [
                    QPoint(200, 20),
                    QPoint(200, 80),
                    QPoint(0, 80),
                    QPoint(0, 45),
                    QPoint(30, 20)
                ],
                'x': 50, 'y': 50, 'width': 200, 'height': 100
            },
            # Keybinding Button
            {
                'text': 'Keybinding',
                'points': [
                    QPoint(200, 20),
                    QPoint(200, 80),
                    QPoint(0, 80),
                    QPoint(0, 45),
                    QPoint(30, 20)
                ],
                'x': 50, 'y': 160, 'width': 200, 'height': 100
            },
            # Tips Button
            {
                'text': 'Tips',
                'points': [
                    QPoint(200, 20),
                    QPoint(200, 80),
                    QPoint(0, 80),
                    QPoint(0, 45),
                    QPoint(30, 20)
                ],
                'x': 50, 'y': 270, 'width': 200, 'height': 100
            },
            # Setting Button
            {
                'text': 'Setting',
                'points': [
                    QPoint(200, 20),
                    QPoint(200, 80),
                    QPoint(0, 80),
                    QPoint(0, 45),
                    QPoint(30, 20)
                ],
                'x': 50, 'y': 380, 'width': 200, 'height': 100
            },
            # Developers Button
            {
                'text': 'Developers',
                'points': [
                    QPoint(200, 20),
                    QPoint(200, 80),
                    QPoint(0, 80),
                    QPoint(0, 45),
                    QPoint(30, 20)
                ],
                'x': 50, 'y': 490, 'width': 200, 'height': 100
            }
        ]

        # Create custom-shaped buttons with the provided shapes and labels
        for config in buttons_config:
            button = CustomButton(
                text=config['text'],
                points=config['points'],
                x=config['x'],
                y=config['y'],
                width=config['width'],
                height=config['height']
            )
            # Add the button to the layout
            self.layout().addWidget(button)


# Main application setup
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CustomButtonPanel()
    window.show()
    sys.exit(app.exec_())