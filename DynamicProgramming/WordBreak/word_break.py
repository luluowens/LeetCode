from functools import lru_cache


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        @lru_cache(None)
        def dp(i):
            if i < 0: 
                return True
            for word in wordDict:
                if (i >= len(word) - 1) and dp(i - len(word)):
                    if s[i - len(word) + 1 : i + 1] == word:
                        return True
            
            return False
        
        return dp(len(s) - 1)