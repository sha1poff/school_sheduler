# Импорт библиотек
from app import MainWindow
from PyQt5 import QtWidgets
import sys


# Приложение
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


# Запуск
if __name__ == '__main__':
    main()
