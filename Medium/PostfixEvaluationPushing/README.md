<h2><a href="#">Postfix EvaluationPushing...</a></h2>
<h3>Difficulty: Medium</h3><hr>
<p><span style="font-size: 14pt;">You are given an array of strings <strong>arr[]</strong> that represents a valid arithmetic expression written in Postfix Notation. Your task is to evaluate the expression and return an integer representing its value.</span></p>
<ul>
<li>T<span style="font-size: 18.6667px;"><span style="font-size: 18.6667px;">he division operation between two integers always computes the </span><strong style="font-size: 18.6667px;">floor value,</strong><span style="font-size: 18.6667px;"> i.e floor(5 / 3) = 1 and floor(-5 / 3) = -2.</span></span></li>
<li><span style="font-size: 18.6667px;"><span style="font-size: 18.6667px;">It is guaranteed that the result of the expression and all intermediate calculations will fit in a 32-bit signed integer.</span></span></li>
<li><span style="font-size: 14pt;">arr[i] is either an operator: "+", "-", "*", "/" or "^", or an integer in the range [-10<sup>4</sup>, 10<sup>4</sup>]</span></li>
</ul>
<p><span style="font-size: 14pt;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 14pt;"><strong style="font-size: 18.6667px;">Input:</strong><span style="font-size: 18.6667px;"> arr[] = ["2", "3", "1", "*", "+", "9", "-"]
</span><strong style="font-size: 18.6667px;">Output:</strong><span style="font-size: 18.6667px;"> -4
</span><strong style="font-size: 18.6667px;">Explanation:</strong><span style="font-size: 18.6667px;"> If the expression is converted into an infix expression, it will be 2 + (3 * 1) – 9 = 5 – 9 = -4.</span></span></pre>
<pre><span style="font-size: 14pt;"><span style="font-size: 18.6667px;"><strong>Input:</strong> arr[] = ["2", "3", "^", "10", "+"]
<strong>Output:</strong> 18
<strong>Explanation:</strong> If the expression is converted into an infix expression, it will be 2 ^ 3 + 10 = 8 + 10 = 18.</span></span></pre>
<p><span style="font-size: 14pt;"><strong>Constraints:<br></strong></span><span style="font-size: 14pt;">3 ≤ arr.size() ≤ 10<sup>3</sup></span></p>