from exercises.square import square_list

def test_square_list():
  assert square_list([2, 4, 6]) == [4, 16, 36]
  assert square_list([3, 6, 9]) == [9, 36, 81]