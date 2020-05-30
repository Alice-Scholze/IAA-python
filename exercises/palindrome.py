# 2. Write a function that recognize palindromes

def palindrome_recongnize(word):
  word = word.lower()
  contrary = word[::-1]

  return word == contrary