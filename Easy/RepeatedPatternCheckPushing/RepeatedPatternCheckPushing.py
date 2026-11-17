class Solution:
    def findPattern(self, s):
        x_count = 0
        y_count = 0

        for ch in s:
            if ch == 'x':
                if y_count > 0:
                    if x_count != y_count:
                        return False
                    x_count = 0
                    y_count = 0
                x_count += 1
            else:
                if x_count == 0:
                    return False
                y_count += 1

        return x_count == y_count