from typing import List
class Solution:


    def maxProfit(self, prices: List[int]) -> int:
        self.prices = prices
        if self.check_constraints(self.prices) == 0:
            exit()

        self.buyAmount = self.buy_amount(self.prices)
        self.buyDay = self.buy_day(self.prices)
        self.sellDay = self.sell_day(self.prices)
        self.sellAmount = self.sell_amount(self.prices)
        self.profit = self.sellAmount - self.buyAmount

        print("Buy on day", self.buyDay+1, "(price =", self.buyAmount, ") and sell on day", self.sellDay+1, "(price =", self.sellAmount, "), profit =", self.sellAmount, "-", self.buyAmount, " = ", self.profit)


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
        tempLst = self.prices
        j = 0
        k = 0
        i = self.buy_day(self.prices)
        buyDay = self.buy_day(self.prices)

        while i < len(self.prices):
            tempLst[j] = self.prices[i]
            i+=1
            j+=1

        if buyDay== max(self.prices):
            print("In this case, no transactions are done and the max profit = 0.")
            exit()

        while k < len(self.prices):
            if max(tempLst) == tempLst[k]:
                return k + (buyDay)
            k+=1

    def buy_amount(self, prices: List[int]) -> int:
        self.prices = prices
        self.minValue = min(self.prices)
        return self.minValue

    def sell_amount(self, prices: List[int]) -> int:
        self.prices = prices
        tempLst = self.prices
        j = 0
        i = self.buy_day(self.prices)
        while i < len(self.prices):
            tempLst[j] = self.prices[i]
            i+=1
            j+=1
        return max(tempLst)

    def check_constraints(self, prices: List[int]) -> int:
        self.prices = prices
        i = 0
        if len(self.prices) <= 1:
            print("Please enter multiple stock entries")
            return 0
        if len(self.prices) >= 1000000:
            print("Please enter under one million entries")
            return 0
        while i < len(self.prices):
            if self.prices[i] <= 0:
                print("Please enter a stock that holds value")
                return 0
            if self.prices[i] >= 100000:
                print("Please enter a realistic stock value")
                return 0
            i+=1
        return 1
