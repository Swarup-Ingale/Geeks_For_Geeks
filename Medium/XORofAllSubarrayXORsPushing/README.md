<h2><a href="#">XOR of All Subarray XORsPushing...</a></h2>
<h3>Difficulty: Medium</h3><hr>
<p><span style="font-size: 14pt;">Given an integer array <strong>arr[]</strong>, find the XOR of the XOR values of all possible non-empty subarrays of the array.</span></p><p><strong><span style="font-size: 14pt;">Examples:</span></strong></p><pre><span style="font-size: 14pt; font-family: 'andale mono', monospace;"><strong>Input:</strong> arr[] = [1, 2, 3] 
<strong>Output: </strong>2
<strong>Explanation:</strong>
xor[1] = 1
xor[1, 2] = 3
xor[2, 3] = 1
xor[1, 2, 3] = 0
xor[2] = 2
xor[3] = 3
Result: 1 ^ 3 ^ 1 ^ 0 ^ 2 ^ 3 = 2
</span></pre><pre><span style="font-size: 14pt; font-family: 'andale mono', monospace;"><strong>Input:</strong> arr[] = [1, 2]
<strong>Output: </strong>0
<strong>Explanation:</strong>
xor[1] = 1
xor[1, 2] = 3
xor[2] = 2
Result: 1 ^ 3 ^ 2 = 0</span></pre>