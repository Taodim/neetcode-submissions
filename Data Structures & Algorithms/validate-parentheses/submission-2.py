class Solution:
    def isValid(self, s: str) -> bool:
        #converted = list(s)
        if (len(s) % 2) != 0:
            return False
        
        stack = []
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)


            elif ((len(stack) == 0) or
                (c == ")" and stack[len(stack) - 1] != "(") or
                (c == "}" and stack[len(stack) - 1] != "{") or
                (c == "]" and stack[len(stack) - 1] != "[")):
                return False
            else:
                stack.pop()


        return len(stack) == 0
                