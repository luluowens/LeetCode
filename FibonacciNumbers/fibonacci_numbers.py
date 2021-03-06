class Solution:
    def fib(self, N: int) -> int:
        cache = {}
        
        def recur_fib(N: int) -> int:
            if N in cache:
                return cache[N]

            if N < 2:
                result = N
            else:
                result = recur_fib(N-1) + recur_fib(N-2)

            cache[N] = result
            return result

        return recur_fib(N)