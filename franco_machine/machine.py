#!/usr/bin/env python3

from franco_machine.limit_error import LimitError

class machine():


    def __init__(self,
                 machine_type,
                 country,
                 max_transaction_amount,
#                 max_haben,
                 sw_version ):

        self.machine_type=machine_type
        self.country=country
        self.sw_version=sw_version

        self.rate_table=[]
        self.rt_version=None

        self.postal_sn=None

        self.haben = 0                # r1
        self.verbrauch = 0            # r2
        self.total_register = 0       # r3

        # ToDo: upper limit
        self.max_transaction_amount = max_transaction_amount
#        self.max_haben = max_haben


    def load_money_amount(self, amount):
        # amount = 100

        # ToDo: type enforcement
        # ToDo: check ragne: not negative and upper limit
        #assert(self.max_transaction_amount > amount ), \
        #'too much money loaded'
        if self.max_transaction_amount < amount:

            raise LimitError(('Transaction amount is greater than max '
                              f'({self.max_transaction_amount})'))

        # haben register darf nie den max_haben überschreiten



        self.haben          += amount
        self.total_register += amount

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
