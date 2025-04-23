#User function Template for python3
class Solution:
    def singleNum(self, arr):
        xor = 0
        for num in arr:
            xor ^= num
        diff_bit = xor & -xor

        num1 = 0
        num2 = 0
        for num in arr:
            if num & diff_bit:
                num1 ^= num
            else:
                num2 ^= num

        return sorted([num1, num2])
