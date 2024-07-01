import re

sentence = input("Enter a sentence: ")
numbers = re.findall(r'\d+', sentence)
numbers = [int(num) for num in numbers]

if numbers:
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    print(f"Sum: {total_sum}")
    print(f"Average: {average}")
else:
    print("No numbers found in the sentence.")
