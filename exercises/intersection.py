# 8. Use list comprehension to create a list with only elements commom to lists A and B

def get_intersection_of(list_a, list_b):
  return [x for x in set(list_a + list_b) if x in list_a and x in list_b]