# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'commandeditwnd.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CommandEditDialog(object):
    def setupUi(self, CommandEditDialog):
        CommandEditDialog.setObjectName("CommandEditDialog")
        CommandEditDialog.resize(927, 419)
        font = QtGui.QFont()
        font.setPointSize(10)
        CommandEditDialog.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(CommandEditDialog)
        self.gridLayout.setContentsMargins(25, 20, 20, 15)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(CommandEditDialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(CommandEditDialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.say = QtWidgets.QLineEdit(CommandEditDialog)
        self.say.setObjectName("say")
        self.horizontalLayout.addWidget(self.say)
        spacerItem3 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.label_4 = QtWidgets.QLabel(CommandEditDialog)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.thresholdSpin = QtWidgets.QSpinBox(CommandEditDialog)
        self.thresholdSpin.setObjectName("thresholdSpin")
        self.horizontalLayout.addWidget(self.thresholdSpin)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.oneExe = QtWidgets.QRadioButton(CommandEditDialog)
        self.oneExe.setAutoExclusive(True)
        self.oneExe.setObjectName("oneExe")
        self.horizontalLayout_9.addWidget(self.oneExe)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem5)
        self.gridLayout.addLayout(self.horizontalLayout_9, 6, 0, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.continueExe = QtWidgets.QRadioButton(CommandEditDialog)
        self.continueExe.setAutoExclusive(True)
        self.continueExe.setObjectName("continueExe")
        self.horizontalLayout_10.addWidget(self.continueExe)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem6)
        self.gridLayout.addLayout(self.horizontalLayout_10, 7, 0, 1, 1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.repeatExe = QtWidgets.QRadioButton(CommandEditDialog)
        self.repeatExe.setAutoExclusive(True)
        self.repeatExe.setObjectName("repeatExe")
        self.horizontalLayout_11.addWidget(self.repeatExe)
        self.repeatCnt = QtWidgets.QSpinBox(CommandEditDialog)
        self.repeatCnt.setMinimum(2)
        self.repeatCnt.setObjectName("repeatCnt")
        self.horizontalLayout_11.addWidget(self.repeatCnt)
        self.label_3 = QtWidgets.QLabel(CommandEditDialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_11.addWidget(self.label_3)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem7)
        self.gridLayout.addLayout(self.horizontalLayout_11, 8, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.keyBut = QtWidgets.QPushButton(CommandEditDialog)
        self.keyBut.setAutoDefault(False)
        self.keyBut.setObjectName("keyBut")
        self.verticalLayout_5.addWidget(self.keyBut)
        self.mouseBut = QtWidgets.QPushButton(CommandEditDialog)
        self.mouseBut.setAutoDefault(False)
        self.mouseBut.setObjectName("mouseBut")
        self.verticalLayout_5.addWidget(self.mouseBut)
        self.pauseBut = QtWidgets.QPushButton(CommandEditDialog)
        self.pauseBut.setAutoDefault(False)
        self.pauseBut.setObjectName("pauseBut")
        self.verticalLayout_5.addWidget(self.pauseBut)
        self.otherBut = QtWidgets.QPushButton(CommandEditDialog)
        self.otherBut.setAutoDefault(False)
        self.otherBut.setObjectName("otherBut")
        self.verticalLayout_5.addWidget(self.otherBut)
        self.horizontalLayout_7.addLayout(self.verticalLayout_5)
        self.actionsListWidget = QtWidgets.QListWidget(CommandEditDialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.actionsListWidget.setFont(font)
        self.actionsListWidget.setObjectName("actionsListWidget")
        self.horizontalLayout_7.addWidget(self.actionsListWidget)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.upBut = QtWidgets.QPushButton(CommandEditDialog)
        self.upBut.setAutoDefault(False)
        self.upBut.setObjectName("upBut")
        self.verticalLayout_6.addWidget(self.upBut)
        self.downBut = QtWidgets.QPushButton(CommandEditDialog)
        self.downBut.setAutoDefault(False)
        self.downBut.setObjectName("downBut")
        self.verticalLayout_6.addWidget(self.downBut)
        self.editBut = QtWidgets.QPushButton(CommandEditDialog)
        self.editBut.setAutoDefault(False)
        self.editBut.setObjectName("editBut")
        self.verticalLayout_6.addWidget(self.editBut)
        self.deleteBut = QtWidgets.QPushButton(CommandEditDialog)
        self.deleteBut.setAutoDefault(False)
        self.deleteBut.setObjectName("deleteBut")
        self.verticalLayout_6.addWidget(self.deleteBut)
        self.horizontalLayout_7.addLayout(self.verticalLayout_6)
        self.gridLayout.addLayout(self.horizontalLayout_7, 3, 0, 1, 7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.asyncChk = QtWidgets.QCheckBox(CommandEditDialog)
        self.asyncChk.setChecked(True)
        self.asyncChk.setObjectName("asyncChk")
        self.horizontalLayout_8.addWidget(self.asyncChk)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem8)
        self.gridLayout.addLayout(self.horizontalLayout_8, 5, 0, 1, 3)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setSpacing(20)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem9)
        self.ok = QtWidgets.QPushButton(CommandEditDialog)
        self.ok.setMinimumSize(QtCore.QSize(130, 0))
        self.ok.setAutoDefault(False)
        self.ok.setObjectName("ok")
        self.horizontalLayout_12.addWidget(self.ok)
        self.cancel = QtWidgets.QPushButton(CommandEditDialog)
        self.cancel.setMinimumSize(QtCore.QSize(130, 0))
        self.cancel.setAutoDefault(False)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout_12.addWidget(self.cancel)
        self.gridLayout.addLayout(self.horizontalLayout_12, 12, 0, 1, 3)

        self.retranslateUi(CommandEditDialog)
        QtCore.QMetaObject.connectSlotsByName(CommandEditDialog)

    def retranslateUi(self, CommandEditDialog):
        _translate = QtCore.QCoreApplication.translate
        CommandEditDialog.setWindowTitle(_translate("CommandEditDialog", "Command Edit Dialog"))
        self.label_2.setText(_translate("CommandEditDialog", "When this command excutes, do the following sequence:"))
        self.label.setText(_translate("CommandEditDialog", "When I say :"))
        self.label_4.setText(_translate("CommandEditDialog", "threshold: "))
        self.oneExe.setText(_translate("CommandEditDialog", "This command executes once"))
        self.continueExe.setText(_translate("CommandEditDialog", "This command repeats continuously"))
        self.repeatExe.setText(_translate("CommandEditDialog", "This command repeats"))
        self.label_3.setText(_translate("CommandEditDialog", "times"))
        self.keyBut.setText(_translate("CommandEditDialog", "Key Press"))
        self.mouseBut.setText(_translate("CommandEditDialog", "Mouse"))
        self.pauseBut.setText(_translate("CommandEditDialog", "Pause"))
        self.otherBut.setText(_translate("CommandEditDialog", "Other"))
        self.upBut.setText(_translate("CommandEditDialog", "Up"))
        self.downBut.setText(_translate("CommandEditDialog", "Down"))
        self.editBut.setText(_translate("CommandEditDialog", "Edit"))
        self.deleteBut.setText(_translate("CommandEditDialog", "Delete"))
        self.asyncChk.setText(_translate("CommandEditDialog", "Allow other commands to execute while this one is running"))
        self.ok.setText(_translate("CommandEditDialog", "OK"))
        self.cancel.setText(_translate("CommandEditDialog", "Cancel"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CommandEditDialog = QtWidgets.QDialog()
    ui = Ui_CommandEditDialog()
    ui.setupUi(CommandEditDialog)
    CommandEditDialog.show()
    sys.exit(app.exec_())
