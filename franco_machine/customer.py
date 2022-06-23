import random

#random.seed(2)

class Customer():

    def __init__(self, myMachine, verbose=False):
        self.myMachine = myMachine
        self.verbose   = verbose

    def frank_down(self):

        all_product_names = self.myMachine.rate_table.rates.keys()

        def get_next_product():
            return random.choice(list(all_product_names))

        next_product = get_next_product()

        while self.myMachine.frank_product(next_product):

            if self.verbose:
                print (self.myMachine.haben, next_product, end='')

            next_product = get_next_product()

            if self.verbose:
                print ((f'            {next_product} :'
                        f' {self.myMachine.rate_table.rates[next_product]} '))
