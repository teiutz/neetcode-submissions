class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = dict()
        d2 = dict()

        for letter in s:
            if letter in d1.keys():
                value = d1.get(letter) + 1
                d1.update({letter : value})
            else:
                d1.update({letter: 1})

        for letter in t:
            if letter in d2.keys():
                value = d2.get(letter) + 1
                d2.update({letter : value})
            else:
                d2.update({letter: 1})

        return d1 == d2
        


