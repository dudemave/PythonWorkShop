

import unittest

import  franco_machine
from franco_machine.limit_error import LimitError


class TestMachineMethods(unittest.TestCase):

    def setUp(self):

        self.machine_one = franco_machine.machine.machine(
        machine_type="PostBaseMini",
        country = 'de',
        max_transaction_amount = 10000000,
        sw_version = '0.0.1'
        )


    def test_init_haben(self):


        self.assertEqual(0, self.machine_one.haben)




    def test_init_haben_2(self):



        self.machine_one.load_money_amount(100000)

        self.assertEqual(100000, self.machine_one.haben)
        self.assertEqual(100000, self.machine_one.total_register)

        self.machine_one.load_money_amount(5000000)

        self.assertEqual(5100000, self.machine_one.haben)
        self.assertEqual(5100000, self.machine_one.total_register)


    def test_frank(self):

        self.machine_one.load_money_amount(100000)
        success = self.machine_one.frank_money_amount(2500)

        self.assertTrue(success)
        self.assertEqual( 97500, self.machine_one.haben)
        self.assertEqual(100000, self.machine_one.total_register)



    def test_frank_overdue(self):

        self.machine_one.load_money_amount( 100000)
        success = self.machine_one.frank_money_amount(100001)

        self.assertFalse(success)


    def test_load_money_all_at_once(self):
        """ too much money - in a single money load process """


        with self.assertRaises(LimitError):
            self.machine_one.load_money_amount( 10000001)

    @unittest.skipIf(True, 'WIP')
    def test_load_money(self):
        """ too much money - in a multiple money load processes """

        with self.assertRaises(LimitError):
            self.machine_one.load_money_amount( 5000000)
            self.machine_one.load_money_amount( 5000000)
            self.machine_one.load_money_amount( 1)


if __name__ == '__main__':
    unittest.main()
