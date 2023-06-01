#### Mark's section ####
import pickle
from os import path

def save (object, file):
    """This serilizes the dictornary"""
    with open(file, "wb") as f:
        pickle.dump(object, f)

def load(file):
    """this loads the dictonary and returns a file, if there isn't one then it returns None"""
    if path.exists(file):
        with open(file, "rb") as f:
            return pickle.load(f)
    return None


USERS_FILE = "users.pkl"
users = load(USERS_FILE)
if users is None:
  users = {}




### Rachelle's section ###
while True:
    user = input("Enter a username, or q to quit, u to see all users: ").capitalize()








    #####Bella's Pretty Section#####