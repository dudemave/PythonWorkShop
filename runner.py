# #!/usr/bin/env python3
import sys

import  franco_machine
from franco_machine.limit_error import LimitError

myMachine = franco_machine.machine.machine(
    machine_type="PostBaseMini",
    country = 'de',
    max_transaction_amount = 10000000,
    sw_version = '0.0.1'
)


print(myMachine.__dict__)

print(myMachine.haben)
myMachine.load_money_amount(10000)
print(myMachine.haben)
myMachine.load_money_amount(amount=500000)
print(myMachine.haben)

print(myMachine.__dict__)


myMachine.frank_money_amount(1000)

transaction_amount = 10000001

if myMachine.load_money_amount(transaction_amount):
    #load succesfull
    pass

else:
    # load not succesfull
    pass

try:
    myMachine.load_money_amount(10000001)
except LimitError, msg:
    print("hurra es ist bescheiden schön")
    sys.exit(msg)

print('xxx')
