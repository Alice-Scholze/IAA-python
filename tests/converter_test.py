from exercises.converter import total_seconds, minutes_to_seconds, hours_to_second

MINUTE = 60
HOUR = 3600

def test_total_seconds():
  assert total_seconds(0, 0, 1) == 1
  assert total_seconds(0, 1, 0) == MINUTE
  assert total_seconds(1, 0, 0) == HOUR

def test_minutes_to_seconds():
  assert minutes_to_seconds(1) == MINUTE
  assert minutes_to_seconds(2) == MINUTE * 2

def test_hours_to_second():
  assert hours_to_second(1) == HOUR
  assert hours_to_second(2) == HOUR * 2