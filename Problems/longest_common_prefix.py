class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        sub = ""
        count = 0
        if len(strs) == 1 :
            return strs[0]
        for i in range(len(strs[0])+1) :
            substring = strs[0][0:i]
            for string in strs :
                if string[0:i] == substring :
                    count += 1
            if count == len(strs) :
                sub = substring
            count = 0
        return sub