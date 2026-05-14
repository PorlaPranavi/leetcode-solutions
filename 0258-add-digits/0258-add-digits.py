class Solution:
    def addDigits(self, num: int) -> int:
        s=0
        while True:
            while num>0:
                d=num%10
                s=s+d
                num=num//10
            if s<10:
                return s
            else:
                num=s
                s=0


        
