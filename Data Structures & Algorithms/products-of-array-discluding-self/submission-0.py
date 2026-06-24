class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sums = []
        for i in range(len(nums)):
            product = 1 

            for k in range(len(nums)):
                if i == k:
                    pass
                else:
                    product *= nums[k]
            sums.append(product)
        return sums
             