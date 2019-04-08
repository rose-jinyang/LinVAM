# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pauseactioneditwnd.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PauseActionEditDialog(object):
    def setupUi(self, PauseActionEditDialog):
        PauseActionEditDialog.setObjectName("PauseActionEditDialog")
        PauseActionEditDialog.resize(271, 133)
        font = QtGui.QFont()
        font.setPointSize(10)
        PauseActionEditDialog.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(PauseActionEditDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(PauseActionEditDialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.secondEdit = QtWidgets.QLineEdit(PauseActionEditDialog)
        self.secondEdit.setObjectName("secondEdit")
        self.horizontalLayout.addWidget(self.secondEdit)
        self.label_2 = QtWidgets.QLabel(PauseActionEditDialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.ok = QtWidgets.QPushButton(PauseActionEditDialog)
        self.ok.setMinimumSize(QtCore.QSize(100, 0))
        self.ok.setObjectName("ok")
        self.horizontalLayout_2.addWidget(self.ok)
        self.cancel = QtWidgets.QPushButton(PauseActionEditDialog)
        self.cancel.setMinimumSize(QtCore.QSize(100, 0))
        self.cancel.setObjectName("cancel")
        self.horizontalLayout_2.addWidget(self.cancel)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.retranslateUi(PauseActionEditDialog)
        QtCore.QMetaObject.connectSlotsByName(PauseActionEditDialog)

    def retranslateUi(self, PauseActionEditDialog):
        _translate = QtCore.QCoreApplication.translate
        PauseActionEditDialog.setWindowTitle(_translate("PauseActionEditDialog", "Pause Action Edit Dialog"))
        self.label.setText(_translate("PauseActionEditDialog", "Pause for "))
        self.label_2.setText(_translate("PauseActionEditDialog", "seconds"))
        self.ok.setText(_translate("PauseActionEditDialog", "OK"))
        self.cancel.setText(_translate("PauseActionEditDialog", "Cancel"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PauseActionEditDialog = QtWidgets.QDialog()
    ui = Ui_PauseActionEditDialog()
    ui.setupUi(PauseActionEditDialog)
    PauseActionEditDialog.show()
    sys.exit(app.exec_())
