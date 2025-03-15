import sys

def addition(num1, num2):
    sum = num1 + num2
    return sum

def subtraction(num1, num2):
    sub = num1 + num2
    return sub

def multiplication(num1, num2):
    mul = num1 * num2
    return mul


num1 = sys.argv[1]
operation = sys.argv[2]
num2 = sys.argv[3]

if operation == 'addition':
  output = addition(int(num1), int(num2))
  print(output)

elif operation == 'subtraction':
  output = subtraction(int(num1), int(num2))
  print(output)

elif operation == 'multiplication':
  output = multiplication(int(num1), int(num2))
  print(output)

else:
  print("Invalid operation")
  sys.exit(1)