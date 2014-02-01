# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 16:29:14 2014

@author: abe
"""
'''
If I have many many cats and want to save their information, 
    one way is to use dictionaries
'''
# new dictionary
cats = {}

'''
Normally, you'd use OOP to define a cat schema (via Classes),
    but for the sake of simplicity, I'm going to assume each `Cat`
    has the following attributes:
    {
        name: str
        color: str
        age: int        
    }
    and I'm also going to represent each cat as a dictionary
'''
# new cat
cat1 = {
    'name': 'Fluffy',
    'color': 'white',
    'age': 2
}

print "cat1", cat1

cat2 = {
    'name': 'Mittens',
    'color': 'brown',
    'age': 3
}

cat3 = {
    'name': 'some cute kitten name',
    'color': 'black',
    'age': 1
}

'''
Back to `cats`. I'll give a key to each of these cats, arbitrarily the order
    in which I got these cats.

PS. This is also how you add more things to an existing dictionary
'''
cats[0] = cat1
cats[1] = cat2
cats[2] = cat3

print "cats", cats

'''
If you wanted to, you can use the hash of the cats' names as the keys:

PS. In Python, you can't hash dictionaries unless you're using a module 
    called `pickle` (docs) [http://docs.python.org/2/library/pickle.html]
'''
cats[hash(cat1['name'])] = cat1

print "keys within cats", cats.keys()

del cats[0]

print "cats", cats
print "cat1", cats[hash(cat1['name'])]

'''
Basically, I can do whatever I want with a dictionary; the basic concept behind
    dictionaries is the idea that you can map one thing to another, and be 
    able to look up whatever you mapped really quickly.

As for hash itself, think of it as a way to uniquely represent any object
    using fixed length data. (when you call: 
        `len(str(hash('a'))) = len(str(hash('b')))`
    it returns true.) We normally use hashing when
    it's difficult to work with the original data. Say I named my cat:
        'abcdef....xyz'
    It would be such a hassle to type cats['abc...xyz'] each time I wanted
    to search for my weirdly alphabetic cat
'''
