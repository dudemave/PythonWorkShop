# #!/usr/bin/env python3


import  franco_machine

myMachine = franco_machine.machine.machine(
    machine_type="PostBaseMini",
    country = 'de',
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
