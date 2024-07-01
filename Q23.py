N = int(input("Enter a number: "))

for i in range(1, N + 1):
    if i % 2 != 0:
        print(i)


def extract_and_sum(sentence):
    import re
    numbers = re.findall(r'\d+', sentence)
    numbers = list(map(int, numbers))
    return numbers, sum(numbers)

# Test case
sentence = "I am 24 years and 2 months old."
numbers, total_sum = extract_and_sum(sentence)
print(f"Extracted numbers: {numbers}")
print(f"Sum of numbers: {total_sum}")
