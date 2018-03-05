from gpiozero import DigitalOutputDevice, CompositeDevice, SourceMixin

class ShiftRegister(SourceMixin, CompositeDevice):
    """
    Extends :class:`CompositeDevice` and represents a shift register
    compatable with 74HC595 devices. Uses 3 GPIO pins.

    Shift: Connect to SH_CP on IC
    Show: Connect to ST_CP on IC
    Data: Connect to DS on IC
    """

    def __init__(self, shift, show, data, pin_factory=None):
        if not all(p is not None for p in [shift, show, data]):
            raise GPIOPinMissing(
                    'Shift CLK, Show CLK, and Data pins must be provided'
                )
        PinClass = DigitalOutputDevice
        super(ShiftRegister, self).__init__(
            shift_device=PinClass(shift, pin_factory=pin_factory),
            show_device=PinClass(show, pin_factory=pin_factory),
            data_device=PinClass(data, pin_factory=pin_factory),
            _order=('shift_device','show_device','data_device'),
            pin_factory=pin_factory
        )
        self.register_values = [0,0,0,0,0,0,0,0]
        self.values = self.register_values

    @property
    def values(self):
        """
        Represents the current value of the shift register
        An array of 1s and 0s
        1 is on, 0 is off.
        """
        return self.register_values

    @values.setter
    def values(self, values):
        if not isinstance(values, list):
            raise OutputDeviceBadValue("Values should be a list")
        if not all(((p == 0) or (p == 1)) for p in values):
            raise OutputDeviceBadValue("Values should be 1 or 0")
        for v in values[::-1]:
            self.shift(v)
        self.show()

    def shift(self, value=0):
        """
        Shifts a 0 or 1 into the shift register
        """
        if (value == 0):
            self.data_device.off()
        elif (value == 1):
            self.data_device.on()
        else:
            raise OutputDeviceBadValue("Only 1 or 0 may be shifted")
        self.shift_device.on()
        self.shift_device.off()
        self.register_values.insert(0, value)
        self.register_values.pop()

    def show(self):
        """
        Updates the storage latch in the shift register.
        This expresses the results on the output pins.
        """
        self.show_device.on()
        self.show_device.off()

