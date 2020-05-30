from exercises.inversion import inverse_list

def test_inverse_list():
  assert inverse_list([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
  assert inverse_list([1, 1, 2, 3, 5, 7]) == [7, 5, 3, 2, 1, 1]