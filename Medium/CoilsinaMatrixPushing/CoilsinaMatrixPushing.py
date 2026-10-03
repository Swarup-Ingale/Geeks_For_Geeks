class Solution:
    def formCoils(self, n: int) -> list[list[int]]:
        m = 4 * n
        max_val = m * m
        steps = [m - 1]
        current_step = m - 2
        while current_step > 0:
            steps.append(current_step)
            steps.append(current_step)
            current_step -= 2
            
        directions = [(1,0), (0, 1), (-1, 0), (0, -1)]
        current_direction = 0
        
        row, col = 0, 0
        
        coil1 = [(row * m) + col + 1]
        
        for s in steps:
            for _ in range(s):
                row += directions[current_direction][0]
                col += directions[current_direction][1]
                
                current_number = (row * m) + col + 1
                coil1.append(current_number)
            current_direction = (current_direction + 1) % 4
        
        coil2 = []
        for number in coil1:
            coil2.append((max_val + 1) - number)
            
        return [coil1, coil2]