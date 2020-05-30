from exercises.factorial import get_factorial

def test_get_factorial():
  assert get_factorial(3) == 6
  assert get_factorial(6) == 720
  assert get_factorial(9) == 362880