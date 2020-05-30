# 5. Write a recursive function to inverse list

def inverse_list(list):
  if len(list) == 1: return list[-1:]

  return list[-1:] + inverse_list(list[:-1])
