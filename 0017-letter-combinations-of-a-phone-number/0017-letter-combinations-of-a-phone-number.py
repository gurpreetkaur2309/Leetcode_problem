from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        # Mapping of digits to corresponding letters
        digit_to_letters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        def backtrack(index: int, current_combination: List[str]):
            # Base case: if the combination is complete
            if index == len(digits):
                combinations.append(''.join(current_combination))
                return

            # Get the letters corresponding to the current digit
            letters = digit_to_letters[digits[index]]
            for letter in letters:
                current_combination.append(letter)  # Choose
                backtrack(index + 1, current_combination)  # Explore
                current_combination.pop()  # Undo the choice

        combinations = []
        backtrack(0, [])
        return combinations
