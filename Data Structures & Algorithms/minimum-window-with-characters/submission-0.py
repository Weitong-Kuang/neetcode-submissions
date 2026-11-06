class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = Counter()
        vaild = 0

        left = right = 0
        start = 0
        best_len = float('inf')

        while right < len(s):
            in_char = s[right]
            right += 1
            if in_char in need:
                window[in_char] += 1
                if window[in_char] == need[in_char]:
                    vaild += 1
            while vaild == len(need):
                if right - left < best_len:
                    best_len = right - left
                    start = left
                out_char = s[left]
                left += 1
                if out_char in need:
                    if window[out_char] == need[out_char]:
                        vaild -= 1
                    window[out_char] -= 1
        if best_len == float('inf'):
            return ""
        else:
            return s[start:start + best_len]

        