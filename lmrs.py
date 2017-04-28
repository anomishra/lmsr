from flask import jsonify
from model.models import Investor, Market, Order
import json
import random
import math

class LMRS:
    b_number = 500
    investor_count = 10
    investors = {}
    orders = []
    day = 1
    MAX_BUY = 20
    MAX_ORDER_SHOW = 30
    history_data = {}

    @staticmethod
    def init(investor_count, b_number, budget=500):
        print("Init ...... .")
        LMRS.day = 1
        LMRS.investor_count = investor_count
        LMRS.b_number = b_number
        LMRS.orders = []

        investors = {}
        for i in range(1, LMRS.investor_count + 1):
            investor = Investor(id = i, budget = budget)
            LMRS.investors[i] = investor
        LMRS.update_market(0, 0, 0, 0, 0)
        LMRS.history_data = {'1':{'DH_DS16': 0, 'DH_RS16': 0, 'RH_DS16': 0, 'RH_RS16':0, 'OTHER16':0}}

        Market.DH_DS16 = 0
        Market.DH_RS16 = 0
        Market.RH_DS16 = 0
        Market.RH_RS16 = 0
        Market.OTHER16 = 0

        return jsonify({'state':True})

    @staticmethod
    def gen_random_orders(day):
        new_orders = []
        for i in range(1, LMRS.investor_count + 1):
            investor = LMRS.investors[i]
            order = Order(day = day, investor_id = i)

            order.DH_DS16 = random.randint(int(-1 * investor.DH_DS16/2), random.randint(0, LMRS.MAX_BUY))
            order.DH_RS16 = random.randint(int(-1 * investor.DH_RS16/2), random.randint(0, LMRS.MAX_BUY))
            order.RH_DS16 = random.randint(int(-1 * investor.RH_DS16/2), random.randint(0, LMRS.MAX_BUY))
            order.RH_RS16 = random.randint(int(-1 * investor.RH_RS16/2), random.randint(0, LMRS.MAX_BUY))
            order.OTHER16 = random.randint(int(-1 * investor.OTHER16/2), random.randint(0, LMRS.MAX_BUY))
            new_orders.append(order)
        random.shuffle(new_orders)
        return new_orders

    @staticmethod
    def calc_c(DH_DS16, DH_RS16, RH_DS16, RH_RS16, OTHER16):
        val =  LMRS.b_number * math.log(math.exp((Market.DH_DS16 + DH_DS16)/LMRS.b_number) + \
                                        math.exp((Market.DH_RS16 + DH_RS16)/LMRS.b_number) + \
                                        math.exp((Market.RH_DS16 + RH_DS16)/LMRS.b_number) + \
                                        math.exp((Market.RH_RS16 + RH_RS16)/LMRS.b_number) + \
                                        math.exp((Market.OTHER16 + OTHER16)/LMRS.b_number)) - \
               LMRS.b_number * math.log(math.exp((Market.DH_DS16 )/LMRS.b_number) + \
                                        math.exp((Market.DH_RS16 )/LMRS.b_number) + \
                                        math.exp((Market.RH_DS16 )/LMRS.b_number) + \
                                        math.exp((Market.RH_RS16 )/LMRS.b_number) + \
                                        math.exp((Market.OTHER16 )/LMRS.b_number))
        return round (val, 4)


    @staticmethod
    def update_market(DH_DS16, DH_RS16, RH_DS16, RH_RS16, OTHER16):
        Market.DH_DS16 += DH_DS16
        Market.DH_RS16 += DH_RS16
        Market.RH_DS16 += RH_DS16
        Market.RH_RS16 += RH_RS16
        Market.OTHER16 += OTHER16

        Market.DH_DS16_u_price = LMRS.calc_c(1, 0, 0, 0, 0)
        Market.DH_RS16_u_price = LMRS.calc_c(0, 1, 0, 0, 0)
        Market.RH_DS16_u_price = LMRS.calc_c(0, 0, 1, 0, 0)
        Market.RH_RS16_u_price = LMRS.calc_c(0, 0, 0, 1, 0)
        Market.OTHER16_u_price = LMRS.calc_c(0, 0, 0, 0, 1)

        LMRS.history_data[LMRS.day] = {'DH_DS16': Market.DH_DS16,
                                       'DH_RS16': Market.DH_RS16,
                                       'RH_DS16': Market.RH_DS16,
                                       'RH_RS16': Market.RH_RS16,
                                       'OTHER16': Market.OTHER16}




    @staticmethod
    def process_order(order):
        order.DH_DS16_u_price = Market.DH_DS16_u_price
        order.DH_RS16_u_price = Market.DH_RS16_u_price
        order.RH_DS16_u_price = Market.RH_DS16_u_price
        order.RH_RS16_u_price = Market.RH_RS16_u_price
        order.OTHER16_u_price = Market.OTHER16_u_price

        order.price = LMRS.calc_c(order.DH_DS16, order.DH_RS16, order.RH_DS16, order.RH_RS16, order.OTHER16)
        LMRS.update_market(order.DH_DS16, order.DH_RS16, order.RH_DS16, order.RH_RS16, order.OTHER16)

        LMRS.investors[order.investor_id].DH_DS16 += order.DH_DS16
        LMRS.investors[order.investor_id].DH_RS16 += order.DH_RS16
        LMRS.investors[order.investor_id].RH_DS16 += order.RH_DS16
        LMRS.investors[order.investor_id].RH_RS16 += order.RH_RS16
        LMRS.investors[order.investor_id].OTHER16 += order.OTHER16
        LMRS.investors[order.investor_id].budget -= order.price

    @staticmethod
    def calc_for_new_day():
        if len(LMRS.investors) == 0:
            LMRS.init(LMRS.investor_count, LMRS.b_number)

        LMRS.day += 1

        new_orders = LMRS.gen_random_orders(LMRS.day)

        for order in new_orders:
            LMRS.process_order(order)
            LMRS.orders.append(order)

    @staticmethod
    def attach_history():
        info = {}
        info['DH_DS16'] = []
        info['DH_RS16'] = []
        info['RH_DS16'] = []
        info['RH_RS16'] = []
        info['OTHER16'] = []
        info['labels'] = []

        for key in LMRS.history_data:
            info['labels'].append(int(key))
            info['DH_DS16'].append(LMRS.history_data[key]['DH_DS16'])
            info['DH_RS16'].append(LMRS.history_data[key]['DH_RS16'])
            info['RH_DS16'].append(LMRS.history_data[key]['RH_DS16'])
            info['RH_RS16'].append(LMRS.history_data[key]['RH_RS16'])
            info['OTHER16'].append(LMRS.history_data[key]['OTHER16'])

        return info

    @staticmethod
    def gen_market_info():
        info = {}
        if len(LMRS.investors) == 0:
            LMRS.init(LMRS.investor_count, LMRS.b_number)

        info['market'] = Market.get_json()
        info['investors'] = {}
        for i in range(1, LMRS.investor_count + 1):
            info['investors'][i] = LMRS.investors[i].get_json()

        info['orders'] = {}
        for i in range (max(0, len(LMRS.orders) - LMRS.MAX_ORDER_SHOW), len(LMRS.orders)):
            order = LMRS.orders[i]
            info['orders'][i +1] = order.get_json()

        info['history'] = LMRS.attach_history()
        return info

    @staticmethod
    def run_for_next_day ():
        LMRS.calc_for_new_day()
        return LMRS.gen_market_info()
