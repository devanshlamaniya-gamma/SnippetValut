# l = [x for x in range(10)]
# print(l)

# a = [1,2] 
# b = [3,4]

# nl = [n for n in a for y in a]
# print(nl)

# s = {x for x in range(10)}
# print(s)

# d = {x:x for x in range(10)}
# print(d)

# ge = (x for x in range(10))
# print(list(ge))

# aa = [1,2,3,4,5]

# ab = [n for n in aa]
# print("ab",ab)

# matrix = [[1,2,3] , [4,5,6],[7,8,9]]

# flatten = [num for i in matrix for num in i]
# print(flatten)

# tu = (1,2,3,4,5,6)

# first , *all = tu

# print(first)
# print(all)

# tuu = set()
# print(type(tuu))


# class decorator:

#     def __init__(self,func):
#         self.func = func

#     def __call__(self , *args , **kwargs):
#         print("starting")

#         result = self.func(*args , **kwargs)

#         print("ending")

#         return result
    
# @decorator
# def say_hello(name):
#     print(f"hello {name}")

# say_hello("devansh")

# from functools import wraps

# def deco(func):
#     @wraps(func)
#     def wrapper(*args , **kwargs):
#         print("starting")

#         result = func(*args , **kwargs)

#         print("ending")
#         return result
#     return wrapper

# @deco
# def say():
#     print("helllo bhaiu")
    

# say()

# import time
# from functools import wraps


# def decorator(func):
#     @wraps(func)    
#     def wrapper(*args ,  **kwargs):

#         start = time.time()

#         func(*args , **kwargs)

#         end = time.time()

#         result = end - start

#         return result
#     return wrapper

# @decorator
# def say_hello():
#     time.sleep(3)
#     print("hello")

# print(say_hello())

import jwt
# from datetime import timedelta , datetime

# secret_key = "Devansh123"
# algorithm = "HS256"
# expiration_time = 30

# def create_jwt(data:dict):

#     data_to_encode = data

#     expire = datetime.now() + timedelta(minutes= expiration_time)

#     data_to_encode.update({"exp" : expire})

#     jwt_token = jwt.encode(data_to_encode , secret_key , algorithm)

#     return jwt_token

# print(create_jwt({
#     "name" : "devansh",
#     "mail" : "devansh@"
# }))


# def check_jwt(jwt_token : str):

#     checked = jwt.decode(jwt_token , secret_key,algorithm )

#     return checked
# print(check_jwt(
#     "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiZGV2YW5zaCIsIm1haWwiOiJkZXZhbnNoQCIsImV4cCI6MTc3MTkzODkwN30.j116_c-VyqBJRtRBNrFZV43YlwocVMblN3L0AGnCX10"
# ))



# import bcrypt

# encrypted = bcrypt.hashpw("devansh".encode("UTF-8"), salt=bcrypt.gensalt())
# print(encrypted)

# checking = bcrypt.checkpw("devansvh".encode("UTF-8") , encrypted)
# print(checking)


# coverage run -m pytest
# coverage report -m

