import keyboard
from pynput.mouse import Button, Controller
import time
import threading
import os, pyaudio
from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *

class ProfileExecutor(threading.Thread):
    mouse = Controller()

    def __init__(self, p_profile = None):
        threading.Thread.__init__(self)
        self.setProfile(p_profile)
        self.m_stop = False
        self.m_listening = True
        self.m_cmdThreads = {}

        self.m_config = Decoder.default_config()
        self.m_config.set_string('-hmm', os.path.join('model', 'en-us/en-us'))
        self.m_config.set_string('-dict', os.path.join('model', 'en-us/cmudict-en-us.dict'))
        self.m_config.set_string('-kws', 'command.list')

        p = pyaudio.PyAudio()
        self.m_stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True)
        self.m_stream.start_stream()

        # Process audio chunk by chunk. On keyword detected perform action and restart search
        self.m_decoder = Decoder(self.m_config)

    def setProfile(self, p_profile):
        self.m_profile = p_profile
        if self.m_profile == None:
            return

        w_commandWordFile = open('command.list', 'w')
        w_commands = self.m_profile['commands']
        i = 0
        for w_command in w_commands:
            if i != 0:
                w_commandWordFile.write('\n')
            w_commandWordFile.write(w_command['name'] + ' /1e-%d/' % w_command['threshold'])
            i = i + 1
        w_commandWordFile.close()
        self.m_config.set_string('-kws', 'command.list')

    def setEnableListening(self, p_enable):
        self.m_listening = p_enable

    def run(self):
        self.m_decoder.start_utt()
        while self.m_stop != True:
            buf = self.m_stream.read(1024)

            self.m_decoder.process_raw(buf, False, False)

            if self.m_decoder.hyp() != None:
                # print([(seg.word, seg.prob, seg.start_frame, seg.end_frame) for seg in decoder.seg()])
                # print("Detected keyword, restarting search")
                #
                # Here you run the code you want based on keyword
                #
                for w_seg in self.m_decoder.seg():
                    self.doCommand(w_seg.word.rstrip())

                self.m_decoder.end_utt()
                self.m_decoder.start_utt()

    def stop(self):
        self.m_stop = True
        threading.Thread.join(self)

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
