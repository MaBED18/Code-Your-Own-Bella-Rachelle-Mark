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

    elif question_1 == "L":
        print("L")




<<<<<<< HEAD
    #####Bella's Pretty Section#####
=======




    #####Bella's Pretty Section#####


>>>>>>> 629d8c1 (I added new code that gets the user's input for signing up and log in usernames into Rachelle's section)
