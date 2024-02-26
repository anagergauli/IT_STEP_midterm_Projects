#       კალკულატორი

# კალკულატორის ფუნქცია მომხმარებლებს საშუალებას აძლევს შეასრულონ ძირითადი არითმეტიკული მოქმედებები (+, -, *, /).
# მომხმარებლებს შეუძლიათ შეიყვანონ ორი რიცხვი დაშემდეგ აირჩიონ ოპერაცია შედეგის მისაღებად.
# კალკულატორი ასევე შეიცავს შეყვანის ვალიდაციას არასწორი შეყვანების დასამუშავებლად.



# მიმატების ოპერაცია
def add(x, y):
    return x + y
# გამოკლების ოპერაცია
def subtract(x, y):
    return x - y
# გამრავლების ოპერაცია
def multiply(x, y):
    return x * y
# გაყოფის ოპერაცია
def divide(x, y):
    # ნულზე გაყოფა არ შეიძლება
    if y == 0:
        return "Error! Division by zero! It is not allowed."
    # დამრგვალება მძიმის შემდეგ ორ ერთეულამდე
    return round(x / y, 2)

# რიცხვის შეტანა
def number_input(user_input):
    while True:
        try:
            number = float(input(user_input))
            return number
        except ValueError:
            print("Please enter only numbers.")
# სხვადასხვა ოპერაციებიდან სასურველის არჩევა
def operation_input():
    while True:
        operation = input("Choose an operation (+, -, *, /): ")
        if operation in ['+', '-', '*', '/']:
            return operation
        else:
            print("Please choose operations from '+', '-', '*', or '/'.")
# შედეგების ფორმატირება
def format_result(result):
    if result.is_integer():
        return int(result)
    else:
        return round(result, 2)

def calculator():
    print("Here is Calculator App! Let's start!")

    while True:
        try:
            num1 = number_input("Enter the first number: ")
            num2 = number_input("Enter the second number: ")
            operation = operation_input()

            if operation == '+':
                result = add(num1, num2)
                print(f"Result of addition: {format_result(result)}")
            elif operation == '-':
                result = subtract(num1, num2)
                print(f"Result of subtraction: {format_result(result)}")
            elif operation == '*':
                result = multiply(num1, num2)
                print(f"Result of multiplication: {format_result(result)}")
            elif operation == '/':
                result = divide(num1, num2)
                print(f"Result of division: {format_result(result)}")

            break 
        except Exception as e:
            print("Here is an error:", e)

if __name__ == "__main__":
    calculator()
