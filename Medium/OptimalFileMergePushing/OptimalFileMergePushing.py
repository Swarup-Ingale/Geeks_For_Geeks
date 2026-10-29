class Solution:
    def minComputation(self, files):
        heapq.heapify(files)
        total_cost = 0

        while len(files) > 1:
            first = heapq.heappop(files)
            second = heapq.heappop(files)

            cost = first + second
            total_cost += cost

            heapq.heappush(files, cost)
            
        return total_cost