# კალკულატორი
# კალკულატორის ფუნქცია მომხმარებლებს საშუალებას აძლევს შეასრულონ ძირითადი
# არითმეტიკული მოქმედებები (+, -, *, /). მომხმარებლებს შეუძლიათ შეიყვანონ ორი რიცხვი და
# შემდეგ აირჩიონ ოპერაცია შედეგის მისაღებად. კალკულატორი ასევე შეიცავს შეყვანის
# ვალიდაციას არასწორი შეყვანების დასამუშავებლად.

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    return x / y

def calculator():
    print("Welcome to the Calculator App!")
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operation = input("Choose an operation (+, -, *, /): ")

            if operation == '+':
                print("Result of addition:", add(num1, num2))
            elif operation == '-':
                print("Result of substraction:", subtract(num1, num2))
            elif operation == '*':
                print("Result of multiplication:", multiply(num1, num2))
            elif operation == '/':
                print("Result of division:", divide(num1, num2))
            else:
                print("Invalid operation. Please choose from '+', '-', '*', or '/'.")
            
            break 
        except ValueError:
            print("Invalid input! Please enter numeric values.")
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    calculator()