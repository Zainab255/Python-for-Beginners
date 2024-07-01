def first_last_digits(n):
    n_str = str(n)
    return n_str[0], n_str[-1]

# Test cases
number = 12345
first, last = first_last_digits(number)
print(f"First digit: {first}")
print(f"Last digit: {last}")
