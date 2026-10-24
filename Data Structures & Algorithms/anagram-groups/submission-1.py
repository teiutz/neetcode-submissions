class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for i in range(len(strs)):
            word_set = "".join(sorted(strs[i]))
            listy = d.get(word_set, [])
            listy.append(strs[i])
            d[word_set] = listy
            
        return list(d.values())

        print(d)
        return answer
