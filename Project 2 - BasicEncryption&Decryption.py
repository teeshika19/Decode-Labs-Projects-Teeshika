# Cyber Security Project 2
# Basic Encryption and Decryption
# Caesar Cipher

# Function to encrypt a message
def encrypt(text, shift):

    encrypted_text = ""

    for char in text:

        # Check for uppercase letters
        if char.isupper():

            # Convert character to ASCII and apply shift
            encrypted_char = chr((ord(char) - 65 + shift) % 26 + 65)

            encrypted_text += encrypted_char

        # Check for lowercase letters
        elif char.islower():

            encrypted_char = chr((ord(char) - 97 + shift) % 26 + 97)

            encrypted_text += encrypted_char

        # Keep spaces, numbers and punctuation unchanged
        else:
            encrypted_text += char

    return encrypted_text


# Function to decrypt a message
def decrypt(text, shift):

    decrypted_text = ""

    for char in text:

        # Check for uppercase letters
        if char.isupper():

            decrypted_char = chr((ord(char) - 65 - shift) % 26 + 65)

            decrypted_text += decrypted_char

        # Check for lowercase letters
        elif char.islower():

            decrypted_char = chr((ord(char) - 97 - shift) % 26 + 97)

            decrypted_text += decrypted_char

        # Keep spaces, numbers and punctuation unchanged
        else:
            decrypted_text += char

    return decrypted_text


# Main program
print("CAESAR CIPHER PROGRAM")
print("Encryption & Decryption")

# Get message from user
message = input("\nEnter the message you want to encrypt: ")

# Get shift key from user
while True:
    try:
        shift = int(input("Enter the shift key: "))
        break

    except ValueError:
        print("Invalid input! Please enter a number.")

# Encrypt the message
encrypted_message = encrypt(message, shift)

# Decrypt the encrypted message
decrypted_message = decrypt(encrypted_message, shift)

# Display results
print("Original Message: ", message)

print("Encrypted Message:", encrypted_message)

print("Decrypted Message:", decrypted_message)

print("\nEncryption and decryption completed successfully!")
