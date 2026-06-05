class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}

        for index, i in enumerate(nums):
            sum = target - i
            if sum in count:
                return [count[sum], index]
            count[i] = index