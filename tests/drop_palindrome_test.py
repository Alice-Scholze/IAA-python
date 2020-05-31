from exercises.drop_palindrome import drop_palindrome

def test_drop_palindrome():
  assert drop_palindrome(['Ana', 'Kitana', 'ovo', 'Linda', '<3']) == ['Kitana', 'Linda', '<3']