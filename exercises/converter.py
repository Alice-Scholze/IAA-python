# 1. Write function to convert hour, minutes and seconds to total seconds:

MINUTE = 60

def total_seconds(hours, minutes, seconds):
  return hours_to_second(hours) + minutes_to_seconds(minutes) + seconds

def minutes_to_seconds(minutes):
  return minutes * MINUTE

def hours_to_second(hours):
  return minutes_to_seconds(hours * MINUTE)
