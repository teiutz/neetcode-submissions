class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for st in strs:
            encoded_string += str(len(st)) + "#" + st

        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_list = []

        i = 0

        while i < len(s):
            number = ""
            while s[i] != "#":
                number += s[i]
                i += 1

            word = ""
            for j in range(i + 1, (i + 1) + int(number)):
                word += s[j]

            decoded_list.append(word)
            i += int(number) + 1

        return decoded_list
