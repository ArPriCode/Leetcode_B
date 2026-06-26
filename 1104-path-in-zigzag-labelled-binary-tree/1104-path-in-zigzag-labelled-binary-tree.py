class Solution(object):
    def pathInZigZagTree(self, label):
        ans = []

        while label >= 1:
            ans.append(label)

            level = label.bit_length() - 1
            start = 1 << level
            end = (1 << (level + 1)) - 1

            label = (start + end - label) // 2

        return ans[::-1]