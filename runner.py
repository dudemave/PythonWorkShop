# #!/usr/bin/env python3
import sys

import  franco_machine
from franco_machine.limit_error import LimitError

# erzeuge eine Machine
myMachine = franco_machine.machine.machine(
    machine_type="PostBaseMini",
    country = 'de',
    max_transaction_amount = 10000000,
    max_haben = 10000000,
    sw_version = '0.0.1'
)

myMachine.load_money_amount(amount=500000)

# Aufladungsbetrag
transaction_amount = 100000

# Machine aufladen $100
transaction_succesfull, ret_msg = myMachine.load_money_amount(transaction_amount)

if transaction_succesfull:     #load succesfull
    print ("money loading succesfull")

else: # load not succesfull
    print(ret_msg)

# Abbuchung 1$
myMachine.frank_money_amount(1000)

print(myMachine.haben)


#try:
#    myMachine.load_money_amount(10000001)
#except LimitError, msg:
#    print("hurra es ist bescheiden schön")
#    sys.exit(msg)
