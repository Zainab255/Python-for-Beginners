def is_python_file(filename):
    return filename.endswith('.py')

# Test cases
filename = "example.py"
print(is_python_file(filename))  # Yes

filename = "example.txt"
print(is_python_file(filename))  # No
