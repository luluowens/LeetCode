class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.

        :param list s: list of strings
        """
        def reverse_string_with_index(chars, start: int, end: int) -> None:
            if end - start >= 1 :
                temp = chars[end]
                chars[end] = chars[start]
                chars[start] = temp
                start += 1
                end -= 1
                chars = reverse_string_with_index(chars, start, end)

        s = reverse_string_with_index(s, 0, len(s)-1)
