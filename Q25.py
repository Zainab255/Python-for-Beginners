def check_all_elements_same(lst):
    return all(x == lst[0] for x in lst)

# Test case
lst = [1, 1, 1, 1]
print(check_all_elements_same(lst))  # True

lst = [1, 2, 1, 1]
print(check_all_elements_same(lst))  # False
