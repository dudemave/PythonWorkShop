#!/usr/bin/env python3

import datetime

myVarName = 'Karl'
myVarDate = datetime.datetime.fromisoformat('2022-02-18')
myVarNumber = 1234556678
myVarOtherIndexNumber = 1212

myList = [myVarName, myVarDate, myVarNumber, myVarOtherIndexNumber]


class theNextClass():
    #double underscore = dunder

    def __init__(self, name_string):
        self.name = name_string

        self.say_my_name()


    def say_my_name(self):
        print(self.name)


def myFunction():
    """ this is a very cool function """


    for i in myList :
        print (i)

    print("Hallo")


##### put the object here
#theNextClass()
newObj = theNextClass('xxx')
secondObj = theNextClass('blub')

secondObj.say_my_name()

secondObj.my_second_name = 'bla'
print (secondObj.my_second_name)


print(myVarDate.year)

print (myList)



myFunction()
