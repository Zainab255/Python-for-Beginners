def modify_string(s):
    if len(s) < 2:
        return s
    return s[0] + '*' * (len(s) - 2) + s[-1]

# Test cases
input_string = "HelloWorld"
print(modify_string(input_string))  # H********d
