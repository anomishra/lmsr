

class Investor(object):
    def __init__(id, budget=500):
        self.id = id
        self.budget = budget
        self.DH_DS16 = 0
        self.DH_RS16 = 0
        self.RH_DS16 = 0
        self.RH_RS16 = 0
        self.OTHER16 =0



class Order(object):
    def __init__(id, DH_DS16, DH_DS16_u_price, DH_RS16, DH_RS16_u_price, RH_DS16, RH_DS16_u_price, RH_RS16, RH_RS16_u_price, OTHER16, OTHER16_u_price):
        self.id = id
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

    def sum():
        return self.DH_DS16 * self.DH_DS16_u_price + self.DH_RS16 * self.DH_RS16_u_price \
               self.RH_DS16 * self.RH_DS16_u_price + self.RH_RS16 * self.RH_RS16_u_price \
               self.OTHER16 * self.OTHER16_u_price

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
