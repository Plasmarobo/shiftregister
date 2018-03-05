from shiftregister import ShiftRegister
import unittest

class TestShiftRegister(unittest.TestCase):

    def test_values(self):
        register = ShiftRegister(10,9,11)
        register.values = [1,0,1,0,1,0,1,0]
        self.assertSequenceEqual(register.values, [1,0,1,0,1,0,1,0])
        register.close()

    def test_shift(self):
        register = ShiftRegister(10,9,11)
        register.shift(1)
        register.shift(1)
        register.shift(0)
        self.assertSequenceEqual(register.values, [0,1,1,0,0,0,0,0])

    def test_show(self):
        register = ShiftRegister(10,9,11)
        register.shift(1)
        register.shift(0)
        register.show()
        self.assertSequenceEqual(register.values, [0,1,0,0,0,0,0,0])

if __name__ == '__main__':
    unittest.main()

