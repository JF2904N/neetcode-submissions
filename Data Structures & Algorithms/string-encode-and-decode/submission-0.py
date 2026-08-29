class Solution:

    def encode(self, strs: List[str]) -> str:
        word = ""
        for ch in strs:
            word += str(len(ch)) + "#" + ch
        return word
    def decode(self, s: str) -> List[str]:
        word, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j +=1 
            length = int(s[i:j]) 
            word.append(s[j+1: j+1+length])
            i = j + 1 + length
        return word