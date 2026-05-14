class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        else:
             a=1
             b=1
             c=1
        for i in range(n-2):
            c=a+b
            a,b=b,c
        return c
        