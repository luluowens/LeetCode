class Solution:
    def myPow(self, x: float, n: int) -> float:
        cache = {}
        def recur_pow(N):
            if N in cache:
                return cache[N]

            if N < 0:
                result = recur_pow(N + 1) / x
            elif N == 0 :
                result = 1
            else:
                result = x * recur_pow(N - 1)

            # put result in cache for later reference.
            cache[N] = result
            return result

        return recur_pow(n)