class Solution:
	def twoSum(self, arr, target):
        s = set()
		
        for num in arr:
            complement = target - num
            if complement in s:
                return True
            s.add(num)
            
        return False