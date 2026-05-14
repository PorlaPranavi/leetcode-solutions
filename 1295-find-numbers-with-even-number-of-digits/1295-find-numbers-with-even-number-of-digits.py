class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            res=int(math.log10(i))+1
            if res%2==0:
                count=count+1
        return count

        