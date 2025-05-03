class Solution:
    def primeList(self, head):
        def is_prime(n):
            if n < 2: return False
            if n == 2: return True
            if n % 2 == 0: return False
            i = 3
            while i * i <= n:
                if n % i == 0:
                    return False
                i += 2
            return True
        
        def nearest_prime(n):
            if is_prime(n):
                return n
            lower = n - 1
            upper = n + 1
            while True:
                if lower >= 2 and is_prime(lower):
                    if is_prime(upper) and upper - n == n - lower:
                        return lower
                    return lower
                if is_prime(upper):
                    return upper
                lower -= 1
                upper += 1
                
        curr = head
        while curr:
            curr.val = nearest_prime(curr.val)
            curr = curr.next
        return head
