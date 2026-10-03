<h2><a href="#">Allocate Minimum PagesPushing...</a></h2>
<h3>Difficulty: Medium</h3><hr>
<p><span class="cf0" style="font-size: 14pt;">Given an array <strong>arr[] </strong>of integers, where each element <strong>arr[i]</strong> represents the number of pages in the i-th book. You also have an integer <strong>k</strong> representing the number of students. The task is to allocate books to each student such that:</span></p>
<ul>
<li><span class="cf0" style="font-size: 14pt;">Each student receives atleast one book.</span></li>
<li><span class="cf0" style="font-size: 14pt;">Each student is assigned a contiguous sequence of books.</span></li>
<li><span class="cf0" style="font-size: 14pt;">No book is assigned to more than one student.</span></li>
<li><span class="cf0" style="font-size: 14pt;">All books must be allocated.</span></li>
</ul>
<p class="pf0"><span class="cf0" style="font-size: 14pt;">The objective is to minimize the maximum number of pages<strong> </strong>assigned to any student. In other words, out of all possible allocations, find the arrangement where the student who receives the most pages still has the smallest possible maximum. If it is not possible to allocate books to all students, return <strong>-1</strong>;</span></p>
<p><span style="font-size: 14pt;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>arr[] = [12, 34, 67, 90], k = 2
<strong>Output: </strong>113
<strong>Explanation: </strong>Allocation can be done in following ways:<br>=&gt; [12] and [34, 67, 90] Maximum Pages = 191<br>=&gt; [12, 34] and [67, 90] Maximum Pages = 157<br>=&gt; [12, 34, 67] and [90] Maximum Pages = 113.<br>The third combination has the minimum pages assigned to a student which is 113.</span></pre>
<pre><span style="font-size: 14pt;"><span class="cf0"><strong>Input:</strong> arr[] = [15, 17, 20], k = 5<br></span><span class="cf0"><strong>Output: </strong>-1<br></span><span class="cf0"><strong>Explanation: </strong></span>Since there are more students than total books, it's impossible to allocate a book to each student.</span></pre>