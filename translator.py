
oneToNineteen = {
    0: "", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten",
    11: "eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen"
}

tens=["", "ten", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]
scales=["", "thousand", "million", "billion"]

def translate(number):
    if number == 0:
        return "zero"

    return translateHelper(number, 1)

def translateHelper(number, scaling):
    scale = 1000
    multiply = int(number / scale)
    residual = number % scale

    result = ""
    if multiply > 0:
        result += translateHelper(multiply, scaling+1) + " "
    hundreds = int(residual / 100)
    belowHundred = residual % 100
    if hundreds > 0:
        result += oneToNineteen[hundreds] + " hundred "
    if belowHundred > 0:
        if belowHundred < 20:
            result += oneToNineteen[belowHundred]
        else:
            tensV = int(belowHundred / 10)
            onesV = belowHundred % 10
            result += tens[tensV] + " "
            if onesV > 0:
                result += oneToNineteen[onesV]

    if len(result) > 0:
        result += " " + scales[scaling-1]

    return result

print(translate(1234567))
print(translate(0))
print(translate(19))
print(translate(123))
print(translate(61))
print(translate(3456))
print(translate(234567))
print(translate(20031204780))

