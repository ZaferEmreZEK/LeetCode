class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i in ["{", "(", "["]:
                stack.append(i)
                continue
            
            elif i in ["]", ")", "}"] and stack:
                temp = stack.pop()
                if (i == "}" and temp == "{") or (i == "]" and temp == "[") or (i == ")" and temp == "("):
                    continue
                else:
                    return False
            return False
        
        if stack:
            return False
        return True




                
        
        