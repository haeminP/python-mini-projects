from caesar_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caeser(text, shift):
    new_text = ""
    if direction == "decode":
        shift *= -1

    for letter in text:
        if letter in alphabet:
            index = alphabet.index(letter)
            new_index = index + shift
            new_text += alphabet[new_index]
        else:
            new_text += letter
    print(f"The {direction}d text is {new_text}")



should_continue = True
print(logo)
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    #in case user enters a shift that is greater than the number of letters in the alphabet
    shift %= 26
    caeser(text, shift)
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
    if result == "no":
        should_continue = False
        print("Goodbye")