class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        dictionary = {}

        for char in s:
            if char in dictionary:
                dictionary[char] += 1
            else:
                dictionary[char] = 1
        for char in t:
            if char not in dictionary:
                return False
            dictionary[char] -= 1
            if dictionary[char] < 0:
                return False
        return True 