from main import *

if __name__ == '__main__':
  print "Running test main script"

  student_dict = {
    'github':'abekim',
    'last': 'Kim',
    'first': 'Abe',
    'email': 'abekim0607@gmail.com'
  }

  s = Student(**student_dict)

  # clone([s], syspath="../test/", url="git@github.com:%s/softdes.git")

  pull(syspath="../test/")