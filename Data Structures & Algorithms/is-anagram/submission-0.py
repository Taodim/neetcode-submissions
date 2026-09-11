class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashMapTracker1 = {}
        for c in s:
            if c in hashMapTracker1:
                hashMapTracker1[c] += 1
            else:
                hashMapTracker1[c] = 1
        
        hashMapTracker2 = {}
        for c2 in t:
            if c2 in hashMapTracker2:
                hashMapTracker2[c2] += 1
            else:
                hashMapTracker2[c2] = 1

        return hashMapTracker1 == hashMapTracker2