
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



total = 2

while True:
    print ("")
    print ("")
    question_1 = input("Would you like to log into your account or sign up and create a new profile? Press L for log in or S to sign up:")
    
    
    if question_1 == "S": 
        user = input("Please enter a username that you would like to use: ")
        pw_hash = hash(input("Please enter your password: "))
        users[user] = pw_hash
    elif question_1 == "L":
        question_2 = input ("Please enter your username: ")
        if question_2 in users:
            question_3 = input ("Please enter your password: ")
            if hash(question_3) == pw_hash:
                print ("")
                print ("Welcome back user " , question_2)
            elif hash(question_3) != pw_hash:
                while total > 0:
                    print ("")
                    print("That is the incorrect password, please try again.")
                    print("")
                    question_3 = input ("Please enter your password: ")
                    if hash(question_3) == pw_hash:
                        print ("")
                        print ("Welcome back user " , question_2)
                        total = 2
                        break
                    elif hash(question_3) != pw_hash:
                        total -= 1
                        continue
                if total == 0:
                    print ("You have entered the wrong password too many times please sign up instead. ")
                    user = input("Please enter a username that you would like to use: ")
                    pw_hash = hash(input("please enter your password: "))
                    users[user] = pw_hash
                    total = 2
        elif question_2 != user:
                print ("there is no username that matches that, please sign up.")
                user = input("Please enter a username that you would like to use: ").capitalize()
                pw_hash = hash(input("please enter your password: "))
                users[user] = pw_hash