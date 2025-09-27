class Solution:
    def kBitFlips(self, arr, k):
        # code here
        flip_state = [0] * len(arr)
        curr_state = 0
        cnt = 0
        for i, v in enumerate(arr):
            curr_state = curr_state ^ flip_state[i]
            if curr_state ^ v == 0:
                if i + k - 1 >= len(arr):
                    return -1
                    
                if i + k < len(arr):
                    flip_state[i+k] ^= 1
                    
                curr_state ^= 1
                cnt += 1
                
        return cnt
        # code here
        
