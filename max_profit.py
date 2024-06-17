'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

https://takeuforward.org/data-structure/stock-buy-and-sell/

'''

def max_profit(prices):
        min_price = prices[0]
        max_profit = 0
        leng = len(prices)

        for i in range(1,leng):
            # min_price = min(prices[i], min_price)
            # max_profit = max(max_profit, prices[i]-min_price)
            
            if prices[i] < min_price:
                min_price = prices[i]

            if max_profit < prices[i]-min_price:
                max_profit = prices[i]-min_price   
                 
        return max_profit






prices = [7,1,5,3,6,4]

prices = [7,6,4,3,1]


print(max_profit(prices))