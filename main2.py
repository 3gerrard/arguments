def find_cube(n):
    return n ** 3
def check_and_execute():
    number = int(input("Enter a number: "))
    if number % 3 == 0:
        result = find_cube(number)
        print("Cube of",number,"is",result)
    else:
        print(number, "is not divisible by 3")
check_and_execute()