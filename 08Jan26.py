class Solution:
    def countSubarrays(self, arr, k):
        from collections import defaultdict
        
        freq = defaultdict(int)
        freq[0] = 1  # base case
        
        odd_count = 0
        result = 0
        
        for num in arr:
            if num % 2 == 1:
                odd_count += 1
            
            if (odd_count - k) in freq:
                result += freq[odd_count - k]
            
            freq[odd_count] += 1
        
        return result
        # Code here
        
