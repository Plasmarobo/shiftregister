# shiftregister
A small gpiozero extension to include the `74HCT595` shift register family in gpiozero.

## Example
Assuming Pin 9 is connected to `SH_CP` (clock), Pin 10 is connected to `ST_CP` (show/latch), and Pin 11 is connected to `DS` (data)

```python
from shiftregister import ShiftRegister

register = ShiftRegister(9, 10, 11)
register.show() # Clear to zero
register.shift(1)
register.shift(0)
register.show()
```
