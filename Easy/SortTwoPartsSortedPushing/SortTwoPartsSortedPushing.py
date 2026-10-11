class Solution:
    def mergeTwoParts(self, arr):
        n = len(arr)
        break_point = -1
        for i in range(1, n):
            if arr[i] < arr[i - 1]:
                break_point = i
                break

        if break_point == -1:
            return arr

        res = []
        p1 = 0
        p2 = break_point

        while p1 < break_point and p2 < n:
            if arr[p1] <= arr[p2]:
                res.append(arr[p1])
                p1 += 1
            else:
                res.append(arr[p2])
                p2 += 1

        if p1 < break_point:
            res.extend(arr[p1:break_point])
        if p2 < n:
            res.extend(arr[p2:n])

        arr[:] = res
        return arr