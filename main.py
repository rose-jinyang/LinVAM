from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ui_mainwnd import Ui_MainWidget
from profileeditwnd import ProfileEditWnd
import json
from profileexecutor import ProfileExecutor
import sys
import pickle
import time
import keyboard
import threading

class MainWnd(QWidget):
    def __init__(self, p_parent = None):
        super().__init__(p_parent)
        self.ui = Ui_MainWidget()
        self.ui.setupUi(self)
        self.m_profileExecutor = ProfileExecutor()

        self.ui.profileCbx.currentIndexChanged.connect(self.slotProfileChanged)
        self.ui.addBut.clicked.connect(self.slotAddNewProfile)
        self.ui.editBut.clicked.connect(self.slotEditProfile)
        self.ui.removeBut.clicked.connect(self.slotRemoveProfile)
        self.ui.listeningChk.stateChanged.connect(self.slotListeningEnabled)
        self.ui.ok.clicked.connect(self.slotOK)
        self.ui.cancel.clicked.connect(self.slotCancel)

        if self.loadFromDatabase() > 0 :
        # if self.loadTestProfiles() > 0:
            w_jsonProfile = self.ui.profileCbx.itemData(0)
            if w_jsonProfile != None:
                self.m_activeProfile = json.loads(w_jsonProfile)
                self.m_profileExecutor.setProfile(self.m_activeProfile)
                self.m_profileExecutor.start()

    def saveToDatabase(self):
        w_profiles = []
        w_profileCnt = self.ui.profileCbx.count()
        for w_idx in range(w_profileCnt):
            w_jsonProfile = self.ui.profileCbx.itemData(w_idx)
            if w_jsonProfile == None:
                continue

            w_profile = json.loads(w_jsonProfile)
            w_profiles.append(w_profile)

        with open("profiles.dat", "wb") as f:
            pickle.dump(w_profiles, f, pickle.HIGHEST_PROTOCOL)

    def loadFromDatabase(self):
        w_profiles = []
        with open("profiles.dat", "rb") as f:
            w_profiles = pickle.load(f)

        for w_profile in w_profiles:
            self.ui.profileCbx.addItem(w_profile['name'])
            w_jsonProfile = json.dumps(w_profile)
            self.ui.profileCbx.setItemData(self.ui.profileCbx.count() - 1, w_jsonProfile)

        return len(w_profiles)

    def loadTestProfiles(self):

        w_carProfileDict = {
            "name": "car game",
            "commands": [
                {'name': 'forward',
                 'actions': [
                     {'name': 'key action', 'key': 'up', 'type': 1}
                 ],
                 'repeat': 1,
                 'async': False,
                 'threshold': 12
                 },
                {'name': 'back',
                 'actions': [
                     {'name': 'key action', 'key': 'down', 'type': 1}
                 ],
                 'repeat': 1,
                 'async': False,
                 'threshold': 3
                 },
                {'name': 'left',
                 'actions': [{'name': 'key action', 'key': 'right', 'type': 0},
                             {'name': 'key action', 'key': 'left', 'type': 1},
                             ],
                 'repeat': 1,
                 'async': False,
                 'threshold': 10
                 },
                {'name': 'right',
                 'actions': [{'name': 'key action', 'key': 'left', 'type': 0},
                             {'name': 'key action', 'key': 'right', 'type': 1},
                             ],
                 'repeat': 1,
                 'async': False,
                 'threshold': 3
                 },
                {'name': 'stop',
                 'actions': [
                     {'name': 'key action', 'key': 'left', 'type': 0},
                     {'name': 'key action', 'key': 'right', 'type': 0},
                     {'name': 'key action', 'key': 'up', 'type': 0},
                     {'name': 'key action', 'key': 'down', 'type': 0}
                 ],
                 'repeat': 1,
                 'async': False,
                 'threshold': 8
                 }
            ]
        }

        w_airplaneProfileDict = {
            "name": "airplane game",
            "commands": [
                {'name': 'up',
                 'actions': [
                     {'name': 'command stop action', 'command name': 'down'},
                     {'name': 'mouse move action', 'x': 0, 'y': -5, 'absolute': False},
                     {'name': 'pause action', 'time': 0.01}
                 ],
                 'repeat': -1,
                 'async': True,
                 'threshold': 3
                 },
                {'name': 'left',
                 'actions': [
                     {'name': 'command stop action', 'command name': 'right'},
                     {'name': 'mouse move action', 'x': -5, 'y': 0, 'absolute': False},
                     {'name': 'pause action', 'time': 0.005}
                 ],
                 'repeat': -1,
                 'async': True,
                 'threshold': 3
                 },
                {'name': 'right',
                 'actions': [
                     {'name': 'command stop action', 'command name': 'left'},
                     {'name': 'mouse move action', 'x': 5, 'y': 0, 'absolute': False},
                     {'name': 'pause action', 'time': 0.005}
                 ],
                 'repeat': -1,
                 'async': True,
                 'threshold': 3
                 },
                {'name': 'down',
                 'actions': [
                     {'name': 'command stop action', 'command name': 'up'},
                     {'name': 'mouse move action', 'x': 0, 'y': 5, 'absolute': False},
                     {'name': 'pause action', 'time': 0.005}
                 ],
                 'repeat': -1,
                 'async': True,
                 'threshold': 3
                 },
                {'name': 'shoot',
                 'actions': [
                     {'name': 'mouse click action', 'button': 'left', 'type': 1},
                     {'name': 'pause action', 'time': 0.03}
                 ],
                 'repeat': 1,
                 'async': False,
                 'threshold': 3
                 },
                {'name': 'stop',
                 'actions': [
                     {'name': 'command stop action', 'command name': 'up'},
                     {'name': 'command stop action', 'command name': 'left'},
                     {'name': 'command stop action', 'command name': 'right'},
                     {'name': 'command stop action', 'command name': 'down'},
                     {'name': 'mouse click action', 'button': 'left', 'type': 0}
                 ],
                 'repeat': 1,
                 'async': False,
                 'threshold': 3
                 }
            ]
        }
        w_profiles = []
        w_profiles.append(w_carProfileDict)
        w_profiles.append(w_airplaneProfileDict)

        i = 0
        for w_profile in w_profiles:
            self.ui.profileCbx.addItem(w_profile['name'])
            w_jsonProfile = json.dumps(w_profile)
            self.ui.profileCbx.setItemData(i, w_jsonProfile)
            i = i + 1

        return i

    def slotProfileChanged(self, p_idx):
        w_jsonProfile = self.ui.profileCbx.itemData(p_idx)
        if w_jsonProfile != None:
            self.m_activeProfile = json.loads(w_jsonProfile)
            self.m_profileExecutor.setProfile(self.m_activeProfile)

    def slotAddNewProfile(self):
        w_profileEditWnd = ProfileEditWnd(None, self)
        if w_profileEditWnd.exec() == QDialog.Accepted:
            w_profile = w_profileEditWnd.m_profile
            self.m_profileExecutor.setProfile(w_profile)
            self.ui.profileCbx.addItem(w_profile['name'])
            w_jsonProfile = json.dumps(w_profile)
            self.ui.profileCbx.setItemData(self.ui.profileCbx.count()-1, w_jsonProfile)

    def slotEditProfile(self):
        w_idx = self.ui.profileCbx.currentIndex()
        w_jsonProfile = self.ui.profileCbx.itemData(w_idx)
        w_profile = json.loads(w_jsonProfile)
        w_profileEditWnd = ProfileEditWnd(w_profile, self)
        if w_profileEditWnd.exec() == QDialog.Accepted:
            w_profile = w_profileEditWnd.m_profile
            self.m_profileExecutor.setProfile(w_profile)
            self.ui.profileCbx.setItemText(w_idx, w_profile['name'])
            w_jsonProfile = json.dumps(w_profile)
            self.ui.profileCbx.setItemData(w_idx, w_jsonProfile)

    def slotRemoveProfile(self):
        w_curIdx = self.ui.profileCbx.currentIndex()
        if w_curIdx >= 0:
            self.ui.profileCbx.removeItem(w_curIdx)

        w_curIdx = self.ui.profileCbx.currentIndex()
        if w_curIdx >= 0:
            w_jsonProfile = self.ui.profileCbx.itemData(w_curIdx)
            w_profile = json.loads(w_jsonProfile)
            self.m_profileExecutor.setProfile(w_profile)

    def slotListeningEnabled(self, p_enabled):
        if p_enabled:
            self.m_profileExecutor.setEnableListening(True)
        else:
            self.m_profileExecutor.setEnableListening(False)

    def slotOK(self):
        self.saveToDatabase()
        self.m_profileExecutor.stop()
        self.close()

    def slotCancel(self):
        self.m_profileExecutor.stop()
        self.close()
        exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWnd = MainWnd()
    mainWnd.show()
    sys.exit(app.exec_())
