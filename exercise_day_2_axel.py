#
vari="field0"
varj="field1"
vark="field2"
varl="field3"

myList = []
myList.append(vari)
myList.insert(1,varj)
myList += [vark]


print(myList)
print("\n ------- \n")
for i in myList:
    print(i)


print("\n ------- \n")