"""Building calculator using dict with lambda expression"""

calculator = {"+" : (lambda x, y : x + y),
"-" : (lambda x, y : x - y),
"*" : (lambda x, y : x * y),
"/" : (lambda x, y : x / y)}

calculator["/"](6,2)
