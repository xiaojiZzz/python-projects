"""
无重复字符的最长子串
给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。
示例 1:
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
提示：
0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        # 也可以使用 cnt = defaultdict(int)
        cnt = [0] * 128
        ans = 0
        for right, char in enumerate(s):
            r = ord(char)
            while cnt[r] > 0:
                l = ord(s[left])
                cnt[l] -= 1
                left += 1
            cnt[r] += 1
            ans = max(ans, right - left + 1)
        return ans


"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = left = 0
        window = set()
        for right, c in enumerate(s):
            while c in window:
                window.remove(s[left])
                left += 1
            window.add(c)
            ans = max(ans, right - left + 1)
        return ans
"""
