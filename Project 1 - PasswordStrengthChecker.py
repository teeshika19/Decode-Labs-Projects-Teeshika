# Password Strength Checker
# DecodeLabs - Cyber Security Project 1

import hmac

# Function to check password strength
def check_password(password):

    # Check password length
    if len(password) < 8:
        return "WEAK"

    # Check for uppercase letters
    has_uppercase = any(char.isupper() for char in password)

    # Check for numbers
    has_number = any(char.isdigit() for char in password)

    # Check for symbols
    has_symbol = any(
        not char.isalnum() and not char.isspace()
        for char in password
    )

    # Determine password strength
    if has_uppercase and has_number and has_symbol:
        return "STRONG"

    elif has_uppercase or has_number or has_symbol:
        return "MEDIUM"

    else:
        return "WEAK"


# Main program
print("PASSWORD STRENGTH CHECKER")

# Ask user to enter a password
password = input("Enter your password: ")

# Ask user to confirm the password
confirm_password = input("Confirm your password: ")

# Compare passwords using constant-time comparison
password_bytes = password.encode("utf-8")
confirm_bytes = confirm_password.encode("utf-8")

if not hmac.compare_digest(password_bytes, confirm_bytes):

    print("\nPasswords do not match!")
    print("Please try again.")

else:

    print("\nPasswords match!")

    # Display password length
    print("\nPassword length:", len(password))

    # Check password strength
    strength = check_password(password)

    # Display password strength
    print("\nPassword strength:", strength)

    # Give recommendations
    if strength == "WEAK":

        print("Your password is weak.")
        print("Use at least 8 characters.")
        print("Include uppercase letters, numbers, and symbols to improve your password")

    elif strength == "MEDIUM":

        print("Your password has medium strength.")
        print("Try including all required character types to make it stronger")

    else:

        print("Your password is strong!")
        print("Good job! Your password meets all requirements.")

