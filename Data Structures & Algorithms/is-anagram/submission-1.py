class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sd = {}
        for c in s:
            if c in sd:
                sd[c] += 1
            else:
                sd[c] = 1
        td = {}
        for c in t:
            if c in td:
                td[c] += 1
            else:
                td[c] = 1
        for k in td.keys():
            if k not in sd.keys():
                return False
            if sd[k] != td[k]:
                return False
        return True
         