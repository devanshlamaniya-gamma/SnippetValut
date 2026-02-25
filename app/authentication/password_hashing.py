import bcrypt


def create_hashed_password(password):

    if password is None:

        raise ValueError("Password cannot be None")

    # password_bytes = password.encode("utf-8")

    # salt = bcrypt.gensalt()

    # hashed_pass = bcrypt.hashpw(password_bytes , salt)

    hashed_pass = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    return hashed_pass.decode("utf-8")


# print(create_hashed_password(str("devansh123")))


def check_hashed_password(entered: str, hashed_password: str):

    entered = entered.encode("utf-8")
    hashed_password = hashed_password.encode("utf-8")

    a = bcrypt.checkpw(entered, hashed_password)

    # if entered == hashed_password:
    #     return True
    # else:
    #     return False

    return a


print(
    check_hashed_password(
        "Xyz@1234", "$2b$12$0DsUsktJQxNIja0Uj1Wf0eslxhe1iZSF8sMLM0Wpj3V8i5bXFT2ei"
    )
)
# $2b$12$egsrvT7yYr8m7Mrze7GmzObWL8VXeVpuc6z5LR6BsBKOfSrUPCifq
# Ritul@123
