class Solution:
    def numWays(self, n: int, k: int) -> int:
        cache = {}

        def paint(left, k) :
            if left in cache :
                return cache[left]

            if left == 0 :
                ways = 1
            elif left == 1 :
                ways = k
            else :
                ways = paint(left - 2, k) * (k-1) + paint(left - 1, k) * (k-1)
            
            cache[left] = ways
            return ways

        return k * paint(n-1, k)
