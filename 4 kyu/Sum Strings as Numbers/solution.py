def sum_strings(x, y):
    if len(x) > len(y):y = y.rjust(len(x), "0")
    elif len(y) > len(x): x = x.rjust(len(y), "0")

    value = 0
    carry = 0
    result = ""

    for a, b in reversed(list(zip(x, y))):
        value = carry + int(a) + int(b)
        carry, value = divmod(value, 10)
        result += str(value)

    result += str(carry)
    answer = result[::-1].lstrip("0")
    
    if answer == "": return "0"
    else: return answer