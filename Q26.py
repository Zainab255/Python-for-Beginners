def camel_to_snake(camel_case_str):
    import re
    snake_case_str = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case_str).lower()
    return snake_case_str

# Test case
camel_case_str = "pythonLearning"
print(camel_to_snake(camel_case_str))  # python_learning
