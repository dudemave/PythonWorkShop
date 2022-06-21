#!/usr/bin/env python3



class machine():


    def __init__(self, machine_type, country, sw_version):

        self.machine_type=machine_type
        self.country=country
        self.sw_version=sw_version

        self.rate_table=[]
        self.rt_version=None

        self.postal_sn=None

        self.haben = 0
        self.verbrauch = None
        self.total_register = None

        # ToDo: upper limit


    def load_money_amount(self, amount):
        # amount = 100

        # ToDo: type enforcement
        # ToDo: check ragne: not negative and upper limit

        self.haben += amount
