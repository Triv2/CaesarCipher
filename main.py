alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
alphabet_length = len(alphabet)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def cipher(direction, text, shift):
    encrypted_message = ""
    decrypted_message = ""
    for letter in text:
        start = alphabet.index(letter)

        end1 = start + shift
        if end1 >= alphabet_length:
            end1 = end1 - alphabet_length
        encrypted_message += alphabet[end1]

        end2 = start - shift
        if end2 <= 1:
            end2 = alphabet_length + end2
        decrypted_message += alphabet[end2]

    if direction == 'encode':
        print(f"The decrypted message is: {encrypted_message}.")
    elif direction == 'decode':
        print(f"The decrypted message is: {decrypted_message}.")


cipher(direction, text, shift)

# def decrypt(text,shift):
#   message=""
#   for letter in text:
#     start = alphabet.index(letter)
#     end = start - shift
#     if end <= 0:
#       end= alphabet_length + end
#     message  += alphabet[end]
#   print(f"The decrypted message is: {message}.")

# def encrypt(text,shift):
#   message=""
#   for letter in text:
#     start = alphabet.index(letter)
#     end = start + shift
#     if end >= alphabet_length:
#       end= end - alphabet_length
#     message  += alphabet[end]
#   print(f"The encrypted message is: {message}.")

# if direction == 'encode':
#   encrypt(text,shift)
# elif direction == 'decode':
#   decrypt(text,shift)
