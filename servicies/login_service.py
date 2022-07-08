
print("login_service working")

def validate(username, password):
    try:
        with open("credentials.txt", "r") as credentials:
            for line in credentials:
                line = line.split(",")
                if line[1] == username and line[3] == password:
                    return True
            return False
    except FileNotFoundError:
        print("You need to Register first or amend Line 71 to     if True:")
        return False