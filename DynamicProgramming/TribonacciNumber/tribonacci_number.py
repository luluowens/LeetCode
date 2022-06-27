class Solution:
    def tribonacci(self, n: int) -> int:
        cache = {}
        def recur_trib(n: int) -> int:
            if n in cache:
                return cache[n]

            if n < 2:
                result = n
            elif n == 2:
                result = 1
            else:
                result = recur_trib(n-1) + recur_trib(n-2) + recur_trib(n-3)

            cache[n] = result
            return result

        return recur_trib(n)