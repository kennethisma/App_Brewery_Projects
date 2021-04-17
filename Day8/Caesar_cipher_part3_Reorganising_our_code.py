##################################### My solution ###################################################
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
#             'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# # TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().


# def caesar(cipher_text, shift_amount, options):
#     if options == 'encode':
#         encrypted_text = ""
#         for letter in cipher_text:
#             position = alphabet.index(letter)
#             new_position = position + shift_amount
#             encrypted_text += alphabet[new_position]
#         print(f"The encoded text is {encrypted_text}")

#     elif options == 'decode':
#         decrypted_text = ""
#         for letter in cipher_text:
#             position = alphabet.index(letter)
#             new_position = position - shift_amount
#             decrypted_text += alphabet[new_position]
#         print(f"The decoded text is {decrypted_text}")

#### I used the same code ####


# # TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
# caesar(cipher_text=text, shift_amount=shift, options=direction)


########################################### Angela's Solution ##########################################################

## Angela wrote cleaner code ##
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"Here's the {direction}d result: {end_text}")


# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
