# Changelog smirgol

### Issues:
	- (fixed) voice recognition autostarts, there is no way to disable it. the flag "self.m_listening" does nothing
	- (fixed) when profile is changed, the new commands will not be loaded, as the voice recognition is already running - by default with the Elite Dangerous settings. You cannot use any other profile.
	- (fixed) "When I say" commands need to be all lower case, otherwise it won't be recognized.

### Known/New Issues:
	- When using external speakers it will pick up a playing audio sample and might trigger commands. Use headphones! :)
	- On a Valve Index headset, the earphones, while being good, will feed the Index microphone causing troubles with the voice recognition.
	  There's probably nothing that can be done about it, maybe some sort of audio filter could be introduced to cut off low-volume sounds?
	  Lower voice audio for now to minimize the issue.
	- There sometimes is a window error in the console when clicking on a 'cancel' button, does not seem to do harm, but should fix that if possible.
	- Sometimes keypress signals are not recognized by game, this is the case with xdotool, don't know if this also happens with standard keyboard library.
	  It seems to solve the issue if you at least once manually press any key while the game window is focused

### Added:
	- hacked profileexcutor to reload command list when changing it. it did not do that,
	  so changing the profile had no effect at all.
	- hacked profileexecutor to somewhat make use of "Enable listening".
	  It was an option without functionality at all until now.
	- created new directory 'voicepacks', copy HCS voicepacks here
	- new command to play a sound
	- new gui to select sounds from voicepacks
	- created playsound class that reads voicepack files and plays audio files with ffplay
	- added alternate keypress handling using xdotool, which won't require root privileges.
	  might not work for any key existing in profiles, as some need to be remapped. added some remappings to profileexecutor.py pressKey()
	- added basic command line argument reading to set some configs. right now there:
	  -noroot - will enable xdotool usage for keypresses
	  -xdowindowid <windowid> - will send keypresses to this window only, makes it more relyable when window is not focused for any reason
	- added auto-detection of Elite Dangerous client window id if -noroot is used and no -xdowindowid is supplied.
	  for this to work, start this script AFTER the client is already running.
	- monkey-wrenched a volume slider to the main window
	- added confirmation dialog for removing a profile (!)
	- copy existing profile. added a copy button to the main menu
	- properly shutdown audio recording stream
	- updated gitignore to ignore audio files

### Dependencies
	- ffplay
	- xdotool (optional, won't need root privileges for keypresses)

	Not sure about these, I had them installed already:
		- import subprocess
		- import shlex
		- import signal

### TODO
	- select multiple files (from same category) to play one of them randomly

### FUTURE IDEAS
	- remember settings and load on start (nice to have)
	- change key assignment logic to record a keypress / buttonpress combo
		- will definitely break existing profiles, as we need to record keycodes and stuff
	- maybe add a state machine like voice attack does
	- look into reading log files from elite dangerous to trigger certain actions.
	  this would be a very game specific addition though...
	- make connection to a specific voice pack more loose, so you can easily change the voice pack,
	  without re-editing all the commands. maybe even a different voice pack for certain actions,
	  like in voice attack (crewmen)
	- reorganize main window to hold more settings and a log window for displaying actions
	- look into other text2speech engines
		i gave julius-speech a quick try. its pretty easy to setup and looks promising, but it
		also has its problems with detecting some "exotic" words. as not being a native
		english speaker, my pronounciation is not the best sometimes, which doesn't help. :)
	- look into make recognized words using regex expressions