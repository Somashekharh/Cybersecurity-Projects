# Password Strength Checker

## Description
The Password Strength Checker is a Python-based tool that evaluates the strength of a password based on specific criteria such as length, inclusion of uppercase and lowercase letters, numbers, and special characters. It provides a user-friendly assessment and actionable feedback to help users create strong, secure passwords.

## Features
- Validates password strength based on five criteria:
  - Minimum length (8 characters).
  - Contains uppercase and lowercase letters.
  - Includes at least one numeric digit.
  - Contains special characters.
- Categorizes password strength as Weak, Medium, or Strong.
- Provides feedback for improving weak or medium passwords.
- Lightweight and easy to run on any machine.

## How It Works
1. The script prompts the user to enter a password.
2. It checks the password against predefined rules:
   - Minimum length of 8 characters.
   - Includes uppercase and lowercase letters.
   - Contains at least one number and one special character.
3. Based on the score (0–5), the script categorizes the password as Weak, Medium, or Strong.
4. Feedback is displayed to help users strengthen their passwords.

## Requirements
- **Python 3.6** or higher
- No additional libraries required (uses Python's standard library)

## Usage Instructions
1. Clone or download the project to your local machine.
2. Navigate to the project directory in the terminal.
3. Run the script:
   bash :~ python password_checker.py
  
4. Enter a password when prompted.
5. View the password strength and feedback.

## File Structure
```
Password-Strength-Checker/
│
├── password_checker.py      # Main script for checking password strength
├── README.md                # Documentation of the project
```

## Sample Output
### Example 1: Weak Password
```plaintext
Password Strength Checker
Enter your password: 12345

Password Strength: Weak
Feedback: Consider making your password longer and including a mix of letters, numbers, and special characters.
```

### Example 2: Medium Password
```plaintext
Password Strength Checker
Enter your password: Hello123

Password Strength: Medium
Feedback: Your password is decent but could be improved by adding more variety.
```

### Example 3: Strong Password
```plaintext
Password Strength Checker
Enter your password: Hello@2023!

Password Strength: Strong
Feedback: Your password is strong. Good job!
```

## Future Improvements
- Add an option to suggest strong passwords automatically.
- Check passwords against common password lists to warn against weak or easily guessable passwords.
- Support batch processing of multiple passwords.
- Add a graphical user interface (GUI) for better usability.

## Credits
- Developed by [Somashekhar Hiremath]
- Inspired by best practices in password security and Python programming.

