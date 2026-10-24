from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for i in range(len(strs)):
            word_set = "".join(sorted(strs[i]))
            d[word_set].append(strs[i])
            
        return list(d.values())

        print(d)
        return answer
