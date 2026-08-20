class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = []
        for i in range(len(nums) - 1):
            changedNums = nums.copy()
            second = target - nums[i]
            changedNums.pop(i)
            if second in changedNums:
                pair = [i, changedNums.index(second)+1]
                break
            #changedNums = nums.copy()
        return pair
            