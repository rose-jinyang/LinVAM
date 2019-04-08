# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'profileeditwnd.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProfileEditDialog(object):
    def setupUi(self, ProfileEditDialog):
        ProfileEditDialog.setObjectName("ProfileEditDialog")
        ProfileEditDialog.resize(1191, 591)
        self.gridLayout_2 = QtWidgets.QGridLayout(ProfileEditDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(ProfileEditDialog)
        self.label.setMinimumSize(QtCore.QSize(60, 0))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.profileNameEdit = QtWidgets.QLineEdit(ProfileEditDialog)
        self.profileNameEdit.setObjectName("profileNameEdit")
        self.horizontalLayout.addWidget(self.profileNameEdit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(ProfileEditDialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.cmdTable = QtWidgets.QTableWidget(self.groupBox)
        self.cmdTable.setMinimumSize(QtCore.QSize(0, 200))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cmdTable.setFont(font)
        self.cmdTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.cmdTable.setDragDropOverwriteMode(False)
        self.cmdTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.cmdTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.cmdTable.setColumnCount(2)
        self.cmdTable.setObjectName("cmdTable")
        self.cmdTable.setRowCount(0)
        self.cmdTable.horizontalHeader().setDefaultSectionSize(160)
        self.cmdTable.horizontalHeader().setMinimumSectionSize(160)
        self.gridLayout.addWidget(self.cmdTable, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.newCmd = QtWidgets.QPushButton(self.groupBox)
        self.newCmd.setMinimumSize(QtCore.QSize(130, 0))
        self.newCmd.setObjectName("newCmd")
        self.horizontalLayout_2.addWidget(self.newCmd)
        self.editCmd = QtWidgets.QPushButton(self.groupBox)
        self.editCmd.setMinimumSize(QtCore.QSize(130, 0))
        self.editCmd.setObjectName("editCmd")
        self.horizontalLayout_2.addWidget(self.editCmd)
        self.deleteCmd = QtWidgets.QPushButton(self.groupBox)
        self.deleteCmd.setMinimumSize(QtCore.QSize(130, 0))
        self.deleteCmd.setObjectName("deleteCmd")
        self.horizontalLayout_2.addWidget(self.deleteCmd)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.ok = QtWidgets.QPushButton(ProfileEditDialog)
        self.ok.setMinimumSize(QtCore.QSize(130, 0))
        self.ok.setObjectName("ok")
        self.horizontalLayout_3.addWidget(self.ok)
        self.cancel = QtWidgets.QPushButton(ProfileEditDialog)
        self.cancel.setMinimumSize(QtCore.QSize(130, 0))
        self.cancel.setObjectName("cancel")
        self.horizontalLayout_3.addWidget(self.cancel)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.retranslateUi(ProfileEditDialog)
        QtCore.QMetaObject.connectSlotsByName(ProfileEditDialog)

    def retranslateUi(self, ProfileEditDialog):
        _translate = QtCore.QCoreApplication.translate
        ProfileEditDialog.setWindowTitle(_translate("ProfileEditDialog", "Dialog"))
        self.label.setText(_translate("ProfileEditDialog", "Profile:"))
        self.groupBox.setTitle(_translate("ProfileEditDialog", "Commands"))
        self.newCmd.setText(_translate("ProfileEditDialog", "New"))
        self.editCmd.setText(_translate("ProfileEditDialog", "Edit"))
        self.deleteCmd.setText(_translate("ProfileEditDialog", "Delete"))
        self.ok.setText(_translate("ProfileEditDialog", "OK"))
        self.cancel.setText(_translate("ProfileEditDialog", "Cancel"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProfileEditDialog = QtWidgets.QDialog()
    ui = Ui_ProfileEditDialog()
    ui.setupUi(ProfileEditDialog)
    ProfileEditDialog.show()
    sys.exit(app.exec_())
