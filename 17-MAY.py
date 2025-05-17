class Solution:
	def sortArray(self, arr, A, B, C):
		# Code here
		arr = [self.fun(A,B,C,x) for x in arr]
		return sorted(arr)
		
	def fun(self,a,b,c,n):
		eq = (a*(n**2)) + (b*n) + c
		return eq
