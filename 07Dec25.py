class Solution:
	 def distinctSubseq(self, s: str) -> int:
        MODULO = 10**9 + 7
        prev_count = 1
        prev_count_for_char = [0] * 26
        for c in s:
            ci = ord(c) - ord("a")
            curr_count = 2 * prev_count - prev_count_for_char[ci]
            prev_count_for_char[ci] = prev_count
            prev_count = curr_count % MODULO
        return prev_count
		# code here
