from solution import Solution


lst = []
lst = [int(item) for item in input("Enter the stock prices: ").split()]
prices = Solution()
prices.maxProfit(lst)