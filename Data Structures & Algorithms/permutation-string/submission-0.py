class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        need = 26 * [0]
        window = 26 * [0]
        for i in range(len(s1)):
            need[ord(s1[i]) - ord('a')] += 1

        for r in range(len(s2)):
            window[ord(s2[r]) - ord('a')] += 1
            if r >= n:
                window[ord(s2[r - n]) - ord('a')] -= 1
            if window == need:
                return True
        return False

                
        