class Solution:
    def evaluatePostfix(self, arr):
        s = []
        for c in arr:
            if c in {"+", "-", "*", "/", "^"}:
                if s:
                    a = s.pop()
                    b = s.pop()
                    
                    if c == "+":
                        s.append(b + a)
                    elif c == "-":
                        s.append(b - a)
                    elif c == "*":
                        s.append(b * a)
                    elif c == "/":
                        s.append(b // a)
                    elif c == "^":
                        s.append(b ** a)
            else:
                s.append(int(c))
        
        return s[0]