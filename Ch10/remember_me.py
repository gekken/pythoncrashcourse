import json


def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    filename = 'username.json'
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """
    Load the username, if it has been previously stored.
    Otherwise, prompt for the username and store it.
    """
    username = get_stored_username()
    if username:
        print("Welcome back, {}!".format(username))
    else:
        username = get_new_username()
        print("We'll remember you when you come back, {}!".format(username))


greet_user()
