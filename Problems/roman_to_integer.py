class Solution:
    def romanToInt(self, s: str) -> int:
        convert = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        number = 0
        i = 0
        if len(s) == 1 :
            return convert[s]
        while i < len(s) - 1 :
            if s[i] == "I" and (s[i+1] == "V" or s[i+1] == "X") :
                number += convert[s[i+1]] - 1
                i += 2
            elif s[i] == "X" and (s[i+1] == "L" or s[i+1] == "C") :
                number += convert[s[i+1]] - 10
                i += 2
            elif s[i] == "C" and (s[i+1] == "D" or s[i+1] == "M") :
                number += convert[s[i+1]] - 100
                i += 2
            else :
                number += convert[s[i]]
                i += 1
        if i == len(s) :
            return number
        else :
            return number + convert[s[-1]]