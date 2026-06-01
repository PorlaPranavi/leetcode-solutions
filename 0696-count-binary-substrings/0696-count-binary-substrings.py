class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n=0
        prev=0
        curr=1
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                curr+=1
            else:
                n+=min(prev,curr)
                prev=curr
                curr=1
        return n+min(prev,curr)
        