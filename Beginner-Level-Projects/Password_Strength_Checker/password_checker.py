import re

def check_password_strength(password):
    # Criteria for strength
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r"[A-Z]", password) is not None
    lowercase_criteria = re.search(r"[a-z]", password) is not None
    number_criteria = re.search(r"[0-9]", password) is not None
    special_char_criteria = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None

    # Calculate score
    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])

    # Determine strength
    if score < 3:
        return "Weak", "Consider making your password longer and including a mix of letters, numbers, and special characters."
    elif score == 3 or score == 4:
        return "Medium", "Your password is decent but could be improved by adding more variety."
    else:
        return "Strong", "Your password is strong. Good job!"

# Input from the user
print("Password Strength Checker")
password = input("Enter your password: ")

# Check strength
strength, feedback = check_password_strength(password)
print(f"\nPassword Strength: {strength}")
print(f"Feedback: {feedback}")
