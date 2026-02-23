import bcrypt


def create_hashed_password(password):

    # password_bytes = password.encode("utf-8")

    # salt = bcrypt.gensalt()

    # hashed_pass = bcrypt.hashpw(password_bytes , salt)

    hashed_pass = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    return hashed_pass.decode("utf-8")


# print(password_hasing("devansh123"))


def check_hashed_password(entered: str, hashed_password: str):

    entered = entered.encode("utf-8")
    hashed_password = hashed_password.encode("utf-8")

    a = bcrypt.checkpw(entered, hashed_password)

    # if entered == hashed_password:
    #     return True
    # else:
    #     return False

    return a


# print(check_pass("devansh123" , "$2b$12$v8TAGRlwzXTCAoU5M6dZf.WQbhoiRWBNPToMMPF8b0JtG/8/t/DCO"))
