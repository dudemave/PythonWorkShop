#!/usr/bin/env python3

from franco_machine.limit_error import LimitError

class machine():


    def __init__(self,
                 machine_type,
                 company,
                 max_transaction_amount,
                 max_haben,
                 sw_version,
                 rate_table = {} ):

        self.machine_type=machine_type
        self.company=company
        self.sw_version=sw_version

        self.rate_table=rate_table
        self.rt_version=None

        self.postal_sn=None

        self.haben = 0                # r1
        self.verbrauch = 0            # r2
        self.total_register = 0       # r3

        # ToDo: upper limit
        self.max_transaction_amount = max_transaction_amount
        self.max_haben = max_haben


    def load_money_amount(self, amount):
        # amount = 100

        # ToDo: type enforcement
        # ToDo: check ragne: not negative and upper limit
        #assert(self.max_transaction_amount > amount ), \
        #'too much money loaded'



        if self.max_transaction_amount < amount:

            msg = ('Transaction amount is greater than max '
            f'({self.max_transaction_amount})')

            return (False , msg)

        elif self.haben + amount > self.max_haben:

            msg = 'the amount of money exceeds the limit'

            return (False, msg)


        else:
            self.haben          += amount
            self.total_register += amount
            return (True, '')


        #    raise LimitError(('Transaction amount is greater than max '
        #                      f'({self.max_transaction_amount})'))



    def frank_money_amount(self, amount):

        success = False

        if self.haben >= amount:

            self.haben          -= amount
            self.verbrauch      += amount

            success = True

        else:

            success = False

        # assure total balance is given # ToDo replace by something more fancy
        assert (self.haben + self.verbrauch == self.total_register)

        return success

    def frank_product(self, product_name):

        #print(self.rate_table)


        amount = self.rate_table.rates[product_name]

        success = self.frank_money_amount(amount)

        return success

    def update_rate_table(self, new_rate_table):

        self.rate_table = new_rate_table
