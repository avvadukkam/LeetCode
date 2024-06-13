class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        event1S = int(event1[0].replace(":",""))
        event1E = int(event1[1].replace(":",""))
        event2S = int(event2[0].replace(":",""))
        event2E = int(event2[1].replace(":",""))
        return not (event2S > event1E or event1S > event2E)

#OR

class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        start1, end1 = event1
        start2, end2 = event2
        if start2 > end1 or start1 > end2:
            return False
        return True