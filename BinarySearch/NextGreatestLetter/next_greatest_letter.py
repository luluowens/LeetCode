class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        targ_val = ord(target)

        if ord(letters[-1]) <= targ_val :
            return letters[0]

        distance = 24
        letter = letters[0]
        left = 0
        right = len(letters) - 1

        while left <= right :
            mid = left + (right - left) // 2
            letter_val = ord(letters[mid])
            if letter_val > targ_val :
                if (letter_val - targ_val) <= distance :
                    distance = letter_val - targ_val
                    letter = letters[mid]
                right = mid - 1
            else :
                left = mid + 1

        return letter