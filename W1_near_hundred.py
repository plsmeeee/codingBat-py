# Given an int n, return True if it is within 10 of 100 or 200.
# Note: abs(num) computes the absolute value of a number.
def near_hundred(n):
  if (n>89 and n<111) or (n>189 and n<211):
    return True
  else:
    return False
