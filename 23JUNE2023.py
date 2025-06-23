class Solution:
    def minSum(self, arr):
        def add_numbers(num1,num2):
            carry=0
            sum1=""
            i , j = len(num1)-1 , len(num2)-1
            
            while i>=0 or j>=0 or carry:
                digit1=int(num1[i]) if i>=0 else 0
                digit2=int(num2[j]) if j>=0 else 0
                total = digit1 + digit2 + carry
                carry = total//10
                sum1+=str(total%10)
                i-=1
                j-=1
            return((sum1[::-1]).lstrip("0"))
    
        arr = sorted(arr)
        num1=""
        num2=""
        if len(arr) == 1:
            return arr[0]
        for i in range(len(arr)):
            if i%2 == 0:
                num1+=str(arr[i])
            else:
                num2+=str(arr[i])
        # print(num1)
        # print(num2)
        return(add_numbers(num1,num2))
        # code here
