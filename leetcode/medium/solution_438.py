"""
找到字符串中所有字母异位词
给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
示例 1:
输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
示例 2:
输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
提示:
1 <= s.length, p.length <= 3 * 104
s 和 p 仅包含小写字母
"""
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt_s = [0] * 26
        cnt_p = [0] * 26
        ans = []
        l = len(p)
        for c in p:
            cnt_p[ord(c) - ord('a')] += 1
        left = 0
        for right, c in enumerate(s):
            idx = ord(c) - ord('a')
            cnt_s[idx] += 1
            if not cnt_p[idx]:
                cnt_s = [0] * 26
                left = right + 1
                continue
            while cnt_s[idx] > cnt_p[idx]:
                i = ord(s[left]) - ord('a')
                cnt_s[i] -= 1
                left += 1
            if right - left + 1 == l:
                ans.append(left)
        return ans


"""
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        n, m = len(s), len(p)
        res = []
        if n < m:
            return res
        p_cnt = [0] * 26
        s_cnt = [0] * 26
        for i in range(m):
            p_cnt[ord(p[i]) - ord('a')] += 1
            s_cnt[ord(s[i]) - ord('a')] += 1
        if s_cnt == p_cnt:
            res.append(0)
        for i in range(m, n):
            s_cnt[ord(s[i - m]) - ord('a')] -= 1
            s_cnt[ord(s[i]) - ord('a')] += 1

            if s_cnt == p_cnt:
                res.append(i - m + 1)
        return res
"""
