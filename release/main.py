import sqlite3
import sys

from PyQt6.QtWidgets import QApplication, QTableWidgetItem, QMainWindow

from UI.mainUI import Ui_MainWindow
from UI.addEditCoffeeFormUI import Ui_Form


class AddWidget(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        con = sqlite3.connect("data/coffee.sqlite")
        cur = con.cursor()
        result = cur.execute("SELECT id FROM data").fetchall()

        for i in result:
            self.comboBox.insertItem(0, str(i[0]))

        self.pushButton.clicked.connect(self.action)

    def action(self):
        if self.add.isChecked():
            self.adding()
        else:
            self.editing()

    def editing(self):
        con = sqlite3.connect("data/coffee.sqlite")
        cur = con.cursor()
        id = self.comboBox.currentText()
        title = self.title.text()
        roasting = self.roasting.text()
        zerno = self.zerno.text()
        description = self.description.text()
        price = self.price.text()
        volume = self.volume.text()
        data_id = cur.execute(f"""SELECT * FROM data WHERE id = {id}""").fetchone()
        if title == '':
            title = data_id[1]
        if roasting == '':
            roasting = data_id[2]
        if zerno == '':
            zerno = data_id[3]
        if description == '':
            description = data_id[4]
        if price == '':
            price = data_id[5]
        if volume == '':
            volume = data_id[6]
        try:
            cur.execute("UPDATE data SET "
                        f"title = '{title}', "
                        f"GroundGrains = '{zerno}', "
                        f"DescriptionTaste = '{description}', "
                        f"price = {price}, "
                        f"DegreeRoasting = '{roasting}', "
                        f"PackingVolume = {volume} "
                        f"WHERE id = {id}")
        except Exception as e:
            self.statusBar().showMessage('Неверно заполнена форма')
            print(e)
        else:
            con.commit()
            self.parent().run()
            self.close()

    def adding(self):
        con = sqlite3.connect("data/coffee.sqlite")
        cur = con.cursor()
        new_id = cur.execute("SELECT max(id) FROM data").fetchone()[0] + 1
        title = self.title.text()
        roasting = self.roasting.text()
        zerno = self.zerno.text()
        description = self.description.text()
        if title == '' or roasting == '' or zerno == '' or description == '':
            self.statusBar().showMessage('Неверно заполнена форма')
            raise ValueError("Неверно заполнена форма")
        try:
            price = int(self.price.text())
            volume = int(self.volume.text())
            new_cofe = (new_id, title, roasting, zerno, description, price, volume)
            cur.execute("INSERT INTO data VALUES (?, ?, ?, ?, ?, ?, ?)", new_cofe)
        except Exception as e:
            self.statusBar().showMessage('Неверно заполнена форма')
        else:
            con.commit()
            self.parent().run()
            self.close()


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addEditCoffeeForm.clicked.connect(self.adding)
        self.run()

    def run(self):
        self.con = sqlite3.connect("data/coffee.sqlite")
        cur = self.con.cursor()
        result = cur.execute("""SELECT * FROM data""").fetchall()
        self.tableWidget.setColumnCount(len(result[0]))
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'Название сорта', 'Степень обжарки', 'Молотый/в зернах',
                                                    'Описание вкуса', 'Цена', 'Объем упаковки'])
        for i, row in enumerate(result):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def adding(self):
        self.add_form = AddWidget(self)
        self.add_form.show()

    def closeEvent(self, event):
        # При закрытии формы закроем и наше соединение
        # с базой данных
        self.con.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
