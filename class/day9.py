'''
Class 09 - 02/20/14

Dictionaries and Computational Linguistics
'''

def reverse_lookup(d, v):
  '''
  Takes in a dictionary and a value and returns all keys that map to v.
  '''
  try:
    return [k for k in d if d[k] == v]
  except ValueError:
    raise Exception("value not found in d")

known = {0:0, 1:1}

def fibonacci(n):
  if n in known: return known[n]

  res = fibonacci(n-2) + fibonacci(n-1)
  known[n] = res
  return res

def orig_fib(n):
  if n in [0, 1]: return n
  return orig_fib(n-2) + orig_fib(n-1)

mem_lev = {}

def levenshtein_distance(s1,s2):
  """ Computes the Levenshtein distance between two input strings """
  if len(s1) == 0:
    return len(s2)
  if len(s2) == 0:
    return len(s1)
  return min([int(s1[0] != s2[0]) + \
    levenshtein_distance(s1[1:],s2[1:]),\
    1+levenshtein_distance(s1[1:],s2),\
    1+levenshtein_distance(s1,s2[1:])])

if __name__ == '__main__':
  d = dict(zip([1, 2, 3, 4, 5], [1, 2, 2, 2, 2]))

  # print fibonacci(35)

