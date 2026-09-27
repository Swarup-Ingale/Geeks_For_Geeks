<h2><a href="#">Minimum Subtraction to Make All 0Pushing...</a></h2>
<h3>Difficulty: Easy</h3><hr>
<p><span style="font-size: 14pt;">Given a non-negative integer array <strong>arr[]</strong>. In one operation, you must:</span></p>
<ul>
<li><span style="font-size: 14pt;">Choose a positive integer x such that x is less than or equal to the smallest non-zero element in arr[].</span></li>
<li><span style="font-size: 14pt;">Subtract x from every positive element in arr[].</span></li>
</ul>
<p><span style="font-size: 14pt;">Return the minimum number of operations required to make every element of the array equal to 0.</span></p>
<p><strong><span style="font-size: 18px;">Examples:</span></strong></p>
<pre><span style="font-size: 18px;"><strong><span style="font-size: 18px;">Input:</span> </strong></span><span style="font-size: 18px;">arr[] = [1, 5, 0, 3, 5]
<strong>Output: </strong>3
<strong>Explanation:</strong></span>
<span style="font-size: 18px;">Choose x = 1. Array becomes [0, 4, 0, 2, 4].
Choose x = 2. Array becomes [0, 2, 0, 0, 2].
Choose x = 2. Array becomes [0, 0, 0, 0, 0].
Thus, the minimum number of operations required is 3.</span></pre>
<pre><strong><span style="font-size: 18px;">Input: </span></strong><span style="font-size: 18px;">arr[] = [0]
<strong>Output: </strong>0
<strong>Explanation: </strong></span><span style="font-size: 18px;">All elements are already 0, so no operation is required.</span></pre>
