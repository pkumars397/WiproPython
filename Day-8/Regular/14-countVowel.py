#Count the number of vowels in a string.

def countVowels(s):
    vowelCountList=[1 for char in s.lower() if char in "aeiou"]
    return sum(vowelCountList)

print(countVowels("hellO worild"))