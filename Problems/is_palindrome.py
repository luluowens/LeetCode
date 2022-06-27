class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        else :
            new_string = int(str(x)[::-1])
            return x == new_string