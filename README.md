# shiftregister
A small gpiozero extension to inclued the 74HCT595 shift register family in gpiozero.

## Example
Assuming Pin 10 is connected to SH_CP, Pin 9 is connected to ST_CP and Pin 11 is connected to DS
```
from shiftregister import ShiftRegister

register = ShiftRegister(10,9,11)
register.show() # Clear to zero
register.shift(1)
register.shift(0)
register.show()
```
