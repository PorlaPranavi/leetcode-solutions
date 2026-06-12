class Solution:
    def sortSentence(self, s: str) -> str:
        word=s.split()
        r=s.split()
        k=[]
        a=[None]*len(r)
        for x in r:
            a[int(x[-1])-1]=x[:-1]
        return " ".join(a)
        
        