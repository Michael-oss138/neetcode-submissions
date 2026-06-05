class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sets = {}
        for char in strs:
            sorting = "".join(sorted(char))
            if sorting not in sets:    
                sets[sorting] = []
            sets[sorting].append(char)
        return list(sets.values())