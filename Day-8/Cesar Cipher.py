from logo import logo

print(logo)


def encrypt(text, shift):
    encypted = []
    for i in range(len(text)):
        encypted.append(ord(text[i]) + shift)

    output = []
    for i in range(len(encypted)):
        output.append(chr(encypted[i]))
    concat_ans = "".join(output)

    print(f'The decoded is {concat_ans}')


def decrypt(text, shift):
    decrypted = []
    for i in range(len(text)):
        decrypted.append(ord(text[i]) - shift)

    output = []
    for i in range(len(decrypted)):
        output.append(chr(decrypted[i]))
    concat_ans = "".join(output)

    print(f'The encoded version is {concat_ans}')


def call(direction , text , shift):

    if direction == 'encode':
        encrypt(text, shift)
    else:
        decrypt(text, shift)


while True:
    user_input = input("Enter a command (type 'exit' to quit): ")

    if user_input.lower() == 'exit':
        print("Exiting the program.")
        break  # Exit the loop
    else:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        call(direction, text, shift)







