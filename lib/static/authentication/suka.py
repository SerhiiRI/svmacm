#!/usr/bin/python3
from functools import reduce




a = dict()
a["12"] = "a"
a["!a"] = "a"
a["!b"] = "a"
a["!c"] = "a"

b = dict()
b["12"] = "d"
b["!a"] = ''
b["!b"] = "b"
b["!c"] = "d"


print("Validation is {}".format(validation(a, b)))
