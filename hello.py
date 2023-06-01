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
    print ("")
    print ("")
    question_1 = input("Would you like to log into your account or sign up and create a new profile? Press L for log in or S to sign up:")
    
    
    if question_1 == "S": 
        user = input("Please enter a username that you would like to use.").capitalize()
        pw_hash = hash(input("please enter your password: "))
        users[user] = pw_hash
    elif question_1 == "L":
        print("L")



