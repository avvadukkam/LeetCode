class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        rule =  ["type", "color", "name"]
        index_rule = rule.index(ruleKey)
        count = 0
        for i in items:
            if i[index_rule] == ruleValue:
                count += 1
        return count