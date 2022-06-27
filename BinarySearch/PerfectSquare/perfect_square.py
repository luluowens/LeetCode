class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        half = num // 2
        left = 0
        right = half
        while left <= right :
            mid = int((left + right) / 2)
            if mid * mid == num :
                return True
            elif mid * mid < num :
                left = mid + 1
            else :
                right = mid - 1
        return False



    # def half_pow(self, x, n) :
    #     if n == 0 :
    #         return 1.0
    #     half = self.half_pow(x, n // 2)
    #     if n % 2 == 0 :
    #         return half * half
    #     else :
    #         return half * half * x


    # def myPow(self, x: float, n: int) -> float:
    #     if n < 0 :
    #         x = 1 / x
    #         n = -n
    #     return self.half_pow(x, n)