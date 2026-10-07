class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Sliding window strategy: If the window is narrow enough, we should be able to use k replacements so all letters are the same
        # The window length would be the output of the algorithm
        # The window length is the highest freq letter + k
        # We need to move the window across the whole string to evaluate all possible replacements
        # We move the wind_min and wind_max at most len(s) each

        # We start the window small then adapt depending on the highest freq letter
        window_letter_dist = {s[0]: 1}
        max_freq_letter = s[0]
        max_freq = 1
        wind_min = 0
        wind_max = 0
        out = 1

        while wind_max < len(s) - 1:
            wind_max += 1
            new_l = s[wind_max]
            window_letter_dist[new_l] = window_letter_dist.get(new_l, 0) + 1
            new_l_freq = window_letter_dist[new_l]
            if new_l_freq > max_freq:
                max_freq_letter = new_l
                max_freq = new_l_freq
            # We need to shrink the window
            if wind_max - wind_min + 1 > max_freq + k:
                l_del = s[wind_min]
                window_letter_dist[l_del] -= 1
                wind_min += 1
            if out < wind_max - wind_min + 1:
                out = wind_max - wind_min + 1
        
        return out