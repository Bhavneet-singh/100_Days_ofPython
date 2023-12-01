from art import logo
import os

# bugs
#not showing winner at the end
print(logo)

arr = {}
winner_val = 0

def get_key_by_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None  # Return None if the value is not found


def call( name, bid):
    global winner_val
    if name in arr:
        arr[name].append(bid)
    else:
        arr[name] = [bid]
    winner_val = max(list(arr.values()))



print("Welcome to the secret auction program")

name = str(input("What is your name?: "))
bid = int(input("What's your bid? :"))
call(name, bid)



while True:

    toContinue = input("Are there any other bidders? Type yes or no: ")
    if toContinue == "yes":
        os.system('cls')
        name = str(input("What is your name?: "))
        bid = int(input("What's your bid? :"))
        call(name, bid)

    else:
        os.system('cls')
        ans = get_key_by_value(arr , winner_val)
        print(f'the winner is {ans}')
        exit()


