from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ui_keyactioneditwnd import Ui_KeyActionEditDialog
import keyboard
import threading

class KeyActionEditWnd(QDialog):
    def __init__(self, p_keyAction, p_parent = None):
        super().__init__(p_parent)
        self.ui = Ui_KeyActionEditDialog()
        self.ui.setupUi(self)

        self.ui.ctrlBut.clicked.connect(self.slotCtrlClicked)
        self.ui.altBut.clicked.connect(self.slotAltClicked)
        self.ui.shiftBut.clicked.connect(self.slotShiftClicked)
        self.ui.winBut.clicked.connect(self.slotWinClicked)

        self.ui.ok.clicked.connect(self.slotOK)
        self.ui.cancel.clicked.connect(self.slotCancel)

        self.m_ctrlState = 0
        self.m_altState = 0
        self.m_shiftState = 0
        self.m_winState = 0

        self.m_keyAction = {}
        self.ui.press_releaseKey.setChecked(True)

        t = threading.Thread(target=self.keyInput)
        t.daemon = True
        t.start()

        if p_keyAction == None:
            return

        w_hotKey = p_keyAction['key']
        w_keys = w_hotKey.split('+')

        for w_key in w_keys:
            if w_key == 'left ctrl':
                self.m_ctrlState = 1
            elif w_key == 'right ctrl':
                self.m_ctrlState = 2
            elif w_key == 'left alt':
                self.m_altState = 1
            elif w_key == 'right alt':
                self.m_altState = 2
            elif w_key == 'left shift':
                self.m_shiftState = 1
            elif w_key == 'right shift':
                self.m_shiftState = 2
            elif w_key == 'left windows':
                self.m_winState = 1
            elif w_key == 'right windows':
                self.m_winState = 2
            else:
                self.ui.keyEdit.setText(w_key)

        w_stateText = ['Ctrl', 'Left Ctrl', 'Right Ctrl']
        self.ui.ctrlBut.setText(w_stateText[self.m_ctrlState])
        w_stateText = ['Alt', 'Left Alt', 'Right Alt']
        self.ui.altBut.setText(w_stateText[self.m_altState])
        w_stateText = ['Shift', 'Left Shift', 'Right Shift']
        self.ui.shiftBut.setText(w_stateText[self.m_shiftState])
        w_stateText = ['Win', 'Left Win', 'Right Win']
        self.ui.winBut.setText(w_stateText[self.m_winState])

        if p_keyAction['type'] == 10:
            self.ui.press_releaseKey.setChecked(True)
        elif p_keyAction['type'] == 0:
            self.ui.releaseKey.setChecked(True)
        elif p_keyAction['type'] == 1:
            self.ui.pressKey.setChecked(True)

    def slotOK(self):
        w_ctrlStateText = ['', 'left ctrl', 'right ctrl']
        w_altStateText = ['', 'left alt', 'right alt']
        w_shiftStateText = ['', 'left shift', 'right shift']
        w_winStateText = ['', 'left windows', 'right windows']

        w_hotKey = ''
        if self.m_ctrlState != 0:
            w_hotKey = w_ctrlStateText[self.m_ctrlState]

        if self.m_altState != 0:
            if w_hotKey != '':
                w_hotKey = w_hotKey + '+'
            w_hotKey = w_hotKey + w_altStateText[self.m_altState]

        if self.m_shiftState != 0:
            if w_hotKey != '':
                w_hotKey = w_hotKey + '+'
            w_hotKey = w_hotKey + w_shiftStateText[self.m_shiftState]

        if self.m_winState != 0:
            if w_hotKey != '':
                w_hotKey = w_hotKey + '+'
            w_hotKey = w_hotKey + w_winStateText[self.m_winState]

        if self.ui.keyEdit.text() != '':
            if w_hotKey != '':
                w_hotKey = w_hotKey + '+'
            w_hotKey = w_hotKey + self.ui.keyEdit.text()

        if w_hotKey == '':
            return

        self.m_keyAction = {}
        self.m_keyAction['name'] = 'key action'
        self.m_keyAction['key'] = w_hotKey
        if self.ui.press_releaseKey.isChecked():
            self.m_keyAction['type'] = 10
        elif self.ui.pressKey.isChecked():
            self.m_keyAction['type'] = 1
        elif self.ui.releaseKey.isChecked():
            self.m_keyAction['type'] = 0

        return super().accept()

    def slotCancel(self):
        return super().reject()

    def slotCtrlClicked(self):
        self.m_ctrlState = (self.m_ctrlState + 1) % 3
        w_stateText = ['Ctrl', 'Left Ctrl', 'Right Ctrl']
        self.ui.ctrlBut.setText(w_stateText[self.m_ctrlState])

    def slotAltClicked(self):
        self.m_altState = (self.m_altState + 1) % 3
        w_stateText = ['Alt', 'Left Alt', 'Right Alt']
        self.ui.altBut.setText(w_stateText[self.m_altState])

    def slotShiftClicked(self):
        self.m_shiftState = (self.m_shiftState + 1) % 3
        w_stateText = ['Shift', 'Left Shift', 'Right Shift']
        self.ui.shiftBut.setText(w_stateText[self.m_shiftState])

    def slotWinClicked(self):
        self.m_winState = (self.m_winState + 1) % 3
        w_stateText = ['Win', 'Left Win', 'Right Win']
        self.ui.winBut.setText(w_stateText[self.m_winState])

    def keyInput(self):
        try:
            while True:
                self.ui.keyEdit.setText(keyboard.read_hotkey(False))
        except:
            pass

