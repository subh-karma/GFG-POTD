class Solution:
    def maxProfit(self, arr):
        bought, prev_sold, just_sold = -arr[0], 0, 0
        for i in range(1, len(arr)):
            price = arr[i]
            new_bought = max(bought, prev_sold - price)
            prev_sold = max(prev_sold, just_sold)
            just_sold = bought + price
            bought = new_bought
        return max(prev_sold, just_sold)
        # code here
        
