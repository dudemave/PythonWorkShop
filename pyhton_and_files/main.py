import os, sys

from pathlib import Path


#print(os.getcwd())
print(Path.cwd())

file_name = 'data.csv'

file_name_as_path = Path(file_name)

my_path_obj = Path.cwd() / file_name
my_path_obj_2 = Path(Path.cwd() , file_name)
my_path_obj_3 = Path(Path.cwd() , file_name_as_path)


#print(my_path_obj)
#print(my_path_obj_2)
#print(my_path_obj_3)




p = Path.cwd()
#for xx in p.iterdir():
#    print (xx)


[ print (xx) for xx in p.iterdir() ]

myList =['aaa', 'bbb', 'ccc' ]

myUpperList = [ ii.upper() for ii in myList] # list comprehention

print (myUpperList)


# in current directory
