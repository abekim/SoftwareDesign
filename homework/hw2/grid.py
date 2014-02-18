'''
grid.py

@author: abekim
'''

# interesting problem we have here because all printing are done in rows :(

def draw_grid(row, col, length):
  for i in range(row):
    print col * ("+" + length * "-") + "+"
    for i in range(length):
      print col * ("|" + length * " ") + "|"
  print col * ("+" + length * "-") + "+"

def print_row(pat, first='+', col=2):
  '''
  prints a row based on its pattern, numerb of columns (in the grid), and the first (and last) character
    pat: pattern in string
    first: first and last character of the row in string
    col: number of columns in the grid
  '''
  print first,seq*col,first
  
def squares(pattern, n):
  '''
  draws an n x n square based on the pattern
    pattern: pattern with horizontal and vertical patterns in dict
    n: number of rows and columns in the grid in int
  '''
  # horizontal and vertical patterns
  horizontal = pattern['h']
  vertical = pattern['v']

  # get

  for i in range(n*len(horizontal['pat'])):
    if not i or not i % length: # when 
      print_row(pattern['h']['pat'], first=pattern['h']['first'], col=n)
