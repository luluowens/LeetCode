class Solution:
    def mySqrt(self, x: int) -> int:
        sq_root = 1
        while sq_root ** 2 < x :
            sq_root += 1
        if sq_root ** 2 > x :
            return sq_root - 1
        else :
            return sq_root