'''
compare.py

@author: abekim
'''

# Problem 6.1 - compare x, y
def compare(x, y):
  '''
  compares x and y and returns:
    1 if x > y,
    0 if x == y,
    -1 if x < y
  '''
  if x > y: return 1
  elif x == y: return 0
  else: return -1