class Solution:
    def findPermutation(self, s):
        def backtrack(start):
            if start == len(s) - 1:
                result.add("".join(s))
                return
            
            for i in range(start, len(s)):
                if i != start and s[i] == s[start]:
                    continue  # Skip duplicates
                s[start], s[i] = s[i], s[start]  # Swap
                backtrack(start + 1)  # Recurse
                s[start], s[i] = s[i], s[start]  # Backtrack (swap back)
        
        s = list(s)  # Convert string to list for easier manipulation
        s.sort()  # Sort to handle duplicates
        result = set()  # Use a set to store unique permutations
        backtrack(0)
        return list(result)
