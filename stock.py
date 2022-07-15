'''
    Author: Carlos Andrés Robles Hernández

'''

from typing import List

from consolemenu import *
from consolemenu.items import *

def maxProfit() -> int:
    '''
    input: 7, 1, 5, 3, 6, 4
    output: 5

    '''
    prices = list(map(int, Screen().input('Ingresa array de stocks separados por una coma: ').split(',')))
    min_price = float('inf')
    max_profit = 0
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price

    print(max_profit)
    Screen().input('Press [Enter to continue')


if __name__ == "__main__":

    #sample imputs
    stock_list = [7,1,5,3,6,4]
    stock_list_2 = [7,6,4,3,1]


    menu = ConsoleMenu("Stock problem", "Linear aproach")
    function_item = FunctionItem("Stock Problem Solution", maxProfit)
    menu.append_item(function_item)

    menu.show()
