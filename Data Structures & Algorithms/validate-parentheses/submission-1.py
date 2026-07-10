class Solution:
    def isValid(self, s: str) -> bool:
        openbrackets = ['(','{','[']
        closebrackets = [')','}',']']
        stack = []
        for bracket in s:
            if bracket in openbrackets:
                stack.append(bracket)
            else:
                try:
                    if stack.pop() != openbrackets[closebrackets.index(bracket)]:
                        return False
                except IndexError:
                    return False
        return len(stack) == 0
        