#!/usr/bin/env python3

from franco_machine.limit_error import LimitError

class machine():


    def __init__(self,
                 machine_type,
                 country,
                 max_load_amount,
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
        self.max_load_amount = max_load_amount


    def load_money_amount(self, amount):
        # amount = 100

        # ToDo: type enforcement
        # ToDo: check ragne: not negative and upper limit
        assert(self.max_load_amount > amount ), \
        'too much money loaded'

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
