from typing import List
class Solution:


    def maxProfit(self, prices: List[int]) -> int:
        self.prices = prices
        print("This is testing: ", self.prices)
        self.buyAmount = self.buy_amount(self.prices)
        self.buyDay = self.buy_day(self.prices)
        self.sellDay = self.sell_day(self.prices)
        self.sellAmount = self.sell_amount(self.prices)
        self.profit = self.sellAmount - self.buyAmount
        print("Buy on day ", self.buyDay + 1, "(price = ", self.buyAmount, ") and sell on day ", self.sellDay + 1, "(price = ", self.sellAmount, "), profit = ", self.sellAmount, "-", self.buyAmount, " = ", self.profit)


    def buy_day(self, prices: List[int]) -> int:
        self.prices = prices
        minValue = self.buy_amount(self.prices)
        i = 0
        while i < len(self.prices):
            if self.prices[i] == minValue:
                return i
            i+=1

    def sell_day(self, prices: List[int]) -> int:
        self.prices = prices
        tempLst = [0, 0, 0, 0, 0]
        j = 0
        k = 0
        maxValue = self.sell_amount(self.prices)
        i = self.buy_day(self.prices)
        buyDay = self.buy_day(self.prices)
        print("i is: ", i)
        while i < len(self.prices):
            tempLst[j] = self.prices[i]
            i+=1
            j+=1
        while k < len(self.prices):
            if max(tempLst) == tempLst[k]:
                return k + buyDay
            k+=1
        print ("tempLST: ", tempLst)

    def buy_amount(self, prices: List[int]) -> int:
        self.prices = prices
        self.minValue = min(self.prices)
        return self.minValue

    def sell_amount(self, prices: List[int]) -> int:
        self.prices = prices
        tempLst = [0, 0, 0, 0, 0]
        j = 0
        i = self.buy_day(self.prices)
        while i < len(self.prices):
            tempLst[j] = self.prices[i]
            i+=1
            j+=1
        return max(tempLst)