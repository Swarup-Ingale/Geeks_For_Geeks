<h2><a href="#">Process Zeros and Neighbors in GridPushing...</a></h2>
<h3>Difficulty: Easy</h3><hr>
<p><span style="font-size: 18px;">Given a matrix <strong>mat[][]</strong> of&nbsp; size n x m. Your task is to process Zeroes, that means in whole matrix when you find a zero, change that element to sum of the upper, lower, left and right value and make</span><span style="font-size: 18px;"> its four adjacent (upper, lower, left, and right) values zero.</span></p>
<p><span style="font-size: 18px;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: </strong>mat[][] = [[1, 2, 3, 4]
                [5, 6, 0, 7] 
&nbsp;               [8, 9, 4, 6]
                [8, 4, 5, 2]]
<strong>Output:</strong> mat[][] = [[1, 2, 0, 4]
&nbsp;                [5, 0, 20, 0]
                 [8, 9, 0, 6] 
&nbsp;                [8, 4, 5, 2]]
<strong>Explanation:</strong> As mat[1][2] = 0, we will perform the operation here. Then mat[1][2] = mat[0][2] + mat[2][2] + mat[1][1]  + mat[1][3] and mat[0][2] = matrix[2][2] = matrix[1][1] = matrix[1][3] = 0.</span>
</pre>
<pre><span style="font-size: 18px;"><strong>Input: </strong>mat[][] = [[1, 2] 
&nbsp;               [3, 4]]
<strong>output: </strong>mat[][] = [[1, 2] 
&nbsp;                [3, 4]]</span>&nbsp;&nbsp;</pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 ≤ n, m ≤ 100<br>0 ≤ mat[i][j] ≤ 100, where 0 ≤ i ≤ n and 0 ≤ j ≤ m</span></p>