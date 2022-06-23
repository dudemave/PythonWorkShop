#
import sys

print()
print()
print("\t demonstration dictionaries and random")
import random
print()
print()

#random.seed(2)
#all_product_names = myMachine.rate_table.rates.keys()
all_prd = {
    "Standard Letter 100gr" :  0.85 ,
    "Einschreiben 50 gr"    :  1.80 ,
    "xyz 150 gr"   :  2.70 ,
    "abc 500 gr"   :  3.50 ,
    }

print(all_prd)
#print(all_prd_names.__dict__)
# xy = myMachine.rate_table.rates.values()
print(list(all_prd))
print(random.choice(list(all_prd)))
print(random.choice(list(all_prd)))
print(random.choice(list(all_prd)))
print(random.choice(list(all_prd)))
print(random.choice(list(all_prd)))
print(random.choice(list(all_prd)))
# 4 x wir ein zufäliger Wert des Dictionaries augegeben




print()
print("Items:")
for vv in all_prd.items():
    print(vv)
print()
print("Values:")
for vv in all_prd.values():
    print(vv)
print()
print("Keys:")
for vv in all_prd.keys():
    print(vv)
print()


print(all_prd['xyz 150 gr'])
assert all_prd['xyz 150 gr'] == 2.7

#for (int ii; ii:=0; ii<=10; ii++):


# range 0 - 10
for aa in range(10):
    print('aa:', aa)

print()

for bb in range(8,10):
    print('bb:', bb)


for cc in range(10,100, 10):
    print('cc:', cc)

del(cc) # remove cc from local scope/namespace

print()

for dd in range(100,10, -10):
    print('dd:', dd)

print ('xxxx')
for ee in range(100,10, 10): # bedingung ist nicht erfüllt
    print('ee:', ee)


my_list = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg']
my_str = "0123456789"

print(my_list[1:4])
print(my_str [1:4])


print(my_list[5:]) # bis zum ende
print(my_str [5:])

print(my_list[5:-1])  # letzte weglassen
print(my_str [5:-1])

print(my_list[5:-3])  # dritt letzte weglassen
print(my_str [5:-3])

print(my_list[:-1])  # vom ersten bis zum vorletzten
print(my_str [:-1])

my_list.pop(3) # dd verschwindet
print(my_list)

my_list.insert(3, 'xx')
print(my_list)

my_list.append('zz')
print(my_list)



# *args bedeutet entpacken aller erhaltenen argumente
def my_function_with_args(*args):
    print (type(args), ':', args)
    for arg in args:
        print (arg)

my_function_with_args(1,2,3,'vier')

# ** mehrfaches entpacken der Argumente
# ** dictionaries werden mit zwei Sternchen entpackt
def my_function_with_kwargs(**kwargs):
    print (type(kwargs), ':', kwargs)
    for key, arg in kwargs.items():
        print (key, arg)

my_function_with_kwargs(eins=1, zwei=2, drei=3, vier='four')


def my_pythonic_function(*args, **kwargs):


    for arg in args:
        print (arg)


    for key, arg in kwargs.items():
        print (key, arg)

print('##############################')

my_pythonic_function(1, 2, drei=3, vier='four')

### commandline parameter
###  python3 exercise_day_4_axel.py blub bla toll

# sdt input
user_input = input('schreib was !! :')
print()
print(user_input, type(user_input))

if __name__ == """__main__""":
    my_pythonic_function(sys.argv)
