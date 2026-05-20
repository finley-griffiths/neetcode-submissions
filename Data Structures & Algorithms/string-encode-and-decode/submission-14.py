class Solution:
    def encode(self, strs: List[str]) -> str:
        return ''.join([f'{len(string)}#{string}' for string in strs])
    def decode(self, s: str) -> List[str]:
        r = []
        start = 0
        i = 0
        while i != len(s):
            if s[i] == '#':
                length = int(s[start:i])
                this_string = s[i+1:i+length+1]
                r.append(this_string)
                start = length+1+i
                i = start
            else:
                i += 1
        return r
