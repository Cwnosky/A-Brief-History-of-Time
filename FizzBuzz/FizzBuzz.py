'''
FizzBuzz
FizzBuzz is a game that has gained in popularity as a programming assignment
to weed out non-programmers during job interviews. The object of the 
assignment is less about solving it correctly according to the below
rules and more about showing the programmer understands basic, necessary
tools such as if-/else-statements and loops.


The rules of FizzBuzz are as follows:

For numbers 1 through 100,

if the number is divisible by 3 print Fizz;
if the number is divisible by 5 print Buzz;
if the number is divisible by 3 and 5 (15) print FizzBuzz;
else, print the number.
'''


def main():
    fizzbuzz2()
    
    
def fizzbuzz():    
    for num in range(1,101):
        try:
            if num % 5 == 0 and num % 3 == 0:
                print(str(num) +' , '+ 'FizzBuzz')
            elif num % 3 == 0:
                print(str(num) +' , '+ 'Fizz')
            elif num % 5 == 0:
                print(str(num) +' , '+ 'Buzz')
            
            if num % 5 != 0 and num % 3 != 0:
                print(num)
               
        except ValueError:
            print('Something went wrong')


def fizzbuzz2():
    num = 0
    while num < 30:
        try:
            if num % 5 == 0 and num % 3 == 0:
                print(str(num) + ' , ' + 'FizzBuzz')
                num += 1
            elif num % 3 == 0:
                print(str(num) + ' , ' + 'Fizz')
                num +=1
            elif num % 5 == 0:
                print(str(num) + ' , ' + 'Buzz')
                num += 1

            if num % 5 != 0 and num % 3 != 0:
                print(num)
                num += 1

        except ValueError:
            print('Something went wrong')


if __name__ == '__main__':
    main()
