class Solution:
    def maxHeight(self, height: list[int], width: list[int], length: list[int]) -> int:
        boxes = []
        n = len(height)
        
        for i in range(n):
            h = height[i]
            w = width[i]
            l = length[i]
            
            boxes.append([h, max(w, l), min(w, l)])
            boxes.append([w, max(h, l), min(h, l)])
            boxes.append([l, max(w, h), min(w, h)])
            
        boxes.sort(key = lambda x: x[1] * x[2], reverse = True)
        total_boxes = len(boxes)
        
        dp = [0] * total_boxes
        for i in range(total_boxes):
            dp[i] = boxes[i][0]
        
        for i in range(1, total_boxes):
            for j in range(0, i):
                if boxes[i][1] < boxes[j][1] and boxes[i][2] < boxes[j][2]:
                    if dp[i] < dp[j] + boxes[i][0]:
                        dp[i] = dp[j] + boxes[i][0]
                        
        return max(dp)