class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        e = str(n)
        w = str(x)
        return e[0] != w and w in e
        