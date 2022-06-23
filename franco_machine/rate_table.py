#

#   mvp - minimal valuable product

class BaseRateTable():

    def __init__(self, ver, company, rates):
        self.version = ver
        self.company = company

        self.rates   = rates #dict()

    # wird ein update hier gemacht?
    # def rt_update
    # Produkttabelle


dpag_0_1 = BaseRateTable(

    ver     = 0.1,
    company = 'dpag',
    rates   = { "Standard Letter" :   850,
                "Einschreiben"    :  1800,
                "Warensendung"    :  2700,
                 }
    )


dpag_0_2 = BaseRateTable(

    ver     = 0.2,
    company = 'dpag',
    rates   = { "Standard Letter" :   900,
                "Einschreiben"    :  2000,
                "Warensendung"    :  2700,
                 }
    )


#    "Standard Letter 100gr" 0.85#
#    "Einschreiben 50 gr"    1.80  #3500
#    "Einschreiben 150 gr"   2.70  #3500
#    "Einschreiben 500 gr"   3.50  #3500
