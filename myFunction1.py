#!/usr/bin/env python3

# myFunction

def MyFranking():
    franking_value = 100
    print(franking_value)

# main()
MyFranking()

####


def MyFranking2(franking_value):
    print(franking_value)

#

MyFranking2(20)

MyFranking2(0)

###

def MyFranking3(value1, value2):
    print(value1)
    print('--------')
    print(value2)


MyFranking3(12, 17)
###

def MyFranking4(value1=123, value2=999, text1='value'):
    print('------------------------------')
    print(text1, value1, text1, value2)


MyFranking4(244, 888, 'value:')

#####
MyFranking4(value1=333, value2=555)
