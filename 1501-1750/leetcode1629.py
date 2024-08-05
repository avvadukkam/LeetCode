class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        maxDuration = releaseTimes[0] 
        slowKey = keysPressed[0]

        for i in range(1, len(releaseTimes)):
            duration = releaseTimes[i] - releaseTimes[i - 1]
            if duration > maxDuration:
                maxDuration = duration
                slowKey = keysPressed[i]
            elif duration == maxDuration:
                slowKey = max(slowKey, keysPressed[i])

        return slowKey