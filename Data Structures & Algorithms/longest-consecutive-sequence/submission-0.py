class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = set(nums)
        mike = 0

        for i in nums:
            if (i-1) not in check:
                long = 1
                while (i+long) in check:
                    long += 1
                mike = max(mike, long)
            return mike 