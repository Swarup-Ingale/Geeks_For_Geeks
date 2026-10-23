''' BST Node Structure
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def pairsViolatingBST(self, root):
        inorder_arr = []

        # Step 1: Extract the in-order traversal
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            inorder_arr.append(node.data)
            inorder(node.right)

        inorder(root)

        n = len(inorder_arr)
        temp_arr = [0] * n

        # Step 2: Merge Sort to count inversions efficiently
        def mergeSortAndCount(left, right):
            inv_count = 0
            if left < right:
                mid = (left + right) // 2

                # Count inversions in the left half, right half, and during the merge
                inv_count += mergeSortAndCount(left, mid)
                inv_count += mergeSortAndCount(mid + 1, right)
                inv_count += merge(left, mid, right)

            return inv_count

        def merge(left, mid, right):
            i = left    # Starting index for left subarray
            j = mid + 1 # Starting index for right subarray
            k = left    # Starting index to be sorted
            inv_count = 0

            while i <= mid and j <= right:
                if inorder_arr[i] <= inorder_arr[j]:
                    temp_arr[k] = inorder_arr[i]
                    i += 1
                else:
                    # Inversion found: inorder_arr[i] > inorder_arr[j]
                    # Because the left subarray is sorted, all elements from i to mid are also > inorder_arr[j]
                    temp_arr[k] = inorder_arr[j]
                    inv_count += (mid - i + 1)
                    j += 1
                k += 1

            # Copy remaining elements of left subarray, if any
            while i <= mid:
                temp_arr[k] = inorder_arr[i]
                i += 1
                k += 1

            # Copy remaining elements of right subarray, if any
            while j <= right:
                temp_arr[k] = inorder_arr[j]
                j += 1
                k += 1

            # Copy the sorted subarray into Original array
            for idx in range(left, right + 1):
                inorder_arr[idx] = temp_arr[idx]

            return inv_count

        return mergeSortAndCount(0, n - 1)