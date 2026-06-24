class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        seen = {}

        for i in range(len(strs)):
            sorted_word = "".join(sorted(strs[i])) 
            if sorted_word not in seen:
                seen[sorted_word] = [strs[i]]
            else:
                seen[sorted_word].append(strs[i])
        
        for key, val in seen.items():
            anagram = []
            for word in val:
                anagram.append(word)
            answer.append(anagram)
        
        return answer
