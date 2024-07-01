def validate_atm_pincode(pin_code):
    if (len(pin_code) == 4 or len(pin_code) == 6) and pin_code.isdigit():
        return "Valid PIN Code"
    else:
        return "Invalid PIN Code"

# Test cases
print(validate_atm_pincode("1234"))  # Valid PIN Code
print(validate_atm_pincode("123456"))  # Valid PIN Code
print(validate_atm_pincode("123"))  # Invalid PIN Code
print(validate_atm_pincode("abcdef"))  # Invalid PIN Code
