class Solution:
    def isValid(self, s: str) -> bool:
        p = []

        for bracket in s:
            if bracket == "(":
                p.append(bracket)
            elif bracket == "{":
                p.append(bracket)
            elif bracket == "[":
                p.append(bracket)
            elif bracket == ")":
                if p == [] or p.pop() != "(":
                    return False
            elif bracket == "}":
                if p == [] or p.pop() != "{":
                    return False
            elif bracket == "]":
                if p == [] or p.pop() != "[":
                    return False

        return len(p) == 0