#Write your code below this row 👇

# if the number between divide by 3 and 5 then it is fizzbuzz 
#if the number is divided by 3 then it is fizz
# if the number is divided by 5 only then it is buzz 

for i in range(1,101):
    if i % 3==0 and i%5==0:
        print("FizzBuzz")
    elif i % 5==0:
        print("Buzz")
    elif i%3 == 0:
        print("Fizz")        
    else:
        print(i)    