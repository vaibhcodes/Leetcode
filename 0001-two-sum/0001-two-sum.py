class Solution:
    def twoSum(self, nums:List[int], target: int) -> List[int]:
        nums = [(nums,idx) for idx,nums in enumerate(nums)]
        nums.sort()
        left , right = 0, len(nums)-1
        while left < right:
            s = nums[left][0] + nums[right][0]
            if s == target:
                return [nums[left][1], nums[right][1]]
            elif s< target:
                left +=1
            else:
                right -=1
