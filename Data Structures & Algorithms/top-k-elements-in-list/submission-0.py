from collections import Counter
import sys


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_nums = Counter(nums)

        l = []

        for key, value in counter_nums.items():
            l.append((key, value))

        res = sorted(l, key=lambda x: x[1], reverse=True)

        res2 = [li[0] for li in res[:k]]

        return res2






    