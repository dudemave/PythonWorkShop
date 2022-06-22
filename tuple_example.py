

"""tuple ist keine immutable (veränderliche) Liste, es ist ein fester Wert
    es wird benutzt wenn der Wert nicht wieder verändert werden soll
    bei Verwaltung von GRÖSSEREN Anzahlen von Listen ist die Performance besser
"""
my_tuple = ('Gräfestraße', 40)
my_tuple_2 = my_tuple


print("my_tuple_2:", my_tuple_2)
print("my_tuple:", my_tuple)



# das gibt einen Fehler
#my_tuple[1] = 44

street, number = my_tuple

print(my_tuple)



my_list = ['Gräfestraße', 40]
my_list[1] = '40a'

print(my_list)


street, number = *my_list

print(street, number)
