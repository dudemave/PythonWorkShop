

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

        machine_one.load_money_amount(100000)

        self.assertEqual(100000, machine_one.haben)
        self.assertEqual(100000, machine_one.total_register)

        machine_one.load_money_amount(5000000)

        self.assertEqual(5100000, machine_one.haben)
        self.assertEqual(5100000, machine_one.total_register)


    def test_frank(self):

        machine_one = franco_machine.machine.machine(
            machine_type="PostBaseMini",
            country = 'de',
            sw_version = '0.0.1'
            )

        machine_one.load_money_amount(100000)
        success = machine_one.frank_money_amount(2500)

        self.assertTrue(success)
        self.assertEqual( 97500, machine_one.haben)
        self.assertEqual(100000, machine_one.total_register)


    def test_frank_overdue(self):

        
        machine_one = franco_machine.machine.machine(
            machine_type="PostBaseMini",
            country = 'de',
            sw_version = '0.0.1'
            )

        machine_one.load_money_amount( 100000)
        success = machine_one.frank_money_amount(100001)

        self.assertFalse(success)


if __name__ == '__main__':
    unittest.main()
