import math

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        # Note: Step 'g' में हम यहाँ Zero Division Fix ऐड करेंगे
        return a / b

    # हमने यहाँ से '#' हटा दिया है और सही से Space (Indentation) दिया है
    def square_root(self, x):
        return math.sqrt(x)

if __name__ == "__main__":
    calculator = Calculator()
    num1 = 16
    num2 = 4
    
    print(f"{num1} + {num2} = {calculator.add(num1, num2)}")
    print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}")
    print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")
    print(f"{num1} / {num2} = {calculator.divide(num1, num2)}")

    # यहाँ भी '#' हटा दिया गया है ताकि Square Root टेस्ट हो सके
    num3 = 25
    print(f"The square root of {num3} = {calculator.square_root(num3)}")