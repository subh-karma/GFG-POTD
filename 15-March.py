class Solution:
    def minCoins(self, coins, target):
        # Initialize DP array with a large value
        dp = [float('inf')] * (target + 1)
        dp[0] = 0  # Base case: 0 coins needed for sum = 0
        
        # Process each coin denomination
        for coin in coins:
            for i in range(coin, target + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[target] if dp[target] != float('inf') else -1
