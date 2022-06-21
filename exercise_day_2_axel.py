#
import datetime

vari="field0"
varj="field1"
vark="field2"
varl=datetime.datetime.fromisoformat('2020-03-11')

myList = []
myList.append(vari)
myList.insert(0,varj)
myList += [vark]
myList = myList + [varl]


print(myList)
print("\n ------- \n")
for i in myList:
    print(i)


print("\n ------- \n")
print (myList[0],myList[1],myList[2],myList[3])
