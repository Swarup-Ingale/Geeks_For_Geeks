class Solution:
    def posInfinite(self, s: str, pos: int) -> str:
        lengths = [len(s)]
        step = 1

        while lengths[-1] < pos:
            prev_len = lengths[-1]
            lengths.append(2 * prev_len + step)
            step += 1

        for i in range(len(lengths) - 1, 0, -1):
            prev_len = lengths[i - 1]
            dollar_count = i

            if pos <= prev_len:
                continue
            elif pos <= prev_len + dollar_count:
                return '$'
            else:
                offset = pos - (prev_len + dollar_count)
                pos = prev_len - offset + 1

        return s[pos - 1]