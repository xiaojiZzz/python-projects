"""
字母异位词分组
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
字母异位词 是由重新排列源单词的所有字母得到的一个新单词。
示例 1:
输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
示例 2:
输入: strs = [""]
输出: [[""]]
示例 3:
输入: strs = ["a"]
输出: [["a"]]
提示：
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] 仅包含小写字母
"""
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        idx = {}
        for s in strs:
            sting = str(sorted(s))
            if sting in idx.keys():
                l = idx[sting]
                l.append(s)
            else:
                l = [s]
                idx[sting] = l
        return [v for v in idx.values()]
        # return list(idx.values())


"""
class Solution:
    # 使用 defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            # 把 s 排序，作为哈希表的 key
            sorted_s = ''.join(sorted(s))
            d[sorted_s].append(s)
        return list(d.values())
"""

"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            counts = [0] * 26
            for char in s:
                counts[ord(char) - ord('a')] += 1
            key = tuple(counts)
            groups[key].append(s)
        
        return list(groups.values())
"""
