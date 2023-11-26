# String Permutations Generator(BRUTE FORCE)

This Python script generates all possible permutations of a given string using the random module.

## Overview

Ever wondered about the countless ways you can rearrange the characters of a string? This script is your answer! By utilizing the randomness of the `random` module, the script generates and showcases all unique permutations of a string.

- **Takes a string as input:** The journey begins by prompting the user to enter a string. For instance, you can input "cow" to explore its various permutations.

- **Converts characters to ASCII values:** Each character in the input string is converted to its ASCII value. This step adds a unique numeric representation for each character, setting the stage for diverse permutations.

- **Calculates the factorial of string length:** The script computes the factorial of the length of the input string. This value ensures that the loop runs until the new list has the required number of permutations.

- **Generates unique permutations:** The script employs randomness to create unique permutations, ensuring that each sequence is distinct from the others. This process involves selecting characters based on their ASCII values.

- **Prints all possible permutations:** Once the permutations are generated, the script prints them for you to marvel at. For example:

## Example
Suppose you enter the string "cow". The script will output various unique permutations of the characters in the string. For example:
```bash
ALL POSSIBLE PERMUTATIONS OF THE ENTERED STRING: 6

['wco', 'ocw', 'woc', 'owc', 'cwo', 'cow']
```

## Usage

1. Run the script.
2. Enter a string when prompted. For example, enter "cow".

## Disadvantage
• Since it's a brute force not an algorithm it can take lot of time for longer strings

```bash
python string_permutations_generator.py
```
## Created On
31 October 2023
