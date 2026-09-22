class Solution:
    def findLongestWord(self, s: str, d: list) -> str:
        def get_next_idx(arr, target):
            left, right = 0, len(arr)
            while left < right:
                mid = (left + right) // 2
                if arr[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return left

        pos = [[] for _ in range(26)]
        for i, char in enumerate(s):
            pos[ord(char) - 97].append(i)

        best_word = ""

        for word in d:
            curr_idx = -1
            possible = True

            for char in word:
                char_idx = ord(char) - 97
                arr = pos[char_idx]

                idx_in_list = get_next_idx(arr, curr_idx)

                if idx_in_list == len(arr):
                    possible = False
                    break

                curr_idx = arr[idx_in_list]

            if possible:
                if len(word) > len(best_word) or (len(word) == len(best_word) and word < best_word):
                    best_word = word

        return best_word