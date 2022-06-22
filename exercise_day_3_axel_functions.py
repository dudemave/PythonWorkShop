#
import datetime

# keine Parameter Übergabe möglich
def function1():
    print()
    #print("function parameter: \"",myarg,"\" ????")
    print("function 1 parameter 1: \"myarg\" !!" )

    return True

# beste variante für parameter 1
# - es erhält einen vordefinierten Wert wenn nichts übergeben wird
def function2(myarg1=42,p2=None, p3=None):
    print("function 2 parameter 1: \""+str(myarg1)+"\" ...." )
    print("function 2 parameter 1: \"%s\" ...." % myarg1)
    if p2 != None:
        print("  function 2 parameter 2: \"%s\" ....%s" % (p2, "addStuff"))
    print("  function 2 parameter 3: \"%s\" ...." % p3)
    return False

print(function1())
#print(function1(878787))    # geht nicht
print()

print(function2("juhu 47110815"))   # 1 parameter
print(function2())                  # ohne Parameter
print(function2(34622,"test"))      # 2 Parameter
print(function2(34622,"Hurdi Schmurr"))      # 2 Parameter
print(function2(34622,"Eine schöne Sache wär' ...."))      # 2 Parameter
print(function2(34622,"keene Ahnung",789))      # 2 Parameter

print(function2(p3=34622,myarg1="keene Ahnung",p2=789))      # with definition in any order

print()
x=6646544
print(f'test behavior strings: "{x}" !!!')  # dies funktioniert erst ab python 3.8
x="Test String"
print(f'test behavior strings: "{x}" !!!')

name="Supername"
score=545454
print("Total score for %s is %s  " % (name, score))
