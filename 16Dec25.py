class Solution:
    def areRotations(self, s1, s2):
        combined = s1 + s1
        return combined.find(s2)!=-1
        
