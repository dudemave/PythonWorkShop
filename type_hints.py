




sys.exit()


def greeting(name: str, strict=False) -> str :


    if type(name) != str and strict:
        raise TypeError

    return (f'Hallo {name}')



#def greeting(name: str) -> str:
#    return 'Hello ' + name


print(greeting('bösewicht'))


print(greeting(['bösewicht']))
print(greeting(['bösewicht','7465764']))
