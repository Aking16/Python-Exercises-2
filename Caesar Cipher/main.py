def caesar_cipher(text, shift):
    result = []
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap around using modulo
            shifted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            result.append(shifted_char)
        else:
            # Non-alphabetic characters remain unchanged
            result.append(char)
    return ''.join(result)

while True:
    if __name__ == "__main__":
        plaintext = input("Enter text to encrypt: ")
        shift = 3  # Shift by 3 for encryption
        encrypted = caesar_cipher(plaintext, shift)
        print(f"Encrypted: {encrypted}")

        decrypted = caesar_cipher(encrypted, -shift)  # Use negative shift for decryption
        print(f"Decrypted: {decrypted}")