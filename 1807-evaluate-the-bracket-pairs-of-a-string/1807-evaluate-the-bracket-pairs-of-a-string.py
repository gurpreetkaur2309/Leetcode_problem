class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        knowledge = dict(knowledge)
        result = []
        key = ""
        inside = False

        for ch in s:
            if ch == '(':
                inside = True
                key = ""

            elif ch == ')':
                result.append(knowledge.get(key, '?'))
                inside = False

            elif inside:
                key += ch

            else:
                result.append(ch)

        return ''.join(result)