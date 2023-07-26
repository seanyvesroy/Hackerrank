class Solution:
    def binToNum(self, s: str) -> int:
        count = 0
        total = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "1":
                total = total + (2 ** count)
                count += 1
            else:
                count += 1
        return total
    
    
    
    
    def addBinary(self, a: str, b: str) -> str:
        aNum = self.binToNum(a)
        bNum = self.binToNum(b)
        
        print(aNum)

        sumNum = aNum + bNum

        binNum = bin(sumNum)

        result = str(binNum)
        return result[2:]


    