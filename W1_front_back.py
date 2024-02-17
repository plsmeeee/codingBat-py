# Given a string, return a new string where the first and last chars have been exchanged.
def front_back(str):
  front=str[:1]
  back=str[-1:]
  if len(str)<=1:
    return str
  else:  
    return back + str[1:-1] +front
