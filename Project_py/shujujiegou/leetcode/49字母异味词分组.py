"""
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
示例:
输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]]
"""
import collections


class Solution:
    def groupAnagrams(self, strlist):
        """
        当两个字符串的排序字符串相等时 两个字符串是字母异分词
        时间复杂度 O(Nklogk) N是strlist长度 k是strlist中字符串的最大长度
        在O(klogk）的时间内对每个字符串排序
        空间复杂度O(nk)
        :param strlist:
        :return:
        """
        ans = collections.defaultdict(list)

        for s in strlist:
            ans[tuple(sorted(s))].append(s)

        return ans.values()


if __name__ == "__main__":
    str1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    s = Solution()

    print(s.groupAnagrams(str1))

