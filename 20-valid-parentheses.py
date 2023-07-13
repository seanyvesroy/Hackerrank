class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        comparison = {')' : '(', ']' : '[', '}' : '{'}
        start = {'{', '[', '('}
        stack = []

        if s[0] not in start:
            return False

        for letter in s:
            if letter in start:
                stack.append(letter)
            else:
                if len(stack) == 0:
                    return False
                temp = stack.pop()    
                if comparison[letter] != temp:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False