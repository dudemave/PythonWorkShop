class DummyMachine():

    def __init__(self):
        pass

    def process_user_input(self, *args):

        print ('xxx', args[0])

        price     = 7.5
        zone_fine = 4.5

        if args[0][0] != args[0][1]:
            price += zone_fine


        result = ('FirstCl.LetterLetter',  price, '4711')


        return result
