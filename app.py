# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Programming\Python\sheduler\sheduler.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets, QtGui
from scripts import parse_student, parse_teacher


class MainWindow(QtWidgets.QMainWindow):
    widgets_stylesheet = "background: rgb(255, 255, 255);\n""font: 24pt \"MS Shell Dlg 2\";"
    days_stylesheet = "background: rgb(255, 255, 255);\n""font: 20pt \"MS Shell Dlg 2\";"

    def __init__(self):
        # Базовые настройки
        super(MainWindow, self).__init__()
        self.resize(1920, 1080)
        self.setStyleSheet("background-color: rgb(132, 8, 10)")

        self.CentralWidget = QtWidgets.QWidget(self)
        self.CentralWidget.setObjectName("CentralWidget")

        # Контейнеры с расписанием
        self.MondaySheduleLabel = QtWidgets.QLabel(self.CentralWidget)
        self.MondaySheduleLabel.setGeometry(QtCore.QRect(30, 350, 341, 350))
        self.MondaySheduleLabel.setText("")
        self.MondaySheduleLabel.setStyleSheet(self.days_stylesheet)

        self.TuesdaySheduleLabel = QtWidgets.QLabel(self.CentralWidget)
        self.TuesdaySheduleLabel.setGeometry(QtCore.QRect(400, 350, 341, 350))
        self.TuesdaySheduleLabel.setText("")
        self.TuesdaySheduleLabel.setStyleSheet(self.days_stylesheet)

        self.WednesdaySheduleLabel = QtWidgets.QLabel(self.CentralWidget)
        self.WednesdaySheduleLabel.setGeometry(QtCore.QRect(780, 350, 341, 350))
        self.WednesdaySheduleLabel.setText("")
        self.WednesdaySheduleLabel.setStyleSheet(self.days_stylesheet)

        self.ThursdaySheduleLabel = QtWidgets.QLabel(self.CentralWidget)
        self.ThursdaySheduleLabel.setGeometry(QtCore.QRect(1160, 350, 341, 350))
        self.ThursdaySheduleLabel.setText("")
        self.ThursdaySheduleLabel.setStyleSheet(self.days_stylesheet)

        self.FridaySheduleLabel = QtWidgets.QLabel(self.CentralWidget)
        self.FridaySheduleLabel.setGeometry(QtCore.QRect(1540, 350, 341, 350))
        self.FridaySheduleLabel.setText("")
        self.FridaySheduleLabel.setStyleSheet(self.days_stylesheet)

        self.Group = [
            self.MondaySheduleLabel,
            self.TuesdaySheduleLabel,
            self.WednesdaySheduleLabel,
            self.ThursdaySheduleLabel,
            self.FridaySheduleLabel
        ]

        # Радиокнопки
        self.StudentRadioButton = QtWidgets.QRadioButton(self.CentralWidget)
        self.StudentRadioButton.setGeometry(QtCore.QRect(430, 40, 271, 81))
        self.StudentRadioButton.setMinimumSize(QtCore.QSize(271, 1))
        self.StudentRadioButton.setStyleSheet(self.widgets_stylesheet)

        self.TeacherRadioButton = QtWidgets.QRadioButton(self.CentralWidget)
        self.TeacherRadioButton.setGeometry(QtCore.QRect(430, 170, 271, 81))
        self.TeacherRadioButton.setMinimumSize(QtCore.QSize(271, 0))
        self.TeacherRadioButton.setStyleSheet(self.widgets_stylesheet)

        # Надписи
        self.MondayLabel = QtWidgets.QLabel(self.CentralWidget)
        self.MondayLabel.setGeometry(QtCore.QRect(100, 290, 201, 51))
        self.MondayLabel.setStyleSheet(self.days_stylesheet)

        self.TuesdayLabel = QtWidgets.QLabel(self.CentralWidget)
        self.TuesdayLabel.setGeometry(QtCore.QRect(470, 290, 201, 51))
        self.TuesdayLabel.setStyleSheet(self.days_stylesheet)

        self.WednesdayLabel = QtWidgets.QLabel(self.CentralWidget)
        self.WednesdayLabel.setGeometry(QtCore.QRect(850, 290, 201, 51))
        self.WednesdayLabel.setStyleSheet(self.days_stylesheet)

        self.ThursdayLabel = QtWidgets.QLabel(self.CentralWidget)
        self.ThursdayLabel.setGeometry(QtCore.QRect(1230, 290, 201, 51))
        self.ThursdayLabel.setStyleSheet(self.days_stylesheet)

        self.FridayLabel = QtWidgets.QLabel(self.CentralWidget)
        self.FridayLabel.setGeometry(QtCore.QRect(1610, 290, 201, 51))
        self.FridayLabel.setStyleSheet(self.days_stylesheet)

        self.ClassLabel = QtWidgets.QLabel(self.CentralWidget)
        self.ClassLabel.setGeometry(QtCore.QRect(970, 40, 251, 81))
        self.ClassLabel.setStyleSheet(self.widgets_stylesheet)

        self.TeacherLabel = QtWidgets.QLabel(self.CentralWidget)
        self.TeacherLabel.setGeometry(QtCore.QRect(790, 170, 431, 81))
        self.TeacherLabel.setStyleSheet(self.widgets_stylesheet)

        # Окна ввода
        self.ClassValueLineEdit = QtWidgets.QLineEdit(self.CentralWidget)
        self.ClassValueLineEdit.setGeometry(QtCore.QRect(1260, 40, 81, 81))
        self.ClassValueLineEdit.setStyleSheet(self.widgets_stylesheet)
        self.ClassValueLineEdit.setText("")

        self.TeacherValueLineEdit = QtWidgets.QLineEdit(self.CentralWidget)
        self.TeacherValueLineEdit.setGeometry(QtCore.QRect(1260, 170, 231, 81))
        self.TeacherValueLineEdit.setStyleSheet(self.widgets_stylesheet)
        self.TeacherValueLineEdit.setText("")

        # Иконка школы
        self.SchoolIconLabel = QtWidgets.QLabel(self.CentralWidget)
        self.SchoolIconLabel.setGeometry(QtCore.QRect(100, 50, 191, 191))
        self.SchoolIconLabel.setStyleSheet("background: rgb(255, 255, 255);")
        self.Pixmap = QtGui.QPixmap(r'assets/images/icon.png')
        self.SchoolIconLabel.setPixmap(self.Pixmap)

        # Кнопка
        self.Button = QtWidgets.QPushButton(self.CentralWidget)
        self.Button.setGeometry(QtCore.QRect(1670, 100, 91, 91))
        self.Button.setStyleSheet(self.widgets_stylesheet)
        self.Button.clicked.connect(self.button_clicked)

        self.setCentralWidget(self.CentralWidget)

        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslate_ui()

        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Менеджер расписаний"))
        self.StudentRadioButton.setText(_translate("MainWindow", " Ученик"))
        self.TeacherRadioButton.setText(_translate("MainWindow", " Учитель"))
        self.MondayLabel.setText(_translate("MainWindow", "  Понедельник"))
        self.TuesdayLabel.setText(_translate("MainWindow", "      Вторник"))
        self.WednesdayLabel.setText(_translate("MainWindow", "        Среда"))
        self.ThursdayLabel.setText(_translate("MainWindow", "     Четверг"))
        self.FridayLabel.setText(_translate("MainWindow", "      Пятница"))
        self.ClassLabel.setText(_translate("MainWindow", " Введите класс: "))
        self.TeacherLabel.setText(_translate("MainWindow", " Введите фамилию учителя:"))
        self.Button.setText(_translate("MainWindow", "ОК"))

    def button_clicked(self):
        """ Функция нажатия кнопки """
        shedule = []
        try:
            if self.StudentRadioButton.isChecked():
                shedule = parse_student(self.ClassValueLineEdit.text())
            elif self.TeacherRadioButton.isChecked():
                shedule = parse_teacher(self.TeacherValueLineEdit.text())
            for label in self.Group:
                label.setText(shedule[self.Group.index(label)])
        except Exception:
            pass
