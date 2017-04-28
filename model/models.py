

class Investor(object):
    def __init__(self, id, budget=500):
        self.id = id
        self.budget = budget
        self.DH_DS16 = 0
        self.DH_RS16 = 0
        self.RH_DS16 = 0
        self.RH_RS16 = 0
        self.OTHER16 = 0

    def get_json(self):
        return {
            'id': self.id,
            'budget': self.budget,
            'DH_DS16': self.DH_DS16,
            'DH_RS16': self.DH_RS16,
            'RH_DS16': self.RH_DS16,
            'RH_RS16': self.RH_RS16,
            'OTHER16': self.OTHER16
            }


class Order(object):
    def __init__(self, day, investor_id, DH_DS16=0, DH_DS16_u_price=0, DH_RS16=0, DH_RS16_u_price=0, RH_DS16=0, RH_DS16_u_price=0, RH_RS16=0, RH_RS16_u_price=0, OTHER16=0, OTHER16_u_price=0):
        self.day = day
        self.investor_id = investor_id
        self.DH_DS16 = DH_DS16
        self.DH_DS16_u_price = DH_DS16_u_price
        self.DH_RS16 = DH_RS16
        self.DH_RS16_u_price = DH_RS16_u_price
        self.RH_DS16 = RH_DS16
        self.RH_DS16_u_price = RH_DS16_u_price
        self.RH_RS16 = RH_RS16
        self.RH_RS16_u_price = RH_RS16_u_price
        self.OTHER16 = OTHER16
        self.OTHER16_u_price = OTHER16_u_price
        self.price   = 0

    def get_json(self):
        return {
            'day': self.day ,
            'investor_id': self.investor_id ,
            'DH_DS16': self.DH_DS16 ,
            'DH_DS16_u_price': self.DH_DS16_u_price ,
            'DH_RS16': self.DH_RS16 ,
            'DH_RS16_u_price': self.DH_RS16_u_price ,
            'RH_DS16': self.RH_DS16 ,
            'RH_DS16_u_price': self.RH_DS16_u_price ,
            'RH_RS16': self.RH_RS16 ,
            'RH_RS16_u_price': self.RH_RS16_u_price ,
            'OTHER16': self.OTHER16 ,
            'OTHER16_u_price': self.OTHER16_u_price ,
            'price': self.price
        }

class Market(object):
    DH_DS16 = 0
    DH_DS16_u_price = 0
    DH_RS16 = 0
    DH_RS16_u_price = 0
    RH_DS16 = 0
    RH_DS16_u_price = 0
    RH_RS16 = 0
    RH_RS16_u_price = 0
    OTHER16 =0
    OTHER16_u_price =0

    @staticmethod
    def get_json():
        info = {}
        info['DH_DS16'] = {'count' : Market.DH_DS16 , 'price': Market.DH_DS16_u_price}
        info['DH_RS16'] = {'count' : Market.DH_RS16 , 'price': Market.DH_RS16_u_price}
        info['RH_DS16'] = {'count' : Market.RH_DS16 , 'price': Market.RH_DS16_u_price}
        info['RH_RS16'] = {'count' : Market.RH_RS16 , 'price': Market.RH_RS16_u_price}
        info['OTHER16'] = {'count' : Market.OTHER16 , 'price': Market.OTHER16_u_price}
        return info
