def _push(a,n):
    stack = []
    
    for val in a:
        if not stack:
            stack.append((val, val))
        else:
            curr_min = stack[-1][1]
            stack.append((val, min(val, curr_min)))
    return stack
            
def _getMinAtPop(stack):
    while stack:
        curr_min = stack[-1][1]
        print(curr_min, end=" ")
        stack.pop()