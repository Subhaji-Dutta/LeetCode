class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, path, remaining):
            # Base case
            if remaining == 0:
                result.append(path[:])
                return

            if remaining < 0:
                return

            # Try all candidates starting from 'start'
            for i in range(start, len(candidates)):
                # Choose
                path.append(candidates[i])

                # Explore (same i because we can reuse elements)
                backtrack(i, path, remaining - candidates[i])

                # Backtrack (undo choice)
                path.pop()

        backtrack(0, [], target)
        return result