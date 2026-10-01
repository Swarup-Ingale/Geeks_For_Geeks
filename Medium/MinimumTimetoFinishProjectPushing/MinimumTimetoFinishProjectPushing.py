import sys
sys.setrecursionlimit(2 * 10**5)

class Solution:
    def minTime(self, duration, dependencies):
        n = len(duration)

        adj = [[] for _ in range(n)]
        for u, v in dependencies:
            adj[u].append(v)

        state = [0] * n
        dp = [-1] * n

        def dfs(node):
            if state[node] == 1:
                return -1
            if state[node] == 2:
                return dp[node]

            state[node] = 1

            max_dependent_time = 0
            for neighbor in adj[node]:
                res = dfs(neighbor)
                if res == -1:
                    return -1
                max_dependent_time = max(max_dependent_time, res)

            state[node] = 2
            dp[node] = duration[node] + max_dependent_time
            return dp[node]

        overall_max_time = 0
        for i in range(n):
            if state[i] == 0:
                result = dfs(i)
                if result == -1:
                    return -1

        return max(dp)