class Solution:
    def searchWord(self, mat, word):
        if not mat or not mat[0] or not word:
            return []

        n = len(mat)
        m = len(mat[0])
        word_len = len(word)
        ans = []

        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]

        for r in range(n):
            for c in range(m):
                if mat[r][c] == word[0]:
                    found = False
                    for dr, dc in directions:
                        curr_r = r + dr
                        curr_c = c + dc
                        match = True

                        for k in range(1, word_len):
                            if (0 <= curr_r < n and 0 <= curr_c < m and 
                                mat[curr_r][curr_c] == word[k]):
                                curr_r += dr
                                curr_c += dc
                            else:
                                match = False
                                break

                        if match:
                            found = True
                            break 

                    if found:
                        ans.append([r, c])

        return ans