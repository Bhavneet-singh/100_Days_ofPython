from logo import logo
print(logo)

user_input =input("Do you want to continue 1 for Yes , 0 for No : ")
if int(user_input) == 1:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))



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

    if direction == 'encode':
        encrypt(text , shift)
    else:
        decrypt(text , shift)

