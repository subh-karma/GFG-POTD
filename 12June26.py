from collections import Counter

class Solution:
    def kSubstr(self, s: str, k: int) -> bool:
        n = len(s)

        if n % k != 0:
            return False

        blocks = [s[i:i + k] for i in range(0, n, k)]
        freq = Counter(blocks)

        if len(freq) == 1:
            return True

        if len(freq) == 2 and 1 in freq.values():
            return True

        return False
