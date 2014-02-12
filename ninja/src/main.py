import csv
import getpass
import os
from models import *
from gitpy import *

def get_from_csv (path='data', filename='students.csv'):
  students = {}

  with open(os.path.join(path, filename), 'rb') as csvfile:
    reader = csv.reader(csvfile)

    header = reader.next()

    for row in reader:
      students[row[0]] = dict(zip(index, row))

if __name__ == '__main__':
  with open('mystudents.csv', 'rb') as csvfile:
    read = csv.reader(csvfile)

    for row in read:
      uid = row[0]
      name = row[1]
      email = row[2]

      if not(len(uid)):
        print "User ID empty! ID:",name
      else:
        students[uid] = {"name": name, "email": email, "user": uid}


  import json

  with open('mystudents.json', 'wb') as f:
    json.dump(students, f)


  # from names import family

  # matches = []
  # nonMatches = []

  # matchCount = 0
  # nonMatchCount = 0

  # for n in family:
  #   uid = n.split()[-1]
  #   if uid in users:
  #     matches.append(uid)
  #     matchCount += 1
  #     users.remove(uid)
  #   else:
  #     nonMatches.append(uid)
  #     nonMatchCount += 1

  # print "Number matched: ", matchCount
  # print "Number unmatched: ", nonMatchCount
  # print "nonMatches: ", nonMatches
  # print "students who haven't forked: ", users

  with open('mystudents.json', 'rb') as f:
    students = json.load(f)

  clone_repos([key for key in students.keys()])
