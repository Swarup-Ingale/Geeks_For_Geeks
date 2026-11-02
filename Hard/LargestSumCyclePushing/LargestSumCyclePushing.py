class Solution:
    def largestSumCycle(self, edge):
        n = len(edge)
        vis = [False] * n
        path_vis = [False] * n
        ans = -1

        for i in range(n):
            if not vis[i]:
                curr = i
                path = []

                while curr != -1 and not vis[curr]:
                    vis[curr] = True
                    path_vis[curr] = True
                    path.append(curr)
                    curr = edge[curr]

                if curr != -1 and path_vis[curr]:
                    cycle_sum = curr
                    temp = edge[curr]

                    while temp != curr:
                        cycle_sum += temp
                        temp = edge[temp]

                    ans = max(ans, cycle_sum)

                for node in path:
                    path_vis[node] = False

        return ans