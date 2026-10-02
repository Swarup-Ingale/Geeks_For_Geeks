<h2><a href="#">Cycle Length in Linked ListPushing...</a></h2>
<h3>Difficulty: Medium</h3><hr>
<p><span style="font-size: 18.6667px;">Given the head<strong> </strong>of a linked list. A linked list contains a cycle if its last node is connected to a previous node. If the given list contains a cycle, return the length of the cycle. Otherwise, return 0.</span></p>
<p><span style="font-size: 18.6667px;"><strong>Note:</strong> Internally, the driver code uses an integer <strong>x</strong> to represent the position (1-based indexing) of the node to which the last node is connected. If x = 0, it means last node points to null which indicating there is no loop.</span></p>
<p><span style="font-size: 14pt;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 14pt;"><strong>Input: </strong><br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/904501/Web/Other/blobid0_1756186026.webp" width="434" height="90"><strong>
Output: </strong>4<strong>
Explanation: </strong>There exists a loop in the linked list 2 -&gt; 3 -&gt; 4 -&gt; 5, the length of the loop is 4.<br></span></pre>
<pre><span style="font-size: 14pt;"><strong>Input:</strong><br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/904501/Web/Other/blobid0_1756128118.webp" width="478" height="99">
<strong>Output:</strong> 3
<strong>Explanation: </strong>There exists a loop in the linked list 19 -&gt; 33 -&gt; 10, the length of loop is 3.</span></pre>
<pre><span style="font-size: 14pt;"><strong>Input:</strong><br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/904501/Web/Other/blobid1_1756128178.webp" width="512" height="68"><br><strong>Output: </strong>0<strong>
Explanation: </strong>There is no loop.</span></pre>