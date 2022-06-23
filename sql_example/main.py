import sqlite3

from pathlib import Path

from dummy_machine import DummyMachine

db_file_name = 'example.db'
db_path = Path.cwd() / db_file_name

if db_path.exists():
    db_path.unlink()  # removes old db file

con = sqlite3.connect('example.db')

cur = con.cursor()

cur.execute('''CREATE TABLE test_cases_rt212
               (menuCode text, weight real, origne text, destination text, product_name text,  price real, product_code text)''')

#cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
#cur.execute("INSERT INTO stocks VALUES ('2022-12-24','Get','XYZ',123, 45.67)")
#cur.execute("INSERT INTO stocks VALUES ('2020-05-12','Get','SGD',456, 32.49)")

"""

MenuEbenen Produktname                Weight  Preis   ProdCode
1-1-1      FirstCl.LetterLetter           5    7.5    4711
1-1-2      FirstCl.LetterLargeLetter      5    9.3    815
5-6-1      InterntlRegMailReturnReceipt   5    9.95   9367
"""


#MenuEbenen Produktname                Weight  Preis   ProdCode
cur.execute("INSERT INTO test_cases_rt212 VALUES ('1-1-1', 5, 'NY', 'NY', 'FirstCl.LetterLetter',  7.5, '4711')")
cur.execute("INSERT INTO test_cases_rt212 VALUES ('1-1-1', 5, 'NY', 'UT', 'FirstCl.LetterLetter',  12., '4711')")
cur.execute("INSERT INTO test_cases_rt212 VALUES ('1-1-2', 5, 'NY', 'NY', 'FirstCl.LetterLargeLetter',  9.3, '815')")
cur.execute("INSERT INTO test_cases_rt212 VALUES ('5-6-1', 5, 'NY', 'NY', 'InterntlRegMailReturnReceipt',  9.95, '9367')")

# Save (commit) the changes
con.commit()

########################################################

"""
für jeden eintrag in der Datenbank
führe einen Test mit dem Gerät druch

"""

# hole alle datenbank / testeinträge

myDummyMachine = DummyMachine()

cur.execute("SELECT * FROM test_cases_rt212;")
all_tests = cur.fetchall()    # xx = cur.fetchone()

good_tests = []
bad_tests = []

def calculate_zones(org, dest):

    number_of_zones =0

    if org != dest:
        number_of_zones = 9


for test_data in all_tests:

    test_input = test_data[2:]
    print(test_input)
    test_result = myDummyMachine.process_user_input(test_input)
    #print (test_result)
#    print(test_result[0], test_data[2])



    if (test_result[0] == test_data[4]
        and
        test_result[1] == test_data[5]
        and
        test_result[2] == test_data[6]
        ):

        good_tests.append(test_data)



    else:
        bad_tests.append(test_data)

    #print(all_tests)
    #print(test_data)
    #print(test_result)


print()
print (f'tests passed: {len(good_tests)}')

#print(good_tests)
print('###################')
print(bad_tests)

#print(xx[-1][3])
