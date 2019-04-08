# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\keyactioneditwnd.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_KeyActionEditDialog(object):
    def setupUi(self, KeyActionEditDialog):
        KeyActionEditDialog.setObjectName("KeyActionEditDialog")
        KeyActionEditDialog.resize(471, 164)
        self.gridLayout = QtWidgets.QGridLayout(KeyActionEditDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(KeyActionEditDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.press_releaseKey = QtWidgets.QRadioButton(KeyActionEditDialog)
        self.press_releaseKey.setObjectName("press_releaseKey")
        self.horizontalLayout_2.addWidget(self.press_releaseKey)
        self.pressKey = QtWidgets.QRadioButton(KeyActionEditDialog)
        self.pressKey.setObjectName("pressKey")
        self.horizontalLayout_2.addWidget(self.pressKey)
        self.releaseKey = QtWidgets.QRadioButton(KeyActionEditDialog)
        self.releaseKey.setObjectName("releaseKey")
        self.horizontalLayout_2.addWidget(self.releaseKey)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.ok = QtWidgets.QPushButton(KeyActionEditDialog)
        self.ok.setAutoDefault(False)
        self.ok.setObjectName("ok")
        self.horizontalLayout_3.addWidget(self.ok)
        self.cancel = QtWidgets.QPushButton(KeyActionEditDialog)
        self.cancel.setAutoDefault(False)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout_3.addWidget(self.cancel)
        self.gridLayout.addLayout(self.horizontalLayout_3, 5, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ctrlBut = QtWidgets.QPushButton(KeyActionEditDialog)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.ctrlBut.setFont(font)
        self.ctrlBut.setAutoDefault(False)
        self.ctrlBut.setObjectName("ctrlBut")
        self.horizontalLayout.addWidget(self.ctrlBut)
        self.altBut = QtWidgets.QPushButton(KeyActionEditDialog)
        self.altBut.setAutoDefault(False)
        self.altBut.setObjectName("altBut")
        self.horizontalLayout.addWidget(self.altBut)
        self.shiftBut = QtWidgets.QPushButton(KeyActionEditDialog)
        self.shiftBut.setAutoDefault(False)
        self.shiftBut.setObjectName("shiftBut")
        self.horizontalLayout.addWidget(self.shiftBut)
        self.winBut = QtWidgets.QPushButton(KeyActionEditDialog)
        self.winBut.setAutoDefault(False)
        self.winBut.setObjectName("winBut")
        self.horizontalLayout.addWidget(self.winBut)
        self.keyEdit = QtWidgets.QLineEdit(KeyActionEditDialog)
        self.keyEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.keyEdit.setObjectName("keyEdit")
        self.horizontalLayout.addWidget(self.keyEdit)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(KeyActionEditDialog)
        QtCore.QMetaObject.connectSlotsByName(KeyActionEditDialog)

    def retranslateUi(self, KeyActionEditDialog):
        _translate = QtCore.QCoreApplication.translate
        KeyActionEditDialog.setWindowTitle(_translate("KeyActionEditDialog", "Key Action Dialog"))
        self.label.setText(_translate("KeyActionEditDialog", "Key (Combination):"))
        self.press_releaseKey.setText(_translate("KeyActionEditDialog", "Press and Release Key(s)"))
        self.pressKey.setText(_translate("KeyActionEditDialog", "Press Key(s)"))
        self.releaseKey.setText(_translate("KeyActionEditDialog", "Release Key(s)"))
        self.ok.setText(_translate("KeyActionEditDialog", "OK"))
        self.cancel.setText(_translate("KeyActionEditDialog", "Cancel"))
        self.ctrlBut.setText(_translate("KeyActionEditDialog", "Ctrl"))
        self.altBut.setText(_translate("KeyActionEditDialog", "Alt"))
        self.shiftBut.setText(_translate("KeyActionEditDialog", "Shift"))
        self.winBut.setText(_translate("KeyActionEditDialog", "Win"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    KeyActionEditDialog = QtWidgets.QDialog()
    ui = Ui_KeyActionEditDialog()
    ui.setupUi(KeyActionEditDialog)
    KeyActionEditDialog.show()
    sys.exit(app.exec_())
