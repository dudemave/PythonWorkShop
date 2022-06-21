

import unittest

import  franco_machine



class TestMachineMethods(unittest.TestCase):

    def test_init_haben(self):

        machine_one = franco_machine.machine.machine(
            machine_type="PostBaseMini",
            country = 'de',
            sw_version = '0.0.1'
        )

        self.assertEqual(0, machine_one.haben)
    #    self.assertEqual(0, machine_one.total_register)



    def test_init_haben_2(self):

        machine_one = franco_machine.machine.machine(
            machine_type="PostBaseMini",
            country = 'de',
            sw_version = '0.0.1'
        )

        machine_one.load_money_amount(100)

        self.assertEqual(100, machine_one.haben)
        self.assertEqual(100, machine_one.total_register)

        machine_one.load_money_amount(5000)

        self.assertEqual(5100, machine_one.haben)
        self.assertEqual(5100, machine_one.total_register)


if __name__ == '__main__':
    unittest.main()
