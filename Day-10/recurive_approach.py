ans =0
def calling():
    global ans 
    
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
    operations(first_no , next_no, input_operator)
    

    #ask user wants to continue or not
    toContinue = input(f'Type y to continue calculation wih {ans} else type n')


    #if yes then contiue with the ans came before else start new
    if toContinue == 'y':
        calling()
    else:
        exit()

def operations(first_no, next_no , input_operator):
    if input_operator == '+':
        ans = first_no + next_no
        print(f'Result is {ans}')
    elif input_operator == '-':
        ans = first_no - next_no
        print(f'Result is {ans}')
    elif input_operator == '/':
        ans = first_no // next_no
        print(f'Result is {ans}')
    elif input_operator == '*':
        ans = first_no * next_no
        print(f'Result is {ans}')
    else:
        print("Invalid operator")

calling()
