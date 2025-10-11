#Functions are amazing
a: int = int(input("Enter a number :"))
b: int = int(input("Enter another number :"))

def arithmetic(x:int , y:int) -> None :
    print(f'The sum of {x} and {y} is {x + y}')
    print(f'The difference of {x} and {y} is {x - y}')
    print(f'The product of {x} and {y} is {x * y}')
    print(f'The exponentation of {x} and {y} is {x ** y}')
    if x != 0 :
        print(f'The quotient of {x} and {y} is {x / y}')
    else :
        print('Sorry , Division by zero is not allowed')
        
arithmetic(a,b)

