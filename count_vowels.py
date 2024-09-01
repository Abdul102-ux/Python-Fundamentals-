
def count_vowels(text):
    vowels = 'aeiou'
    return sum(1 for char in text.lower() if char in vowels)


text = input("Enter a string: ")
print(f"The number of vowels in the string is: {count_vowels(text)}")
