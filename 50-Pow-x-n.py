class Solution:
    def myPow(self, x: float, n: int) -> float:
        y = x
        i = 1
        if n == 0:
            return 1
        if x == 0:
            return 0
        check = n / x
        if x == 1:
            return 1
        if x == -1:
            if n % 2 == 0:
                return 1
            else:
                return -1
        if n > 100000000:
            while i < check:
                y *= y
                i *= 2
            for j in range(int(i), n):
                y *= x
        elif n > 0:
            for j in range(n - 1):
                y *= x
        elif n < -100000000:
            while i < (check * -1):
                y *= y
                i *= 2
            for j in range(int(i) * -1, n):
                y *= x
            return 1/y
        elif n < 0:
            for i in range(n * (- 1) - 1):
                y *= x
            return(1/y)           
        return y