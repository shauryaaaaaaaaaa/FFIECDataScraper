class TopBankSubsidiaries:
    def getData():
        JPMorganChase = ["CHASE BANK OF TEXAS-SAN ANGELO, NATIONAL ASSOCIATION",
                         "CHASE BANK USA, NATIONAL ASSOCIATION",
                         "CHASE MANHATTAN BANK AND TRUST COMPANY, NATIONAL ASSOCIATION",
                         "CHASE MANHATTAN BANK USA, NATIONAL ASSOCIATION",
                         "CHASE MANHATTAN BANK, THE",
                         "CHASE MANHATTAN PRIVATE BANK, NATIONAL ASSOCIATION",
                         "CHASE MANHATTAN TRUST COMPANY, NATIONAL ASSOCIATION",
                         "JPMORGAN BANK AND TRUST COMPANY, NATIONAL ASSOCIATION",
                         "JPMORGAN CHASE BANK",
                         "JPMORGAN CHASE BANK, DEARBORN",
                         "JPMORGAN CHASE BANK, NATIONAL ASSOCIATION"]
        
        BankOfAmerica = ["BANK OF AMERICA CALIFORNIA, NATIONAL ASSOCIATION",
                         "BANK OF AMERICA GEORGIA, NATIONAL ASSOCIATION",
                         "BANK OF AMERICA NATIONAL TRUST DELAWARE",
                         "BANK OF AMERICA OREGON, NATIONAL ASSOCIATION",
                         "BANK OF AMERICA RHODE ISLAND, NATIONAL ASSOCIATION",
                         "BANK OF AMERICA TRUST COMPANY OF DELAWARE, NATIONAL ASSOCIATION",
                         "BANK OF AMERICA, NATIONAL ASSOCIATION",
                         "BANK OF AMERICA, NATIONAL ASSOCIATION (USA)"]
        
        CitiCorp = ["CITIBANK (BANAMEX USA)",
                    "CITIBANK (NEVADA), NATIONAL ASSOCIATION",
                    "CITIBANK (NEW YORK STATE)",
                    "CITIBANK (SOUTH DAKOTA), N.A.",
                    "CITIBANK (SOUTH DAKOTA), NATIONAL ASSOCIATION",
                    "CITIBANK DELAWARE",
                    "CITIBANK TEXAS, NATIONAL ASSOCIATION",
                    "CITIBANK USA",
                    "CITIBANK USA, NATIONAL ASSOCIATION",
                    "CITIBANK, N.A.",
                    "CITICORP TRUST DELAWARE, NATIONAL ASSOCIATION",
                    "CITICORP TRUST, NATIONAL ASSOCIATION",
                    "CITIGROUP TRUST - DELAWARE, NATIONAL ASSOCIATION"]
        
        WellsFargo = ["WELLS FARGO ALASKA TRUST COMPANY, NATIONAL ASSOCIATION",
                      "WELLS FARGO BANK ALASKA, NATIONAL ASSOCIATION",
                      "WELLS FARGO BANK ARIZONA, NATIONAL ASSOCIATION",
                      "WELLS FARGO BANK GRAND JUNCTION, NATIONAL ASSOCIATION",
                      "WELLS FARGO BANK GRAND JUNCTION-DOWNTOWN, NATIONAL ASSOCIATION",
                      "WELLS FARGO BANK ILLINOIS, NATIONAL ASSOCIATION",
                      "WELLS FARGO BANK INDIANA, NATIONAL ASSOCIATION",
                      "WELLS FARGO BANK IOWA, NATIONAL ASSOCIATION",
                      "WELLS FARGO BANK MICHIGAN, NATIONAL ASSOCIATION",
                      "WELLS FARGO BANK MINNESOTA, NATIONAL ASSOCIATION",
                      "WELLS FARGO BANK MONTANA, NATIONAL ASSOCIATION",
                      "WELLS FARGO BANK NEBRASKA, NATIONAL ASSOCIATION",
                      "WELLS FARGO BANK NEVADA, NATIONAL ASSOCIATION",
                      "WELLS FARGO BANK NEW MEXICO, NATIONAL ASSOCIATION",
                      "WELLS FARGO BANK NORTH DAKOTA, NATIONAL ASSOCIATION",
                      "WELLS FARGO BANK NORTHWEST, NATIONAL ASSOCIATION",
                      "WELLS FARGO BANK OHIO, NATIONAL ASSOCIATION",
                      "WELLS FARGO BANK SOUTH CENTRAL, NATIONAL ASSOCIATION",
                      "WELLS FARGO BANK SOUTH DAKOTA, NATIONAL ASSOCIATION",
                      "WELLS FARGO BANK TEXAS, NATIONAL ASSOCIATION",
                      "WELLS FARGO BANK WEST, NATIONAL ASSOCIATION",
                      "WELLS FARGO BANK WISCONSIN, NATIONAL ASSOCIATION",
                      "WELLS FARGO BANK WYOMING, NATIONAL ASSOCIATION",
                      "WELLS FARGO BANK, LTD.",
                      "WELLS FARGO BANK, NATIONAL ASSOCIATION",
                      "WELLS FARGO CENTRAL BANK",
                      "WELLS FARGO DELAWARE TRUST COMPANY, NATIONAL ASSOCIATION",
                      "WELLS FARGO FINANCIAL BANK",
                      "WELLS FARGO FINANCIAL NATIONAL BANK",
                      "WELLS FARGO HSBC TRADE BANK, NATIONAL ASSOCIATION",
                      "WELLS FARGO LIMITED,WELLS FARGO NATIONAL BANK WEST",
                      "WELLS FARGO TRUST COMPANY, NATIONAL ASSOCIATION"]
        
        GoldmanSachs = ["GOLDMAN SACHS BANK USA",
                        "GOLDMAN SACHS TRUST COMPANY, NATIONAL ASSOCIATION, THE",
                        "GOLDMAN SACHS TRUST COMPANY, THE NATIONAL ASSOCIATION"]
        
        MorganStanley = ["MORGAN STANLEY BANK",
                         "MORGAN STANLEY BANK, N.A.",
                         "MORGAN STANLEY DEAN WITTER BANK, INC.",
                         "MORGAN STANLEY PRIVATE BANK, NATIONAL ASSOCIATION",
                         "MORGAN STANLEY TRUST NATIONAL ASSOCIATION"]
        
        USBancorp = ["U.S. BANK,U.S. BANK NATIONAL ASSOCIATION",
                     "U.S. BANK NATIONAL ASSOCIATION MT",
                     "U.S. BANK NATIONAL ASSOCIATION ND",
                     "U.S. BANK NATIONAL ASSOCIATION OR",
                     "U.S. BANK TRUST COMPANY, NATIONAL ASSOCIATION",
                     "U.S. BANK TRUST NATIONAL ASSOCIATION",
                     "U.S. BANK TRUST NATIONAL ASSOCIATION MT",
                     "U.S. BANK TRUST NATIONAL ASSOCIATION SD"]
        
        TruistFinancial = ["TRUIST BANK",
                           "SUNTRUST BANK",
                           "SUNTRUST BANKCARD, NATIONAL ASSOCIATION",
                           "BB&T BANKCARD CORPORATION",
                           "BB&T FINANCIAL, FSB"]
        
        PNC = ['PNC BANK, DELAWARE',
              'PNC BANK, NATIONAL ASSOCIATION']
        
        BMOHarris = ['BMO HARRIS BANK NATIONAL ASSOCIATION',
                    'BMO HARRIS CENTRAL NATIONAL ASSOCIATION']
        
        KeyBank = ["KEY BANK AND TRUST",
                   "KEY BANK USA, NATIONAL ASSOCIATION",
                   "KEY NATIONAL TRUST COMPANY OF DELAWARE",
                   "KEYBANK NATIONAL ASSOCIATION"]
        
        Northern = ["NORTHERN TRUST BANK OF ARIZONA, NATIONAL ASSOCIATION",
                    "NORTHERN TRUST BANK OF CALIFORNIA, NATIONAL ASSOCIATION",
                    "NORTHERN TRUST BANK OF COLORADO",
                    "NORTHERN TRUST BANK OF FLORIDA N.A.",
                    "NORTHERN TRUST BANK OF TEXAS N.A.",
                    "NORTHERN TRUST BANK, NATIONAL ASSOCIATION",
                    "NORTHERN TRUST COMPANY OF NEW YORK",
                    "NORTHERN TRUST COMPANY OF NEW YORK, THE",
                    "NORTHERN TRUST COMPANY, THE",
                    "NORTHERN TRUST INVESTMENTS, NATIONAL ASSOCIATION",
                    "NORTHERN TRUST, NATIONAL ASSOCIATION"]
        
        Ally = ['ALLY BANK',
               'GMAC AUTOMOTIVE BANK',
               'GMAC BANK',
               'GMAC COMMERCIAL MORTGAGE BANK']
        
        CitizensBank = ["CITIZENS BANK",
                        "CITIZENS' BANK",
                        "CITIZENS BANK - WAKULLA",
                        "CITIZENS BANK & SAVINGS COMPANY",
                        "CITIZENS BANK & TRUST",
                        "CITIZENS BANK & TRUST CO.",
                        "CITIZENS BANK & TRUST CO. OF JACKSON",
                        "CITIZENS BANK & TRUST CO., HUTCHINSON, MINN.",
                        "CITIZENS BANK & TRUST COMPANY",
                        "CITIZENS BANK & TRUST COMPANY IN ST. PAUL",
                        "CITIZENS BANK & TRUST COMPANY OF ARDMORE",
                        "CITIZENS BANK & TRUST COMPANY OF CHICAGO",
                        "CITIZENS BANK & TRUST COMPANY OF VIVIAN, LOUISIANA",
                        "CITIZENS BANK (KY), INC",
                        "CITIZENS BANK AND TRUST",
                        "CITIZENS BANK AND TRUST COMPANY",
                        "CITIZENS BANK AND TRUST COMPANY OF GRAINGER COUNTY",
                        "CITIZENS BANK AND TRUST COMPANY OF GRAYSON COUNTY, THE",
                        "CITIZENS BANK AND TRUST OF WEST GEORGIA",
                        "CITIZENS BANK AND TRUST, INC.",
                        "CITIZENS BANK COMPANY, THE",
                        "CITIZENS BANK IN LOUP CITY",
                        "CITIZENS BANK MINNESOTA",
                        "CITIZENS BANK NEW HAMPSHIRE",
                        "CITIZENS BANK OF ADA",
                        "CITIZENS BANK OF ALBANY",
                        "CITIZENS BANK OF AMERICUS",
                        "CITIZENS BANK OF ASHVILLE, OHIO, THE",
                        "CITIZENS BANK OF BLOUNT COUNTY",
                        "CITIZENS BANK OF BLYTHEDALE",
                        "CITIZENS BANK OF CAMPBELL COUNTY, INC.",
                        "CITIZENS BANK OF CAPE VINCENT",
                        "CITIZENS' BANK OF CHARLESTON",
                        "CITIZENS BANK OF CHATSWORTH",
                        "CITIZENS BANK OF CLOVIS, THE",
                        "CITIZENS BANK OF COCHRAN, THE",
                        "CITIZENS BANK OF CONNECTICUT",
                        "CITIZENS BANK OF CUMBERLAND COUNTY, INC.",
                        "CITIZENS BANK OF DE GRAFF, THE",
                        "CITIZENS BANK OF EAST TENNESSEE, THE",
                        "CITIZENS BANK OF EDINA, THE",
                        "CITIZENS BANK OF EDINBURG",
                        "CITIZENS BANK OF EDMOND, THE",
                        "CITIZENS BANK OF EFFINGHAM",
                        "CITIZENS BANK OF ELDON",
                        "CITIZENS BANK OF FAYETTE, THE",
                        "CITIZENS BANK OF FLORIDA",
                        "CITIZENS BANK OF FORSYTH COUNTY, THE",
                        "CITIZENS BANK OF FROSTPROOF",
                        "CITIZENS BANK OF GAINESBORO",
                        "CITIZENS BANK OF GEORGIA, THE",
                        "CITIZENS BANK OF HIGGINSPORT, OHIO, THE",
                        "CITIZENS BANK OF JESSAMINE COUNTY",
                        "CITIZENS BANK OF KANSAS",
                        "CITIZENS BANK OF KANSAS, NATIONAL ASSOCIATION",
                        "CITIZENS BANK OF KENTUCKY, INC",
                        "CITIZENS BANK OF LAS CRUCES",
                        "CITIZENS BANK OF LOGAN, THE",
                        "CITIZENS BANK OF LONDON, THE",
                        "CITIZENS BANK OF MASSACHUSETTS",
                        "CITIZENS BANK OF MORGANTOWN, INC",
                        "CITIZENS BANK OF MUKWONAGO",
                        "CITIZENS BANK OF NEVADA COUNTY",
                        "CITIZENS BANK OF NEW ULM",
                        "CITIZENS BANK OF NEWBURG",
                        "CITIZENS BANK OF NORBORNE",
                        "CITIZENS BANK OF NORTHERN CALIFORNIA",
                        "CITIZENS BANK OF NORTHERN KENTUCKY, INC.",
                        "CITIZENS BANK OF OKLAHOMA",
                        "CITIZENS BANK OF OREGON, THE",
                        "CITIZENS BANK OF OVIEDO, THE",
                        "CITIZENS BANK OF PAGOSA SPRINGS",
                        "CITIZENS BANK OF PENNSYLVANIA",
                        "CITIZENS BANK OF PERRY, THE",
                        "CITIZENS BANK OF PHILADELPHIA, THE",
                        "CITIZENS BANK OF PRINCETON",
                        "CITIZENS BANK OF RHODE ISLAND",
                        "CITIZENS BANK OF ROGERSVILLE",
                        "CITIZENS BANK OF SOUTHERN PENNSYLVANIA",
                        "CITIZENS BANK OF SPARTA, THE",
                        "CITIZENS BANK OF SPENCER",
                        "CITIZENS BANK OF SWAINSBORO, THE",
                        "CITIZENS BANK OF TEXAS, NATIONAL ASSOCIATION",
                        "CITIZENS BANK OF THE OZARKS,CITIZENS BANK OF THE SOUTH",
                        "CITIZENS BANK OF VALLEY HEAD, THE",
                        "CITIZENS BANK OF WASHINGTON COUNTY",
                        "CITIZENS BANK OF WEIR, KANSAS, THE",
                        "CITIZENS BANK OF WEST VIRGINIA, INC.",
                        "CITIZENS BANK OF WESTON, INC., THE",
                        "CITIZENS BANK OF WINFIELD, THE",
                        "CITIZENS BANK WEALTH MANAGEMENT, NATIONAL ASSOCIATION",
                        "CITIZENS BANK, INC.",
                        "CITIZENS' BANK, INC.",
                        "CITIZENS BANK, N.A.",
                        "CITIZENS BANK, NATIONAL ASSOCIATION",
                        "CITIZENS BANK, THE",
                        "CITIZEN'S BANK, VILLE PLATTE, LOUISIANA",
                        "CITIZENS BANK-ILLINOIS, NATIONAL ASSOCIATION"]
        
        FifthThird = ["FIFTH THIRD BANK",
                      "FIFTH THIRD BANK, FLORIDA",
                      "FIFTH THIRD BANK, INDIANA",
                      "FIFTH THIRD BANK, KENTUCKY, INC.",
                      "FIFTH THIRD BANK, N.A.",
                      "FIFTH THIRD BANK, NATIONAL ASSOCIATION",
                      "FIFTH THIRD BANK, NORTHERN KENTUCKY, INC."]
        
        StateStreet = ["STATE STREET BANK AND TRUST COMPANY",
                       "STATE STREET BANK AND TRUST COMPANY OF CALIFORNIA, N.A.",
                       "STATE STREET BANK AND TRUST COMPANY OF CONNECTICUT, N.A.",
                       "STATE STREET BANK AND TRUST COMPANY OF MISSOURI, N.A.",
                       "STATE STREET BANK AND TRUST COMPANY OF NEW ENGLAND, NATIONAL ASSOCIATION",
                       "STATE STREET BANK AND TRUST COMPANY OF NEW HAMPSHIRE, N.A.",
                       "STATE STREET BANK AND TRUST COMPANY, N.A.","STATE STREET GLOBAL ADVISORS, N.A."]
        
        HSBC = ["HSBC BANK & TRUST COMPANY (DELAWARE), NATIONAL ASSOCIATION",
                "HSBC BANK NEVADA, NATIONAL ASSOCIATION",
                "HSBC BANK USA",
                "HSBC BANK USA, NATIONAL ASSOCIATION",
                "HSBC NATIONAL BANK USA",
                "HSBC TRUST COMPANY (DELAWARE), NATIONAL ASSOCIATION"]
        
        CharlesSchwab = ["CHARLES SCHWAB BANK",
                         "CHARLES SCHWAB BANK, NATIONAL ASSOCIATION",
                         "CHARLES SCHWAB BANK, SSB",
                         "CHARLES SCHWAB PREMIER BANK",
                         "CHARLES SCHWAB PREMIER BANK, SSB",
                         "CHARLES SCHWAB SIGNATURE BANK",
                         "CHARLES SCHWAB TRUST BANK"]
        
        TIAA = ['TIAA, FSB',
               'TIAA-CREF TRUST COMPANY FSB']
        
        BNYMellon = ["BNY MELLON TRUST OF DELAWARE",
                     "BNY MELLON, NATIONAL ASSOCIATION",
                     "BNY WESTERN TRUST COMPANY",
                     "BNYM (DELAWARE)",
                     "MELLON 1ST BUSINESS BANK, NATIONAL ASSOCIATION",
                     "MELLON BANK (DE) NATIONAL ASSOCIATION",
                     "MELLON BANK, N.A.",
                     "MELLON PRIVATE TRUST COMPANY, NATIONAL ASSOCIATION",
                     "MELLON SECURITIES TRUST COMPANY",
                     "MELLON TRUST OF DELAWARE, NATIONAL ASSOCIATION",
                     "MELLON TRUST OF NEW ENGLAND NATIONAL ASSOCIATION",
                     "MELLON UNITED NATIONAL BANK"]
        
        CapitalOne = ['CAPITAL ONE BANK',
                     'CAPITAL ONE BANK (USA), NATIONAL ASSOCIATION',
                     'CAPITAL ONE, NATIONAL ASSOCIATION']
        
        TD = ['TD BANK USA, NATIONAL ASSOCIATION',
             'TD BANK, N.A.',
             'TD BANKNORTH, NATIONAL ASSOCIATION']
        
        Comerica = ['COMERICA BANK',
                   'COMERICA BANK & TRUST, NATIONAL ASSOCIATION',
                   'COMERICA BANK-CALIFORNIA',
                   'COMERICA BANK-TEXAS']
        
        banks = {'JPMorganChase': JPMorganChase,
                'BankOfAmerica': BankOfAmerica,
                'CitiBanks': CitiCorp,
                'WellsFargo': WellsFargo,
                'GoldmanSachs': GoldmanSachs,
                'MorganStanley': MorganStanley,
                'USBancorp': USBancorp,
                'TruistFinancial': TruistFinancial,
                'PNCBank': PNC,
                'BMOHarris': BMOHarris,
                'KeyBankBank': KeyBank,
                'NorthernTrust': Northern,
                'AllyBank': Ally,
                'CitizensBank': CitizensBank,
                'FifthThird': FifthThird,
                'StateStreet': StateStreet,
                'HSBCBank': HSBC,
                'CharlesSchwab': CharlesSchwab,
                'TIAABank': TIAA,
                'BNYMellon': BNYMellon,
                'CapitalOne': CapitalOne,
                'TorontoDominion': TD,
                'ComericaBank': Comerica}
        
        subsidiaries = [JPMorganChase, BankOfAmerica, CitiCorp, WellsFargo, GoldmanSachs, MorganStanley, USBancorp, TruistFinancial, PNC, BMOHarris, KeyBank, Northern, Ally, CitizensBank, FifthThird, StateStreet, HSBC, CharlesSchwab, TIAA, BNYMellon, CapitalOne, TD, Comerica]
        return banks, subsidiaries