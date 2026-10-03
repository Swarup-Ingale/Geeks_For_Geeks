class Solution:
    def findPages(self, arr, k):
        n = len(arr)
        
        if k > n:
            return -1
        
        left = max(arr)
        right = sum(arr)
        ans = -1
        
        def is_possible(max_pages: int) -> bool:
            student_count = 1
            current_pages = 0
            
            for pages in arr:
                if current_pages + pages <= max_pages:
                    current_pages += pages
                
                else:
                    student_count += 1
                    current_pages = pages
                    
                    if student_count > k:
                        return False
            
            return True
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if is_possible(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return ans