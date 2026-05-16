class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:
            chars = ''.join(sorted(word))
            if chars in d:
                d[chars].append(word)
            else:
                d[chars] = [word]
        return list(d.values())