# LinVAM
Linux Voice Activated Macro
## Status
This project is currently a work-in-progress and is minimally functional.
## Requirements
- python3
- PyQt5
- python3-xlib
- PyAudio
- pocketsphinx
- swig3.0
## Install
- $ pip3 install PyQt5
- $ pip3 install python3-xlib
- $ pip3 install PyAudio
- $ pip3 install pocketsphinx
- $ sudo apt-get install swig3.0
- $ sudo ln -s /usr/bin/swig3.0 /usr/bin/swig
- $ git clone https://github.com/rose-jinyang/LinVAM.git
## Usage
This script must be run with root privilege because it must hook and simulate input devices such as keyboard, mouse etc.
- $ cd LinVAM
- $ xhost +
- $ sudo python3 ./main.py

