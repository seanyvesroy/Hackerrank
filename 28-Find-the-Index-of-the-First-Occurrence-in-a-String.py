class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        count = 0
        index = -1
        finalIndex = -1
        i = 0
        j = 0
        while i < len(haystack):
            while j < len(needle):
                if haystack[i] != needle[j]:
                    count = 0
                    j = 0
                    i += 1
                    break
                else:
                    if count == 0:
                        index = i
                    count = count + 1
                    if count == len(needle) and finalIndex != -1:
                        finalIndex = index
                        return finalIndex
                    j += 1
                    i += 1

        return -1

                