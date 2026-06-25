class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string)) + '#' + string
        return encoded
    
    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            lenght = int(s[i:j])
            j += 1 
            decoded.append(s[j: j + lenght])
            i = j + lenght
        return decoded
            
            
