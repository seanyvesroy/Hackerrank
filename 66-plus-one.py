class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        if len(digits) == 1 and digits[0] == 9:
            return [1,0]
        digits[len(digits) - 1] += 1
        for i in range(len(digits) - 1, 0, -1):
            if digits[i] > 9:
                digits[i - 1] += 1
                digits[i] = 0
        temp = [1]
        if digits[0] > 9:
            digits[0] = 0
            digits = temp + digits

        return digits