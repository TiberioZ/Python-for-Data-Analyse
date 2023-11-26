import pandas as pd 

class Conversion():

    def get_value_from_age_group(self, age_group: str):
        age_mapping = {
            '18-24': -0.95197,
            '25-34': -0.07854,
            '35-44': 0.49788,
            '45-54': 1.09449,
            '55-64': 1.82213,
            '65+': 2.59171
        }

        result = age_mapping.get(age_group, None)
        return result
    

    def get_value_from_gender(gender:str):
        gender_mapping = {
            'Female': 0.48246,
            'Male': -0.48246
        }

        return gender_mapping.get(gender, None)
    
    
    def get_education_value(education_meaning:str):
        education_mapping = {
            'Left school before 16 years': -2.43591,
            'Left school at 16 years': -1.73790,
            'Left school at 17 years': -1.43719,
            'Left school at 18 years': -1.22751,
            'Some college or university, no certificate or degree': -0.61113,
            'Professional certificate/diploma': -0.05921,
            'University degree': 0.45468,
            'Masters degree': 1.16365,
            'Doctorate degree': 1.98437
        }

        return education_mapping.get(education_meaning, None)
    

    def get_country_value(country_meaning:str):
        country_mapping = {
            'Australia': -0.09765,
            'Canada': 0.24923,
            'New Zealand': -0.46841,
            'Other': -0.28519,
            'Republic of Ireland': 0.21128,
            'UK': 0.96082,
            'USA': -0.57009
        }

        return country_mapping.get(country_meaning, None)
    
    def get_ethnicity_value(ethnicity_meaning):
        ethnicity_mapping = {
            'Asian': -0.50212,
            'Black': -1.10702,
            'Mixed-Black/Asian': 1.90725,
            'Mixed-White/Asian': 0.12600,
            'Mixed-White/Black': -0.22166,
            'Other': 0.11440,
            'White': -0.31685
        }

        return ethnicity_mapping.get(ethnicity_meaning, None)
    

    def get_nscore_value(nscore_meaning):
        nscore_mapping = {
            12: -3.46436,
            13: -3.15735,
            14: -2.75696,
            15: -2.52197,
            16: -2.42317,
            17: -2.34360,
            18: -2.21844,
            19: -2.05048,
            20: -1.86962,
            21: -1.69163,
            22: -1.55078,
            23: -1.43907,
            24: -1.32828,
            25: -1.19430,
            26: -1.05308,
            27: -0.92104,
            28: -0.79151,
            29: -0.67825,
            30: -0.58016,
            31: -0.46725,
            32: -0.34799,
            33: -0.24649,
            34: -0.14882,
            35: -0.05188,
            36: 0.04257,
            37: 0.13606,
            38: 0.22393,
            39: 0.31287,
            40: 0.41667,
            41: 0.52135,
            42: 0.62967,
            43: 0.73545,
            44: 0.82562,
            45: 0.91093,
            46: 1.02119,
            47: 1.13281,
            48: 1.23461,
            49: 1.37297,
            50: 1.49158,
            51: 1.60383,
            52: 1.72012,
            53: 1.83990,
            54: 1.98437,
            55: 2.12700,
            56: 2.28554,
            57: 2.46262,
            58: 2.61139,
            59: 2.82196,
            60: 3.27393
        }

        return nscore_mapping.get(nscore_meaning, None)
    

    def get_escore_value(escore_meaning):
        escore_mapping = {
            16: -3.27393,
            17: -3.10,
            18: -3.00537,
            19: -2.72827,
            20: -2.53830,
            21: -2.44904,
            22: -2.32338,
            23: -2.21069,
            24: -2.11437,
            25: -2.03972,
            26: -1.92173,
            27: -1.76250,
            28: -1.63340,
            29: -1.50796,
            30: -1.37639,
            31: -1.23177,
            32: -1.09207,
            33: -0.94779,
            34: -0.80615,
            35: -0.69509,
            36: -0.57545,
            37: -0.43999,
            38: -0.30033,
            39: -0.15487,
            40: 0.00332,
            41: 0.16767,
            42: 0.32197,
            43: 0.47617,
            44: 0.63779,
            45: 0.80523,
            46: 0.96248,
            47: 1.11406,
            48: 1.28610,
            49: 1.45421,
            50: 1.58487,
            51: 1.74091,
            52: 1.93886,
            53: 2.12700,
            54: 2.32338,
            55: 2.57309,
            56: 2.85950,
            57: 2.95,
            58: 3.00537,
            59: 3.27393
        }

        return escore_mapping.get(escore_meaning, None)
    

    def get_oscore_value(oscore_meaning):
        oscore_mapping = {
            24: -3.27393,
            25: -3,
            26: -2.85950,
            27: -2.7,
            28: -2.63199,
            29: -2.39883,
            30: -2.21069,
            31: -2.09015,
            32: -1.97495,
            33: -1.82919,
            34: -1.68062,
            35: -1.55521,
            36: -1.42424,
            37: -1.27553,
            38: -1.11902,
            39: -0.97631,
            40: -0.84732,
            41: -0.71727,
            42: -0.58331,
            43: -0.45174,
            44: -0.31776,
            45: -0.17779,
            46: -0.01928,
            47: 0.14143,
            48: 0.29338,
            49: 0.44585,
            50: 0.58331,
            51: 0.72330,
            52: 0.88309,
            53: 1.06238,
            54: 1.24033,
            55: 1.43533,
            56: 1.65653,
            57: 1.88511,
            58: 2.15324,
            59: 2.44904,
            60: 2.90161
        }

        return oscore_mapping.get(oscore_meaning, None)
    

    def convert_ascore_to_value(ascore):
        conversion_table = {
        12: -3.46436,
        13: -3.35,
        14: -3.22,
        15: -3.18,
        16: -3.15735,
        18: -3.00537,
        19: -2.98,
        20 : -2.96,
        21: -2.94,
        22: -2.92,
        23: -2.90161,
        24: -2.78793,
        25: -2.70172,
        26: -2.53830,
        27: -2.35413,
        28: -2.21844,
        29: -2.07848,
        30: -1.92595,
        31: -1.77200,
        32: -1.62090,
        33: -1.47955,
        34: -1.34289,
        35: -1.21213,
        36: -1.07533,
        37: -0.91699,
        38: -0.76096,
        39: -0.60633,
        40: -0.45321,
        41: -0.30172,
        42: -0.15487,
        43: -0.01729,
        44: 0.13136,
        45: 0.28783,
        46: 0.43852,
        47: 0.59042,
        48: 0.76096,
        49: 0.94156,
        50: 1.11406,
        51: 1.2861,
        52: 1.45039,
        53: 1.61108,
        54: 1.81866,
        55: 2.03972,
        56: 2.23427,
        57: 2.46262,
        58: 2.75696,
        59: 3.15735,
        60: 3.46436
        }

        # Example usage
        ascore = 34
        value = conversion_table.get(ascore)
        return value



    def convert_value_to_cscore(value):
        cscore_mapping = {
            17: -3.46436, 19: -3.15735, 20: -2.90161, 21: -2.72827, 22: -2.57309,
            23: -2.42317, 24: -2.30408, 25: -2.18109, 26: -2.04506, 27: -1.92173,
            28: -1.78169, 29: -1.64101, 30: -1.51840, 31: -1.38502, 32: -1.25773,
            33: -1.13788, 34: -1.01450, 35: -0.89891, 36: -0.78155, 37: -0.65253,
            38: -0.52745, 39: -0.40581, 40: -0.27607, 41: -0.14277, 42: -0.00665,
            43: 0.12331, 44: 0.25953, 45: 0.41594, 46: 0.58489, 47: 0.7583,
            48: 0.93949, 49: 1.13407, 50: 1.30612, 51: 1.46191, 52: 1.63088,
            53: 1.81175, 54: 2.04506, 55: 2.33337, 56: 2.63199, 57: 3.00537,
            59: 3.46436
        }

        return cscore_mapping.get(value, None)
    

    def convert_to_impulsiveness(score):
        conversion_table = {
            1: -2.55524,
            2: -1.37983,
            3: -0.71126,
            4: -0.21712,
            5: 0.19268,
            6: 0.52975,
            7: 0.88113,
            8: 1.29221,
            9: 1.86203,
            10: 2.90161
        }

        impulsiveness = conversion_table.get(score)
        return impulsiveness
    

    def convert_to_sensation_seeking(score):
        conversion_table = {
            1: -2.07848,
            2: -1.54858,
            3: -1.18084,
            4: -0.84637,
            5: -0.52593,
            6: -0.21575,
            7: 0.07987,
            8: 0.40148,
            9: 0.76540,
            10: 1.22470,
            11: 1.92173
        }

        sensation_seeking = conversion_table.get(score)
        return sensation_seeking



    
    
    
