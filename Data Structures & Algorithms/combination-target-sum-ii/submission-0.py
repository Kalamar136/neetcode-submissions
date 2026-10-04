class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Strategy backtracking:
        # Compute the distribution of candidates with dict
        # For each candidate, try to compute sum with or without it (while handling duplicates properly)

        candidates_dist = {}
        for candidate in candidates:
            candidates_dist[candidate] = candidates_dist.get(candidate, 0) + 1
        
        output = []
        unique_candidates = list(candidates_dist.keys())

        def backtrack_candidates(i, summation, cur, rep):
            if summation == target:
                output.append(cur)
                return
            
            if summation > target or i >= len(unique_candidates):
                return
            
            next_i, next_rep = (i + 1, 1) if candidates_dist[unique_candidates[i]] == rep else (i, rep + 1)
            
            backtrack_candidates(next_i, summation + unique_candidates[i], cur + [unique_candidates[i]], next_rep)
            
            backtrack_candidates(i+1, summation, cur, 1)
        
        backtrack_candidates(0, 0, [], 1)
        return output