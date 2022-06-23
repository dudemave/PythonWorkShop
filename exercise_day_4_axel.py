#
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
