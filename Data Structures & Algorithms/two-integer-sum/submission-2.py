class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        k = 0
        j = len(nums) -1 
        while k < j:
            sum = nums[k] + nums[j]
            if target == sum:
                check = [k,j]
                set = [k,j]
                return set
            elif target > sum:
                k += 1
            else:
                j -= 1
        return []