def count_letters(word):
    upper_case_count = sum(1 for c in word if c.isupper())
    lower_case_count = sum(1 for c in word if c.islower())
    return upper_case_count, lower_case_count

# Test cases
word = "HelloWorld"
upper_case_count, lower_case_count = count_letters(word)
print(f"No. of upper case letters: {upper_case_count}")
print(f"No. of lower case letters: {lower_case_count}")
