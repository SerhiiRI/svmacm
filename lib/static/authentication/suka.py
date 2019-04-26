#!/usr/bin/python3
from functools import reduce

def validation(request_template: dict, comparing_template: dict):
    def compare (acc, key):
        print("Acum: {}, Key: {} | {} in template {} | equal Types {}".format(
            acc, key, key, (key in comparing_template), type(request_template[key]) is type(comparing_template[key])
        ))
        return acc\
               and ((key in comparing_template)
                    and (type(request_template[key]) is type(comparing_template[key])))
    return reduce(compare, request_template.keys())


a = dict()
a["12"] = "a"
a["!a"] = "a"
a["!b"] = "a"
a["!c"] = "a"

b = dict()
b["12"] = ","
b["!a"] = "b"
b["!b"] = "b"
b["!c"] = []


print("Validation is {}".format(validation(a, b)))
