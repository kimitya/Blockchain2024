# Function to encrypt the message using Caesar Cipher
def caesar_encrypt(plaintext, shift):
    result = ""

    for i in range(len(plaintext)):
        char = plaintext[i]

        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char

    return result


def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)  # Decryption is simply shifting backwards

plaintext = "What has a head like a cat.Feel like a cat.A tail like a cat.But isn't a cat?"
shift = 12

ciphertext = caesar_encrypt(plaintext, shift)
print(f"Encrypted: {ciphertext}")

decrypted_text = caesar_decrypt(plaintext, shift)
print(f"Decrypted: {decrypted_text}")
