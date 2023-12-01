#if user says after completion if he wants to continue with the same number then continue with it only else start new4
from art import logo
print(logo)
def operations(first_no, next_no):
    global ans
    if input_operator == '+':
        ans = first_no + next_no
    elif input_operator == '-':
        ans = first_no - next_no
    elif input_operator == '/':
        ans = first_no // next_no
    elif input_operator == '*':
        ans = first_no * next_no
    else:
        print("Invalid operator")

#input from user
first_no = int(input("Enter first number: "))

#ask for operator

print("+ \n" 
      "/ \n"
      "- \n"
      "*")
input_operator = input("Pick an operator : ")
#input
next_no = int(input("What's next number ? : "))

ans = 0
operations(first_no , next_no)
print(f'Result is {ans}')

#ask user wants to continue or not

while True:
    toContinue = input(f'Type y to continue calculation wih {ans} else type n: ')


    #if yes then contiue with the ans came before else start new
    if toContinue == 'y':
        print("+ \n" 
            "/ \n"
            "- \n"
            "*")
        input_operator = input("Pick an operator : ")
        # input
        next_no = int(input("What's next number ? : "))
        operations(ans , next_no)
        print(f'Result is {ans}')
    else:
        exit()

