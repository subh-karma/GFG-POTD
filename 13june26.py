class Solution:
    def computeValue(self, n):
    
    # For calculate power efficiently
        def power(a,b,mod):
            res = 1
            while b:
                if b&1:
                    res = res*a%mod
                a=a*a%mod
                b>>=1
            return res
            
    # Fermat's Little Theorem
        def modInverse(a,mod):
            return power(a,mod-2,mod)
        
        mod = int(1e9)+7
    
    # Precomputing factorial
        fact = [1]*(2*n + 1)
        
        for i in range(1,2*n+1):
            fact[i] = fact[i-1]*i%mod
            
    # Modulo inverse - easy to understand
        inv = [1]*(2*n + 1)
        inv[2*n] = modInverse(fact[2*n],mod) 
        
        for i in range(2*n-1,-1,-1):
            inv[i] = inv[i+1]*(i+1)%mod
            
    # Simply calculate nCr
        res = fact[2*n]*inv[n]%mod*inv[2*n-n]%mod
        return res
        # code here
        
