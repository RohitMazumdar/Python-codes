def split_string(word):
    first_a_index = word.index('a')
    part1 = word[:first_a_index+1]
    part2 = word[first_a_index+1:]
    return part1, part2


# Prompt the user to enter a word
word = input("Enter a word containing the letter 'a': ")

# Split the string based on the first 'a'
part1, part2 = split_string(word)

# Print the two parts
print(part1)
print(part2)
