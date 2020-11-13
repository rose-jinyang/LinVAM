# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'soundactioneditwnd.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SoundSelect(object):
    def setupUi(self, SoundSelect):
        SoundSelect.setObjectName("SoundSelect")
        SoundSelect.resize(1119, 362)
        SoundSelect.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.labelVoicepacks = QtWidgets.QLabel(SoundSelect)
        self.labelVoicepacks.setGeometry(QtCore.QRect(10, 30, 111, 17))
        self.labelVoicepacks.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.labelVoicepacks.setObjectName("labelVoicepacks")
        self.labelCategories = QtWidgets.QLabel(SoundSelect)
        self.labelCategories.setGeometry(QtCore.QRect(160, 30, 111, 17))
        self.labelCategories.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.labelCategories.setObjectName("labelCategories")
        self.listFiles = QtWidgets.QListView(SoundSelect)
        self.listFiles.setGeometry(QtCore.QRect(660, 90, 451, 231))
        self.listFiles.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.listFiles.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listFiles.setProperty("showDropIndicator", False)
        self.listFiles.setAlternatingRowColors(True)
        self.listFiles.setObjectName("listFiles")
        self.listCategories = QtWidgets.QListView(SoundSelect)
        self.listCategories.setEnabled(True)
        self.listCategories.setGeometry(QtCore.QRect(160, 90, 491, 231))
        self.listCategories.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.listCategories.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listCategories.setProperty("showDropIndicator", False)
        self.listCategories.setAlternatingRowColors(True)
        self.listCategories.setObjectName("listCategories")
        self.listVoicepacks = QtWidgets.QListView(SoundSelect)
        self.listVoicepacks.setGeometry(QtCore.QRect(10, 50, 141, 271))
        self.listVoicepacks.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.listVoicepacks.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listVoicepacks.setProperty("showDropIndicator", False)
        self.listVoicepacks.setAlternatingRowColors(True)
        self.listVoicepacks.setObjectName("listVoicepacks")
        self.labelFiles = QtWidgets.QLabel(SoundSelect)
        self.labelFiles.setGeometry(QtCore.QRect(660, 30, 111, 17))
        self.labelFiles.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.labelFiles.setObjectName("labelFiles")
        self.buttonOkay = QtWidgets.QPushButton(SoundSelect)
        self.buttonOkay.setEnabled(True)
        self.buttonOkay.setGeometry(QtCore.QRect(940, 330, 80, 25))
        self.buttonOkay.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.buttonOkay.setObjectName("buttonOkay")
        self.buttonCancel = QtWidgets.QPushButton(SoundSelect)
        self.buttonCancel.setGeometry(QtCore.QRect(1030, 330, 80, 25))
        self.buttonCancel.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.buttonCancel.setObjectName("buttonCancel")
        self.filterCategories = QtWidgets.QPlainTextEdit(SoundSelect)
        self.filterCategories.setGeometry(QtCore.QRect(160, 50, 491, 31))
        self.filterCategories.setObjectName("filterCategories")
        self.filterFiles = QtWidgets.QPlainTextEdit(SoundSelect)
        self.filterFiles.setGeometry(QtCore.QRect(660, 50, 451, 31))
        self.filterFiles.setPlainText("")
        self.filterFiles.setObjectName("filterFiles")
        self.buttonPlaySound = QtWidgets.QPushButton(SoundSelect)
        self.buttonPlaySound.setGeometry(QtCore.QRect(410, 330, 80, 25))
        self.buttonPlaySound.setToolTip("")
        self.buttonPlaySound.setObjectName("buttonPlaySound")
        self.buttonStopSound = QtWidgets.QPushButton(SoundSelect)
        self.buttonStopSound.setGeometry(QtCore.QRect(500, 330, 80, 25))
        self.buttonStopSound.setToolTip("")
        self.buttonStopSound.setObjectName("buttonStopSound")

        self.retranslateUi(SoundSelect)
        QtCore.QMetaObject.connectSlotsByName(SoundSelect)

    def retranslateUi(self, SoundSelect):
        _translate = QtCore.QCoreApplication.translate
        SoundSelect.setWindowTitle(_translate("SoundSelect", "Sound selection"))
        self.labelVoicepacks.setText(_translate("SoundSelect", "VoicePacks:"))
        self.labelCategories.setText(_translate("SoundSelect", "Categories:"))
        self.labelFiles.setText(_translate("SoundSelect", "Voice files:"))
        self.buttonOkay.setText(_translate("SoundSelect", "Ok"))
        self.buttonCancel.setText(_translate("SoundSelect", "Cancel"))
        self.filterCategories.setToolTip(_translate("SoundSelect", "Filter categories"))
        self.filterCategories.setStatusTip(_translate("SoundSelect", "Filter"))
        self.filterFiles.setToolTip(_translate("SoundSelect", "Filter voice files"))
        self.filterFiles.setStatusTip(_translate("SoundSelect", "Filter"))
        self.buttonPlaySound.setText(_translate("SoundSelect", "Play Sound"))
        self.buttonStopSound.setText(_translate("SoundSelect", "Stop Sound"))
