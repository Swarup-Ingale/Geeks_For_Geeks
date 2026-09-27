<h2><a href="#">Make All ZeroPushing...</a></h2>
<h3>Difficulty: Medium</h3><hr>
<p class="" data-start="210" data-end="358"><span style="font-size: 14pt;">Two players are playing a game involving energy stacks. Each stack contains a certain number of energy crystals represented as integers in an array <strong>arr[]</strong>.</span></p>
<p class="" data-start="360" data-end="515"><span style="font-size: 14pt;">Players take turns. On each turn, a player must remove one entire stack (i.e., remove one element from the array). However, there's a special rule:</span></p>
<p><span style="font-size: 14pt;"> </span></p>
<ul>
<li><span style="font-size: 14pt;">If the <strong data-start="526" data-end="541">bitwise XOR</strong> of the entire array is 0 before a player's turn, then that player instantly wins.</span><span style="font-size: 14pt;"> </span></li>
<li data-start="633" data-end="784"><span style="font-size: 14pt;">If it's not zero, they must remove one stack. The game continues until someone wins either due to the XOR rule or because the other player cannot move.</span></li>
</ul>
<p class="" data-start="895" data-end="948"><span style="font-size: 14pt;"> </span></p>
<p class="" data-start="786" data-end="883"><span style="font-size: 14pt;">Both players play optimally. You need to determine who will win for each initial array of stacks.</span></p>
<p class="" data-start="786" data-end="883"><span style="font-size: 14pt;">Return <strong>true</strong> if Player second wins otherwise return <strong>false</strong>.</span></p>
<p class="" data-start="115" data-end="226"><strong style="font-size: 14pt;">Examples:</strong></p>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>arr[] = [1, 2, 3]
<strong>Output: </strong>false<br><strong>Explanation: </strong>Since xor of the entire array is 0 before player 1's turn, player 1 wins.</span></pre>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>arr[] = [1, 2, 4]<br><strong>Output: </strong>true<br></span><span style="font-size: 14pt;"><strong>Explanation: </strong>Player1 removes 1 from arr[] on his turn, then player2 removes 2 from arr[], then player1 removes 4 which makes bitwise xor of arr[] as 0. Hence player2 wins.</span></pre>