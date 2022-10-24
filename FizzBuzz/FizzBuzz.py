def main():
    fizzbuzz()
    
    
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


if __name__ == '__main__':
    main()
