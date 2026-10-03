<h2><a href="#">Longest Substring with K UniquesPushing...</a></h2>
<h3>Difficulty: Medium</h3><hr>
<p data-start="157" data-end="313"><span style="font-size: 14pt;">You are given a string <strong>s</strong> </span><span style="font-size: 18.6667px;">consisting only lowercase alphabets </span><span style="font-size: 14pt;">and an integer </span><strong style="font-size: 14pt;">k</strong><span style="font-size: 14pt;">. Your task is to find the <strong>length </strong>of the <strong>longest substring</strong> that contains exactly </span><strong style="font-size: 14pt;">k</strong><span style="font-size: 14pt;"> distinct characters.</span></p><p data-start="157" data-end="313"><span style="font-size: 14pt;"><span style="font-size: 14pt;"><strong>Note :</strong> If no such substring exists, return </span><strong style="font-size: 14pt;">-1</strong><span style="font-size: 14pt;">.&nbsp;</span></span></p><p><span style="font-size: 18px;"><strong>Examples:</strong></span></p><pre><span style="font-size: 18px;"><strong>Input: </strong>s = "aabacbebebe</span><span style="font-size: 18px;">", k = 3
<strong>Output:</strong> 7
<strong>Explanation</strong>: The longest substring with exactly 3 distinct characters is "cbebebe", which includes 'c', 'b', and 'e'.
</span></pre><pre><span style="font-size: 18px;"><strong>Input</strong>: s = "aaaa", k = 2
<strong>Output:</strong> -1
<strong>Explanation</strong>: There's no substring with 2 distinct characters.<br></span></pre><pre><span style="font-size: 14pt;"><strong>Input: </strong>s = "aabaaab", k = 2
<strong>Output:</strong> 7
<strong>Explanation</strong>: </span><span style="font-size: 14pt;">The entire string "aabaaab" has exactly 2 unique characters 'a' and 'b', making it the longest valid substring.</span></pre>