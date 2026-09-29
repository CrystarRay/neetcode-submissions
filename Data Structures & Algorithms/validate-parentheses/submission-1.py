class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        closetOpen = {")" : "(", "]" : "[", "}" : "{" }
        for i in s:
            if i in closetOpen:
                if stack and stack[-1] == closetOpen[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False