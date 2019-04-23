#!/usr/bin/python3
import json


def addUser(userList:list):
    userList = [dict({"login":log, "password":passwd}) for log, passwd in userList]
    print(userList)
    # with open("users.file", "w+") as authfile:
    #     authfile.write(encode(key, (JSONUserTemplate("admin", "lala"))))

# print("LOGIN:{}".format(str(verifiedUser(key, "admin", "lala"))))
addUser((("a", "p"), ("d", "b"), ("k", "n")))

