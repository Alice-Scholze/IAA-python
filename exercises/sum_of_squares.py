# 3. Write a function that receives a number list and return the ones sum of square

def sum_of_square(number_list):
  list_to_exponential = map(lambda x: x * x, number_list)
  
  return sum(list_to_exponential)