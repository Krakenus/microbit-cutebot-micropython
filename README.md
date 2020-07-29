# BBC micro:bit Cutebot MicroPython library

Library providing functions to work with [Cutebot kit](https://www.elecfreaks.com/learn-en/microbitKit/smart_cutebot/cutebot_car.html) for BBC micro:bit board in Python language.

##  Prerequisites

- [BBC micro:bit board](https://www.elecfreaks.com/store/bbc-micro-bit-board-for-coding-programming.html)
- [Smart Cutebot kit](https://www.elecfreaks.com/store/elecfreaks-micro-bit-smart-cutebot-without-micro-bit.html)

## Usage

See python docstrings in `cutebot.py` for description of available functions.

There are several methods how to flash your Python program to micro:bit board. 
Some of these methods are described below. All of them has been tested recently.  
After these steps you will be able to import the cutebot library like any other python module.

```python
import cutebot
# or
from cutebot import *
```

There is always possibility to simply copy content of the `cutebot.py` above your Python code without importing the module.
It will work, however **this way is not recommended**. 
Micro:bit is designed to help people learn to program so **do not learn bad practices**. 

### Online editor

[Official online editor](https://python.microbit.org/v/2.0). 

No additional tools are required. Just a web browser of your choice.

1. Connect you micro:bit board to you PC using USB cable
2. Click the `Load/Save` button
3. Add `cutebot.py` to project files
4. Write your code in editor
5. Click the `Connect` button, then click the `Flash` button (in Chromium based browsers) OR download the hex file and copy it to your micro:bit.


### Mu editor (best for beginners)

Simple Python editor. This method looks similar to the previous one but this editor is available offline.

Prerequisites:

- [Mu editor](https://codewith.mu/en/)

1. Connect you micro:bit board to you PC using USB cable
2. Start Mu editor in micro:bit mode
3. Copy `cutebot.py` to `mu_code` folder in your home directory (after that it will be listed in `Files`)
4. Click the `Files` button
5. Drag and drop `cutebot.py` in the left box
6. Write your code in editor
7. Click the `Flash` button


### CLI (for advanced users, suitable for scripts)

Prerequisites:

- [uflash](https://github.com/ntoll/uflash)
- [microfs](https://github.com/ntoll/microfs)

These are the same command line tools the Mu editor uses in background.

1. Connect you micro:bit board to you PC using USB cable
2. Flash MicroPython interpreter to you board using `uflash` command
3. Upload cutebot.py to you micro:bit using microfs `ufs put cutebot.py`
4. Upload you program (the name `main.py` is required) `ufs put main.py`

Please note that every use of `uflash` or copying a new hex file will clear the board's storage
so your .py files copied with `ufs` will be deleted.

## See also

- [micro:bit MicroPython documentation](https://microbit-micropython.readthedocs.io/en/latest/)
- `examples/` folder for python implementation of [official examples](https://www.elecfreaks.com/learn-en/microbitKit/smart_cutebot/cutebot_case01.html) (not all of them are ready yet).
- My [micro:bit bakefile](https://github.com/Krakenus/microbit-micropython-bakefile) repo
- [Difference](https://github.com/Krakenus/microbit-micropython-bakefile#hex-firmware-and-mainpy) between uploading a hex file with program and a `main.py` using microfs
