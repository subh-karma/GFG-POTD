class Solution:
	def mergeOverlap(self, arr):
		# Code here
		arr.sort(key=lambda x: x[0])
		l = arr[0][0]
		r = arr[0][1]
		result = []
		for pair in arr[1:]:
		    if pair[0] > r:
		        result.append([l,r])
		        l = pair[0]
		        r = pair[1]
		    else:
		        r = max(r, pair[1])
		
		result.append([l,r])        
		return result
		# Code here
