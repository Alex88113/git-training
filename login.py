def login(username: str, password: str):
    if username == "admin" and password == "secret":
        return True
    else:
        return False
