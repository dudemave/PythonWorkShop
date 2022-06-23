# #!/usr/bin/env python3

import  franco_machine


from franco_machine.limit_error import LimitError
from franco_machine.rate_table_data import dpag_0_1, dpag_0_2
from franco_machine.customer import Customer



# erzeuge eine Machine
myMachine = franco_machine.machine.machine(
    machine_type="PostBaseMini",
    company = 'dpag',
    max_transaction_amount = 10000000,
    max_haben = 10000000,
    sw_version = '0.0.1',
    rate_table = dpag_0_1,
)

customer = Customer(myMachine=myMachine, verbose=True)

# Aufladungsbetrag
transaction_amount = 100000

# Machine aufladen $100
transaction_succesfull, ret_msg = myMachine.load_money_amount(
                                            transaction_amount)


myMachine.frank_product('Standard Letter') # 599150
myMachine.frank_product('Einschreiben')    # 597350


print(myMachine.haben)

myMachine.update_rate_table(dpag_0_2)

myMachine.frank_product('Standard Letter') # 596450






customer.frank_down()




#print(myMachine.haben)
