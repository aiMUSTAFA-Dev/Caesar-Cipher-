alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo
print(logo)

continue_1 = True
while continue_1:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def cipher(user_choice):
        if direction == "encrypt":
            def encrypt(original_text, shift_amount):
                cipher_text = ""
                for letter in original_text:
                    if letter in alphabet:
                        index = alphabet.index(letter) + shift_amount
                        index %= len(alphabet)
                        cipher_text += alphabet[index]
                    else:
                        cipher_text += letter
                print(f"The Encrypt Text is: {cipher_text}")
            encrypt(text,shift)

        else:
            def decrypt(original_text, shift_amount):
                cipher_text = ""
                for letter in original_text:
                    if letter in alphabet:
                        index = alphabet.index(letter) - shift_amount
                        index % len(alphabet)
                        cipher_text += alphabet[index]
                    else:
                        cipher_text += letter
                print(f"The Decrypt Text is: {cipher_text}")
            decrypt(text,shift)

    cipher(user_choice= direction)

    continue_or_not = input("Enter \"Yes\" to go again, otherwise enter \"No\" ").lower()
    if continue_or_not == "no":
        continue_1 = False