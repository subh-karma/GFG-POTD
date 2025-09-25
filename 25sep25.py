class Solution:
    def generateBinary(self, n: int) -> list[str]:
        result = []
        for i in range(1, n + 1):
            result.append(bin(i)[2:])  # Convert number to binary (remove '0b')
        return result
 


        # code here
        
