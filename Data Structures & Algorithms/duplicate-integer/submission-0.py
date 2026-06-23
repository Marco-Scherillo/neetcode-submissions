class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in mp:
                return True
            mp[nums[i]] = i
        return False
         