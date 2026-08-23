class Solution:
    def sumGame(self, num):
        n = len(num) // 2
        left = num[:n]
        right = num[n:]

        a = sum(int(x) for x in left if x != '?')
        b = sum(int(x) for x in right if x != '?')

        x = left.count('?')
        y = right.count('?')

        return 2 * (a - b) != 9 * (y - x)