# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(822, 348)
        self.add = QtWidgets.QRadioButton(parent=Form)
        self.add.setGeometry(QtCore.QRect(20, 60, 161, 17))
        self.add.setStyleSheet("color: rgb(0, 0, 0);\n"
                               "font: 12pt \"MS UI Gothic\";\n"
                               "background-color: rgb(170, 158, 146);")
        self.add.setChecked(True)
        self.add.setObjectName("add")
        self.edit = QtWidgets.QRadioButton(parent=Form)
        self.edit.setGeometry(QtCore.QRect(20, 100, 161, 17))
        self.edit.setStyleSheet("color: rgb(0, 0, 0);\n"
                                "font: 12pt \"MS UI Gothic\";\n"
                                "background-color: rgb(170, 158, 146);")
        self.edit.setObjectName("edit")
        self.title = QtWidgets.QLineEdit(parent=Form)
        self.title.setGeometry(QtCore.QRect(370, 60, 441, 31))
        self.title.setStyleSheet("color: rgb(0, 0, 0);\n"
                                 "font: 12pt \"Myanmar Text\";\n"
                                 "background-color: rgb(170, 158, 146);")
        self.title.setObjectName("title")
        self.roasting = QtWidgets.QLineEdit(parent=Form)
        self.roasting.setGeometry(QtCore.QRect(370, 100, 441, 31))
        self.roasting.setStyleSheet("color: rgb(0, 0, 0);\n"
                                    "font: 12pt \"Myanmar Text\";\n"
                                    "background-color: rgb(170, 158, 146);")
        self.roasting.setObjectName("roasting")
        self.zerno = QtWidgets.QLineEdit(parent=Form)
        self.zerno.setGeometry(QtCore.QRect(370, 140, 441, 31))
        self.zerno.setStyleSheet("color: rgb(0, 0, 0);\n"
                                 "font: 12pt \"Myanmar Text\";\n"
                                 "background-color: rgb(170, 158, 146);")
        self.zerno.setObjectName("zerno")
        self.description = QtWidgets.QLineEdit(parent=Form)
        self.description.setGeometry(QtCore.QRect(370, 180, 441, 31))
        self.description.setStyleSheet("color: rgb(0, 0, 0);\n"
                                       "font: 12pt \"Myanmar Text\";\n"
                                       "background-color: rgb(170, 158, 146);")
        self.description.setObjectName("description")
        self.price = QtWidgets.QLineEdit(parent=Form)
        self.price.setGeometry(QtCore.QRect(370, 220, 441, 31))
        self.price.setStyleSheet("color: rgb(0, 0, 0);\n"
                                 "font: 12pt \"Myanmar Text\";\n"
                                 "background-color: rgb(170, 158, 146);")
        self.price.setObjectName("price")
        self.volume = QtWidgets.QLineEdit(parent=Form)
        self.volume.setGeometry(QtCore.QRect(370, 260, 441, 31))
        self.volume.setStyleSheet("color: rgb(0, 0, 0);\n"
                                  "font: 12pt \"Myanmar Text\";\n"
                                  "background-color: rgb(170, 158, 146);")
        self.volume.setObjectName("volume")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(-10, 10, 841, 21))
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
                                 "font: 16pt \"MS UI Gothic\";\n"
                                 "background-color: rgb(170, 158, 146);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(230, 60, 131, 31))
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "font: 12pt \"Myanmar Text\";\n"
                                   "background-color: rgb(170, 158, 146);")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(230, 100, 131, 31))
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "font: 12pt \"Myanmar Text\";\n"
                                   "background-color: rgb(170, 158, 146);")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(230, 140, 131, 31))
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "font: 11pt \"Myanmar Text\";\n"
                                   "background-color: rgb(170, 158, 146);")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=Form)
        self.label_5.setGeometry(QtCore.QRect(230, 180, 131, 31))
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "font: 12pt \"Myanmar Text\";\n"
                                   "background-color: rgb(170, 158, 146);")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=Form)
        self.label_6.setGeometry(QtCore.QRect(230, 220, 131, 31))
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "font: 12pt \"Myanmar Text\";\n"
                                   "background-color: rgb(170, 158, 146);")
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=Form)
        self.label_7.setGeometry(QtCore.QRect(230, 260, 131, 31))
        self.label_7.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "font: 12pt \"Myanmar Text\";\n"
                                   "background-color: rgb(170, 158, 146);")
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.comboBox = QtWidgets.QComboBox(parent=Form)
        self.comboBox.setGeometry(QtCore.QRect(20, 180, 161, 21))
        self.comboBox.setStyleSheet("color: rgb(0, 0, 0);\n"
                                    "font: 12pt \"Myanmar Text\";\n"
                                    "background-color: rgb(170, 158, 146);")
        self.comboBox.setObjectName("comboBox")
        self.label_8 = QtWidgets.QLabel(parent=Form)
        self.label_8.setGeometry(QtCore.QRect(20, 130, 161, 41))
        self.label_8.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "font: 8pt \"Myanmar Text\";\n"
                                   "background-color: rgb(170, 158, 146);")
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(520, 302, 281, 31))
        self.pushButton.setStyleSheet("color: rgb(0, 0, 0);\n"
                                      "font: 12pt \"MS UI Gothic\";\n"
                                      "background-color: rgb(170, 158, 146);")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.add.setText(_translate("Form", "Добавить"))
        self.edit.setText(_translate("Form", "Изменить"))
        self.label.setText(_translate("Form", "Coffe"))
        self.label_2.setText(_translate("Form", "Название"))
        self.label_3.setText(_translate("Form", "Степень обжарки"))
        self.label_4.setText(_translate("Form", "Молотый/в зернах"))
        self.label_5.setText(_translate("Form", "Описание вкуса"))
        self.label_6.setText(_translate("Form", "Цена"))
        self.label_7.setText(_translate("Form", "Объем упаковки"))
        self.label_8.setText(_translate("Form",
                                        "<html><head/><body><p align=\"center\">Выбирете id если хотите<br/>изменить какие либо данные</p></body></html>"))
        self.pushButton.setText(_translate("Form", "Совершить дейтсвие"))