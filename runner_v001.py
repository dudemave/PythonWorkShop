# #!/usr/bin/env python3
import sys

import  franco_machine
from franco_machine.limit_error import LimitError


# eine Machine erzeugen
myMachine = franco_machine.machine.machine(
    machine_type="PostBaseMini",
    country = 'de',
    max_transaction_amount = 10000000,
    max_haben = 10000000,
    sw_version = '0.0.1'
)



# Machine mit 500$ auflanden
myMachine.load_money_amount(amount=500000)


transaction_amount = 10000001

# return wert ist ein tuple, welches hier entpackt wurde
transaction_succesfull, ret_msg = myMachine.load_money_amount(transaction_amount)

print (transaction_succesfull)

if transaction_succesfull:
    #load succesfull
    pass

else:
    # load not succesfull
    print(ret_msg)

# frankieren 1$
myMachine.frank_money_amount(1000)


#try:
#    myMachine.load_money_amount(10000001)
#except LimitError, msg:
#    print("hurra es ist bescheiden schön")
#    sys.exit(msg)
