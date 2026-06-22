class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        new_sorting = sorted(count, key=lambda x:count[x], reverse= True)
        return new_sorting[:k]
        