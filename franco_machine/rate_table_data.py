from franco_machine.rate_table import BaseRateTable


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



usps_0_1 = BaseRateTable(

    ver     = 0.1,
    company = 'usps',
    rates   = { "Std. Letter"   :  13000,
                "Invoice"       :  47000,
                "Market Lttr"   :  55000,
            }
    )


usps_0_2 = BaseRateTable(

    ver     = 0.2,
    company = 'usps',
    rates   = { "Std. Letter"   :  15500,
                "Invoice"       :  49000,
                "Market Lttr"   :  58000,
                 }
    )
