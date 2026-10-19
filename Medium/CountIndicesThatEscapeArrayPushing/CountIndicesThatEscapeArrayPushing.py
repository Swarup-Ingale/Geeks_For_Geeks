class Solution:
    def goodIndices(self, arr):
        n = len(arr)
        state = [0] * n
        good_count = 0
        
        for i in range(n):
            if state[i] != 0:
                continue
                
            path = []
            curr = i
            is_good = False
            
            while True:
                if curr < 0 or curr >= n:
                    is_good = True
                    break

                if state[curr] == 1 or state[curr] == 3:
                    is_good = False
                    break

                if state[curr] == 2:
                    is_good = True
                    break

                state[curr] = 1
                path.append(curr)
                curr = curr + arr[curr]

            final_state = 2 if is_good else 3
            for node in path:
                state[node] = final_state
                if is_good:
                    good_count += 1
                    
        return good_count