class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a=[]
        for i in range(len(nums)//2):
            a.append(nums[i])
            a.append(nums[i+n])
        return a
        