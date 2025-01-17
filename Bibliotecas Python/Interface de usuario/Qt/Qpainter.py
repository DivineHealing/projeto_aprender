import sys
from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QPainter, QColor, QFont
from PyQt6.QtCore import Qt
        
class Teste(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        self.text = "Nosso primeiro teste"

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("Desenhando...")
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawText(qp)
        qp.end()

    def drawText(self, qp):
        qp.setPen(QColor(168, 34, 3))
        qp.setFont(QFont('Decorative', 10))
        # Desenhando o texto na posição (20, 50)
        qp.drawText(20, 50, self.text)
        
def main():
    app = QApplication(sys.argv)
    ex = Teste()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
