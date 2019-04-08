import keyboard
from pynput.mouse import Button, Controller
import time
import threading
import copy
import json

class ProfileExecutor(threading.Thread):
    mouse = Controller()

    def __init__(self, p_profile = None):
        threading.Thread.__init__(self)
        self.m_profile = p_profile
        self.m_stop = False
        self.m_listening = True
        self.m_cmdThreads = {}

    def setProfile(self, p_profile):
        self.m_profile = p_profile

    def setEnableListening(self, p_enable):
        self.m_listening = p_enable

    def run(self):
        while self.m_stop != True:
            keyboard.wait('ctrl+alt')
            if self.m_listening != True:
                continue

            for i in range(3):
                self.doCommand('up')
                time.sleep(0.5)

                self.doCommand('left')
                time.sleep(0.5)

                self.doCommand('right')
                time.sleep(0.5)

                self.doCommand('stop')

    def stop(self):
        self.m_stop = True

    def doAction(self, p_action):
        # {'name': 'key action', 'key': 'left', 'type': 0}
        # {'name': 'pause action', 'time': 0.03}
        # {'name': 'command stop action', 'command name': 'down'}
        # {'name': 'mouse move action', 'x':5, 'y':0, 'absolute': False}
        # {'name': 'mouse click action', 'button': 'left', 'type': 0}
        # {'name': 'mouse wheel action', 'delta':10}
        w_actionName = p_action['name']
        if w_actionName == 'key action':
            w_key = p_action['key']
            w_type = p_action['type']
            if w_type == 1:
                keyboard.press(w_key)
                print("pressed key: ", w_key)
            elif w_type == 0:
                keyboard.release(w_key)
                print("released key: ", w_key)
            elif w_type == 10:
                keyboard.press(w_key)
                keyboard.release(w_key)
                print("pressed and released key: ", w_key)
        elif w_actionName == 'pause action':
            time.sleep(p_action['time'])
        elif w_actionName == 'command stop action':
            self.stopCommand(p_action['command name'])
        elif w_actionName == 'mouse move action':
            if p_action['absolute']:
                ProfileExecutor.mouse.position([p_action['x'], p_action['y']])
            else:
                ProfileExecutor.mouse.move(p_action['x'], p_action['y'])
        elif w_actionName == 'mouse click action':
            w_type = p_action['type']
            w_button = p_action['button']
            if w_type == 1:
                if w_button == 'left':
                    ProfileExecutor.mouse.press(Button.left)
                elif w_button == 'middle':
                    ProfileExecutor.mouse.press(Button.middle)
                elif w_button == 'right':
                    ProfileExecutor.mouse.press(Button.right)
                print("pressed mouse button: ", w_button)
            elif w_type == 0:
                if w_button == 'left':
                    ProfileExecutor.mouse.release(Button.left)
                elif w_button == 'middle':
                    ProfileExecutor.mouse.release(Button.middle)
                elif w_button == 'right':
                    ProfileExecutor.mouse.release(Button.right)
                print("released mouse button: ", w_button)
            elif w_type == 10:
                if w_button == 'left':
                    ProfileExecutor.mouse.click(Button.left)
                elif w_button == 'middle':
                    ProfileExecutor.mouse.click(Button.middle)
                elif w_button == 'right':
                    ProfileExecutor.mouse.click(Button.right)
                print("pressed and released mouse button: ", w_button)
        elif w_actionName == 'mouse scroll action':
            ProfileExecutor.mouse.scroll(0, p_action['delta'])

    class CommandThread(threading.Thread):
        def __init__(self, p_ProfileExecutor, p_actions, p_repeat):
            threading.Thread.__init__(self)
            self.ProfileExecutor = p_ProfileExecutor
            self.m_actions = p_actions
            self.m_repeat = p_repeat
            self.m_stop = False
        def run(self):
            w_repeat = self.m_repeat
            while self.m_stop != True:
                for w_action in self.m_actions:
                    self.ProfileExecutor.doAction(w_action)
                w_repeat = w_repeat - 1
                if w_repeat == 0:
                    break

        def stop(self):
            self.m_stop = True
            threading.Thread.join(self)

    def doCommand(self, p_cmdName):
        if self.m_profile == None:
            return

        w_commands = self.m_profile['commands']
        flag = False
        for w_command in w_commands:
            if w_command['name'] == p_cmdName:
                flag = True
                break
        if flag == False:
            return

        w_actions = w_command['actions']
        w_async = w_command['async']

        if w_async == False:
            w_repeat = w_command['repeat']
            if w_repeat < 1:
                w_repeat = 1
            while True:
                for w_action in w_command['actions']:
                    self.doAction(w_action)
                w_repeat = w_repeat - 1
                if w_repeat == 0:
                    break
        else:
            w_cmdThread = ProfileExecutor.CommandThread(self, w_actions, w_command['repeat'])
            w_cmdThread.start()
            self.m_cmdThreads[p_cmdName] = w_cmdThread

    def stopCommand(self, p_cmdName):
        if p_cmdName in self.m_cmdThreads.keys():
            self.m_cmdThreads[p_cmdName].stop()
            del self.m_cmdThreads[p_cmdName]

# def carGameTest():
#     w_profileDict = {
#         "name": "car game",
#         "commands": [
#             {'name': 'up',
#              'actions': [
#                  {'name': 'key action', 'key': 'up', 'type': 1},
#                  {'name': 'pause action', 'time': 0.03}
#              ],
#              'repeat': 1,
#              'async': False
#              },
#             {'name': 'left',
#              'actions': [{'name': 'key action', 'key': 'right', 'type': 0},
#                          {'name': 'pause action', 'time': 0.03},
#                          {'name': 'key action', 'key': 'left', 'type': 1},
#                          {'name': 'pause action', 'time': 0.03}
#                          ],
#              'repeat': 1,
#              'async': False
#              },
#             {'name': 'right',
#              'actions': [{'name': 'key action', 'key': 'left', 'type': 0},
#                          {'name': 'pause action', 'time': 0.03},
#                          {'name': 'key action', 'key': 'right', 'type': 1},
#                          {'name': 'pause action', 'time': 0.03}
#                          ],
#              'repeat': 1,
#              'async': False
#              },
#             {'name': 'stop',
#              'actions': [
#                  {'name': 'key action', 'key': 'left', 'type': 0},
#                  {'name': 'pause action', 'time': 0.03},
#                  {'name': 'key action', 'key': 'right', 'type': 0},
#                  {'name': 'pause action', 'time': 0.03},
#                  {'name': 'key action', 'key': 'up', 'type': 0},
#                  {'name': 'pause action', 'time': 0.03}
#              ],
#              'repeat': 1,
#              'async': False
#              }
#         ]
#     }
#
#     w_ProfileExecutor = ProfileExecutor(w_profileDict)
#
#     print("Move to the target window and press spacebar")
#     keyboard.wait('space')
#
#     print("Started !")
#
#     for i in range(5):
#         w_ProfileExecutor.doCommand('up')
#         time.sleep(0.5)
#
#         w_ProfileExecutor.doCommand('left')
#         time.sleep(0.5)
#
#         w_ProfileExecutor.doCommand('right')
#         time.sleep(0.5)
#
#         w_ProfileExecutor.doCommand('stop')
#
# def airplaneGameTest():
#     w_profileDict = {
#         "name": "airplane game",
#         "commands": [
#             {'name': 'up',
#              'actions': [
#                  {'name': 'command stop action', 'command name': 'down'},
#                  {'name': 'mouse move action', 'x':0, 'y':-5, 'absolute': False},
#                  {'name': 'pause action', 'time': 0.01}
#              ],
#              'repeat': -1,
#              'async': True
#             },
#             {'name': 'left',
#              'actions': [
#                  {'name': 'command stop action', 'command name':'right'},
#                  {'name': 'mouse move action', 'x':-5, 'y':0, 'absolute': False},
#                  {'name': 'pause action', 'time': 0.005}
#              ],
#              'repeat': -1,
#              'async': True
#             },
#             {'name': 'right',
#              'actions': [
#                  {'name': 'command stop action', 'command name': 'left'},
#                  {'name': 'mouse move action', 'x':5, 'y':0, 'absolute': False},
#                  {'name': 'pause action', 'time': 0.005}
#              ],
#              'repeat': -1,
#              'async': True
#             },
#             {'name': 'down',
#              'actions': [
#                  {'name': 'command stop action', 'command name': 'up'},
#                  {'name': 'mouse move action', 'x':0, 'y':5, 'absolute': False},
#                  {'name': 'pause action', 'time': 0.005}
#              ],
#              'repeat': -1,
#              'async': True
#             },
#             {'name': 'shoot',
#              'actions': [
#                  {'name': 'mouse click action', 'button':'left', 'type': 1},
#                  {'name': 'pause action', 'time': 0.03}
#              ],
#              'repeat': 1,
#              'async': False
#             },
#             {'name': 'stop',
#              'actions': [
#                  {'name': 'command stop action', 'command name': 'up'},
#                  {'name': 'command stop action', 'command name': 'left'},
#                  {'name': 'command stop action', 'command name': 'right'},
#                  {'name': 'command stop action', 'command name': 'down'},
#                  {'name': 'mouse click action', 'button': 'left', 'type': 0}
#              ],
#              'repeat': 1,
#              'async': False
#              }
#         ]
#     }
#
#     w_ProfileExecutor = ProfileExecutor(w_profileDict)
#
#     print("Move to the target window and press the spacebar to start")
#     keyboard.wait('space')
#
#     time.sleep(1)
#
#     print("Started !")
#
#     for i in range(3):
#         w_ProfileExecutor.doCommand('shoot')
#         time.sleep(1)
#
#         w_ProfileExecutor.doCommand('up')
#         time.sleep(1)
#
#         w_ProfileExecutor.doCommand('down')
#         time.sleep(0.5)
#
#         w_ProfileExecutor.stopCommand('down')
#
#         w_ProfileExecutor.doCommand('left')
#         time.sleep(0.5)
#
#         w_ProfileExecutor.doCommand('right')
#         time.sleep(0.5)
#
#         w_ProfileExecutor.doCommand('stop')
#
# if __name__ == "__main__":
#     carGameTest()
#     # airplaneGameTest()
