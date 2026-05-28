import re

def check_password_strength(password):
    # Criteria
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # Collect errors
    errors = {
        "Length >= 8": not length_error,
        "Contains digit": not digit_error,
        "Contains uppercase": not uppercase_error,
        "Contains lowercase": not lowercase_error,
        "Contains symbol": not symbol_error
    }

    # Strength evaluation
    score = sum(errors.values())
    if score == 5:
        strength = "Strong"
    elif 3 <= score < 5:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, errors


# Example usage
password = input("Enter a password: ")
strength, details = check_password_strength(password)

print(f"Password strength: {strength}")
print("Criteria check:")
for rule, passed in details.items():
    print(f"- {rule}: {'✔️' if passed else '❌'}")
