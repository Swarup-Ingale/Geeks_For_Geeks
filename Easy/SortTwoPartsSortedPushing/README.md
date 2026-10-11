<h2><a href="#">Sort Two Parts SortedPushing...</a></h2>
<h3>Difficulty: Easy</h3><hr>
<p><span style="font-size: 18px;">Given an integer array <strong>arr[]</strong> where the two parts around a break point are individually sorted, merge them into a single sorted array.&nbsp; The break point can be anywhere in the array, including at the beginning or end.</span></p><p><span style="font-size: 18px;"><strong>Examples:</strong></span></p><pre><span style="font-size: 18px;"><strong>Input: </strong>arr[] = [2, 3, 8, -1, 7, 10]
<strong>Output: </strong>[-1, 2, 3, 7, 8, 10] 
<strong>Explanation: </strong>[2, 3, 8] and [-1, 7, 10] are sorted in the original array. The overall sorted version is [-1 2 3 7 8 10].</span></pre><pre><span style="font-size: 18px;"><strong>Input: </strong>arr[] = [-4, 6, 9, -1, 3]
<strong>Output: </strong>[-4, -1, 3, 6, 9]
<strong>Explanation: </strong>[-4, 6, 9] and [-1, 3] are sorted in the original array. The overall sorted version is [-4 -1 3 6 9].</span></pre><pre><span style="font-size: 18px;"><strong>Input: </strong>arr[] = [10, 20, 30]
<strong>Output: </strong>[10, 20, 30]
<strong>Explanation: </strong>One part is empty and the other part is whole array which is already sorted.</span></pre>