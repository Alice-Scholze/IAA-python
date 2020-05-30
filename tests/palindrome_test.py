from exercises.palindrome import palindrome_recongnize

def test_palindrome_recongnize():
  assert palindrome_recongnize('Ana') == True
  assert palindrome_recongnize('oiieeiio') == True
  assert palindrome_recongnize('1221') == True