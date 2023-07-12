class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        check = {}
        count = 0
        maxCount = 0

        if len(s) < 2:
            return len(s)
        
        while right < len(s):
            if s[right] not in check:
                check[s[right]] = right
                right += 1
                count += 1
                if count > maxCount:
                    maxCount = count
            elif s[right] in check:
                left = check[s[right]] + 1
                right = check[s[right]] + 1
                check = {}
                count = 0
        return maxCount