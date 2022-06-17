def encrypt(text, shift):
    cipher_text = ""
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift
            new_letters = alphabet[new_position]
            cipher_text += new_letters
        else:
            cipher_text += char
    print(f"Your encoded message is: {cipher_text}")


def decrypt(text, shift):
    default_text = ""
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position - shift
            new_letter = alphabet[new_position]
            default_text += new_letter
        else:
            default_text += char
    print(f"Your decoded message is : {default_text}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
game_is_on = True
while game_is_on:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:
        print("Please check your spellings and try again")

    to_continue = input("Do you want to continue the game?: Type 'y' for yes or 'n' for no: ").lower()
    if to_continue == "n":
        game_is_on = False
        print("Game is over")

