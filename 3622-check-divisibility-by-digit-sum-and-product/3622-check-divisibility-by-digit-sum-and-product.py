class Solution:
    def checkDivisibility(self, n: int) -> bool:
        x,s,p=n,0,1
        while x:
            d=x%10
            s+=d
            p*=d
            x//=10
        return n% (s+p) ==0