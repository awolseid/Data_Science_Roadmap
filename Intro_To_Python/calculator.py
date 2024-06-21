def summation(x, y):
  return f"The sum of {x} and {y} is {x + y}."
def difference(x, y):
  return f"The diffence of {x} and {y} is {x - y}."
def product(x, y):
  return f"The product of {x} and {y} is {x * y}."
def division(x, y):
  if y == 0:
    return f"The ratio of {x} and {y} is not possible."
  else:
    return f"The ratio of {x} and {y} is {round(x / y, 4)}."