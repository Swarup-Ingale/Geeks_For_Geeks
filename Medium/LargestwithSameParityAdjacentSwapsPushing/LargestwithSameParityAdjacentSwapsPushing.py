class Solution:
    def lexicographicallyLargest(self, arr: list[int]) -> list[int]:
        n = len(arr)
        start = 0
        
        while start < n:
            end = start

            while end + 1 < n and (arr[end] % 2) == (arr[end + 1] % 2):
                end += 1

            arr[start:end + 1] = sorted(arr[start:end + 1], reverse=True)

            start = end + 1
            
        return arr