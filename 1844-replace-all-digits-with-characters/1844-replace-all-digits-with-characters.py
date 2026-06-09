class Solution:
    def replaceDigits(self, s: str) -> str:
        l=""
        for i in range(len(s)):
            if i%2==0:
                l+=s[i]
            else:
                l+=chr(ord(s[i-1])+int(s[i]))
        return l
