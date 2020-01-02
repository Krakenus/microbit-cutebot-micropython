# micro:bit Cutebot MicroPython library

Library providing functions to work with [Cutebot kit](https://www.elecfreaks.com/learn-en/microbitKit/smart_cutebot/cutebot_car.html) for BBC micro:bit board in Python language.

##  Prerequisites

- [BBC micro:bit board](https://www.elecfreaks.com/store/bbc-micro-bit-board-for-coding-programming.html)
- [Smart Cutebot kit](https://www.elecfreaks.com/store/elecfreaks-micro-bit-smart-cutebot-without-micro-bit.html)
- [uflash](https://github.com/ntoll/uflash)
- [microfs](https://github.com/ntoll/microfs)

## Usage

1. Connect you micro:bit board to you PC using USB cable
2. Flash MicroPython interpreter to you board using `uflash` command
3. Upload cutebot.py to you micro:bit using microfs
`ufs put cutebot.py`

After these steps you will be able to import the cutebot library like any other python module.

See python docstrings in `cutebot.py` for description of available functions.

```python
import cutebot
# or
from cutebot import *
```

Please note that every use of `uflash` or copying a new hex file will clear the board`s storage
so you will have to repeat step 3 after that.

## See also

- [micro:bit MicroPython documentation](https://microbit-micropython.readthedocs.io/en/latest/)
- `examples/` folder for python implementation of official examples (not all of them are ready yet).
- My [micro:bit scripts](https://github.com/Krakenus/microbit-micropython-scripts) repo
- [Difference](https://github.com/Krakenus/microbit-micropython-scripts#hex-firmware-and-mainpy) between uploading a hex file with program and a `main.py` using microfs
