import random

ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode(text):

    shift_value = random.randint(1,24)

    new_text = ""

    for char in text:
        if char not in ALPHABET:
            new_text += char
        else:
            new_index = ALPHABET.index(char.lower())+shift_value
            if new_index >= len(ALPHABET):
                new_index -= len(ALPHABET)
            new_text += ALPHABET[new_index]

    return [new_text,shift_value]

def decode(cipher, shift_key):
    new_text = ""

    for char in cipher:
        if char not in ALPHABET:
            new_text += char
        else:
            origional_index = ALPHABET.index(char.lower())-shift_key
            if origional_index < 0:
                origional_index+=len(ALPHABET)
            new_text += ALPHABET[origional_index]

    return new_text

text = input("Enter text: ")

data = encode(text)

print (f"The shift value is : {data[1]}")
print (f"The encrypted message is: {data[0]}")

print (f"The origional message was: {decode(data[0],data[1])}")