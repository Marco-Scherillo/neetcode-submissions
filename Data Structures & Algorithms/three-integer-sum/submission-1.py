class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        answer = []
        for i in range(n):
            j = i + 1
            k = len(nums) - 1
            target = -nums[i]
            while j < k:
                guess = nums[j] + nums[k]
                if guess == target:
                    if [nums[i], nums[j], nums[k]] not in answer:
                        answer.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif guess < target:
                    j += 1
                elif guess > target:
                    k -= 1
        return answer

