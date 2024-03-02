import sys
from app import App
from calculator.calculate import Calculate

number_cruncher = Calculate()

def is_number(num1,num2):
    try:
        float(num1)
        float(num2)
        return True
    except ValueError:
        return False
    
def calculate_and_print(a, operation, b):
    if is_number(a,b) == True:
        if operation == "+":
            print(a + " " + operation + " " + b + " = " + str(number_cruncher.add(float(a), float(b))))
        elif operation == "-":
            print(a + " " + operation + " " + b + " = " + str(number_cruncher.subtract(float(a), float(b))))
        elif operation == "*":
            print(a + " " + operation + " " + b + " = " + str(number_cruncher.multiply(float(a), float(b))))
        elif operation == "/":
            print(a + " " + operation + " " + b + " = " + str(number_cruncher.divide(float(a), float(b))))
        else:
            print("Unknown operation: " + operation)
    else:
        print("Invalid number input: " + a + " or " + b)

def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <number1> <operation> <number2> ")
        sys.exit(1)
    
    _, a, operation, b = sys.argv
    calculate_and_print(a, operation, b)

if __name__ == '__main__':
    app = App().start()   # old method in this file is 'main()'
