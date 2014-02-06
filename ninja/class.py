import csv

with open('ClassEmails.csv', 'rb') as csvfile:
  read = csv.reader(csvfile)

  for row in read:
    print len(row)
