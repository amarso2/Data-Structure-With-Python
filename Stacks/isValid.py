class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping.values(): 
                
                stack.append(char)
            elif char in mapping: 
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:  
                continue

        return not stack
    s=  input("Enter brekets")
    print(isValid(s))  
    print(isValid(s))  
    print(isValid(s))  
    print(isValid(s))  
    print(isValid(s))