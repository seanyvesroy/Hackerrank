class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        check = False
        
        for i in range(len(s) - 1, -1,-1):
            if s[i].isalpha():
                check = True
            if s[i] == " " and check:
                break
            elif check:
                    count +=1

        return count