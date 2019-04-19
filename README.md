# LinVAM
Linux Voice Activated Macro
## Status
This project is currently a work-in-progress and is minimally functional.

Utilising Pocketsphinx, a lightweight voice to text engine you can specify voice commands for the tool to recognise and actions to perform.

Known bugs and planned additions
- To save and use changes click Ok on the main GUI then reload.
- Remember last loaded profile and load on start
- Log window showing spoken words the V2T recognises with ability to right click and assign voice command and actions to current profile
- Support for joysticks and gaming devices
## Requirements
- python3
- PyQt5
- python3-xlib
- pocketsphinx
- swig3.0
## Install
- $ pip3 install PyQt5
- $ pip3 install python3-xlib
- $ pip3 install pocketsphinx
- $ sudo apt-get install swig3.0
- $ sudo ln -s /usr/bin/swig3.0 /usr/bin/swig
- $ git clone https://github.com/rose-jinyang/LinVAM.git
## Usage
This script must be run with root privilege because it must hook and simulate input devices such as keyboard, mouse etc.
- $ cd LinVAM
- $ xhost +
- $ sudo python3 ./main.py

### Profiles
Multiple profiles are supported.  To create a new profile for a specific task/game click new and the main profile editor window will be displayed

![Main GUI](https://raw.githubusercontent.com/aidygus/LinVAM/master/.img/gui.png)
### Key combinations
To assign key combinations first decide which functional key to press by clicking on Ctrl, Alt, Shift or Win to denote left or right key then press the actual command key

![Main GUI](https://raw.githubusercontent.com/aidygus/LinVAM/master/.img/combination.png)
### Complex commands
It is possible to add multiple actions to a voice command for complex macros with the ability to add a pause between each action.
You can also assign mouse movements and system commands if you require (eg opening applications such as calculator, browser etc)

![Main GUI](https://raw.githubusercontent.com/aidygus/LinVAM/master/.img/complex.png)
### Threshold
As a rough guide use a value of 10 for each syllable of a word then tweak it down for better accuracy.
