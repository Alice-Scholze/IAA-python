# 4. Write a recursive function that return the factorial of a number

def get_factorial(number):
  if number == 1: return number

  return number * get_factorial(number - 1)