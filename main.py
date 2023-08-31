import random
import string

# Open the text file in read mode
file_path = 'wordlist.10000.txt'  # Replace with the actual file path
word_list = []

with open(file_path, 'r') as file:
    for line in file:
        # Remove the newline character at the end of each line
        cleaned_line = line.strip()
        word_list.append(cleaned_line)

# Now, the 'lines' list contains each line from the text file as an item
print(word_list)

#letters_available = ''.join(random.choice(string.ascii_lowercase) for _ in range(4))

# Generate random letters based on characters in the word list
unique_chars = set(''.join(word_list))
letters_available = ''.join(random.choice(list(unique_chars)) for _ in range(5))
print("Random letters:", letters_available)

print (letters_available)

def can_spell_words(letters_available, word_list):
    spellable_words = []
    for word in word_list:
        if len(word) >= 3 and all(letter in letters_available for letter in word):
            spellable_words.append(word)
    return spellable_words

# Find and print words that can be spelled using the random letters
spellable_words = can_spell_words(letters_available, word_list)
if spellable_words:
    print("The random letters can spell the following words:")
    for word in spellable_words:
        print(word)
else:
    print("The random letters cannot spell any word from the list.")

points = 0

user_input = input("Enter your value: ")

if user_input in spellable_words and len(user_input) >= 3:
    print('Correct!')
    if len(user_input) == 3:
        points += 1
    elif len(user_input) > 3:
        points += len(user_input) - 1
    print(points)
elif len(user_input) < 3:
   print ('Too short!')
else:
    print('Try again!')


