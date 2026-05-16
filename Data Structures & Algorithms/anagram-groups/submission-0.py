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
        # go through every word in strs
        # find out if its in an existing anagram dict
        #   do that by checking the sorted one and frequency of it
        # if so add that word into the associated list
        # else make a new one
        # return the list of those lists