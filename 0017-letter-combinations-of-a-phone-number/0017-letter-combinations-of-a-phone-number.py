# from typing import List

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

        # Start with an empty combination
        combinations = [""]

        for digit in digits:
            # Get the letters corresponding to the current digit
            letters = digit_to_letters[digit]
            new_combinations = []
            # For each combination so far, append each letter of the current digit
            for combination in combinations:
                for letter in letters:
                    new_combinations.append(combination + letter)
            # Update combinations with the newly generated combinations
            combinations = new_combinations

        return combinations
