class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def climb(n:int) -> int:
            if n in cache:
                return cache[n]

            if n < 4:
                result = n
            else:
                result = climb(n-1) + climb(n-2)

            cache[n] = result
            return result

        return climb(n)