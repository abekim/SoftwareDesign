from git import Repo
import os, shutil
from models import *

def test_urls (users, url="https://github.com/%s/SoftwareDesign"):
  """
  Test whether or not the urls are valid
  """
  import urllib2

  failed = [] # keep track of failed user ids
  
  for uid in users:
    try:
      urllib2.urlopen(url % uid)
    except:
      failed.append(uid)
      print uid + " has failed to load"
  
  print "Loaded %i of %i successfully" % (len(users) - len(failed), len(users))
  print "Failed user ids: %s" % failed

def clone_repos(students, syspath="../repos/", url="git@github.com:%s/SoftwareDesign.git"):
  """
  Recursively removes previous copies of the repo (requires user confirmation)
  Clones the repos from the urls to a folder called repos/<username>

    students : list of student objects
    syspath : system path to copy repos to
  """
  if (raw_input("Remove current repositories? (y/n) ")) != "y":
    raise Exception("Failed to confirm. Failed to clone repos")
  
  # if other repos exist, remove them
  if os.path.exists(syspath):
    shutil.rmtree(syspath) # remove existing repos
    print "Successfully removed repos from \"%s\"" % syspath

  for s in students:
    path = syspath + s.user
    
    print "Cloning Repo: %s to %s" % (s.name, path)

    if not os.path.exists(path):
      os.makedirs(path)
    
    Repo.clone_from(url % s.user, path)

  print "Successfully cloned repos"

def pull_repos(syspath="../repos/"):
  """
  Pulls from remote for all directories under syspath
  """
  for fold in os.listdir(syspath):
    print "Pulling Repo for ", fold
    repo = Repo(os.path.join(syspath,fold))

    o = repo.remotes.origin
    print o.refs
    o.pull()

