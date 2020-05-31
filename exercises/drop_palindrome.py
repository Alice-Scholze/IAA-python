# 7. Use list comprehension to drop palindromes elements of string list

def drop_palindrome(string_list):
  return [x for x in string_list if x.lower() != x.lower()[::-1]]