class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avg=sum(nums[:k])
        m=avg
        for i in range(k,len(nums)):
            avg=avg+nums[i]-nums[i-k]
            m=max(m,avg)
        return m/k

        