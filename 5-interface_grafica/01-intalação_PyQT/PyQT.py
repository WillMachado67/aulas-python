# PyQT é um toolkit desenvolvido em C++ utilizando vários programas para
# criação de apicativos GUI (Interface Gráfica). Também inclui diversas
# funcionalidade, como: acesso a base de dados, threads, comunicação de rede,
# etc...

# pip install PyQt5

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtWidgets import QWidget, QGridLayout


class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.btn = QPushButton('Texto botão')
        self.btn.setStyleSheet('font-size: 40px')
        self.grid.addWidget(self.btn, 0, 0, 1, 1)
        # grid = linha, coluna, qtd linhas, qtd colunas
        self.btn.clicked.connect(lambda: print('Ola mundo!'))
        self.setCentralWidget(self.cw)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec()
