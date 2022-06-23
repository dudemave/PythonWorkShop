#!/usr/bin/env python3

import sys

import  franco_machine
from franco_machine.limit_error import LimitError

from franco_machine.rate_table_data import usps_0_1, usps_0_2


usFM  = franco_machine.machine.machine(
    machine_type="PostBaseMini",
    company = 'usps',
    max_transaction_amount = 10000000,
    max_haben = 10000000,
    sw_version = '0.0.1',
    rate_table = usps_0_1,
)

usFM.load_money_amount(amount=1500000)
