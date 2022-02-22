from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def caesar(text, shift, direction):
    text = text.lower()
    if direction == 'decode':
        shift *= -1
    new_text = ''
    for letter in text:
        if letter.isalpha():
            index = alphabet.index(letter)
            new_index = (index + shift) % 26
            new_text += alphabet[new_index]
        else:
            new_text += letter
    print(new_text)

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    more = input("More to do? ").casefold()
    if more == 'n' or more == 'no':
        break

print("BYE BYE!")