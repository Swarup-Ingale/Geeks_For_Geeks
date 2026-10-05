class Solution:
    def infixToPostfix(self, s):
        prec = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
        stack = []
        o = []
        
        for c in s:
            if c.isalnum():
                o.append(c)
            elif c == "(":
                stack.append(c)
            elif c == ")":
                while stack and stack[-1] != "(":
                    o.append(stack.pop())
                stack.pop()
            
            else:
                if c == "^":
                    while stack and stack[-1] != "(" and prec[c] < prec[stack[-1]]:
                        o.append(stack.pop())
                        
                else:
                    while stack and stack[-1] != "(" and prec[c] <= prec[stack[-1]]:
                        o.append(stack.pop())
            
                stack.append(c)
            
        while stack:
            o.append(stack.pop())
        return "".join(o)