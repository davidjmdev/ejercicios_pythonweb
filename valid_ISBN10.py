def valid_ISBN10(isbn:str) -> bool:
    check_digit = 0

    for index, digit in enumerate(isbn[:-1], start=1):
        if digit.isdigit():
            check_digit += int(digit) * index
        else:
            return False

    if isbn[-1].isdigit():
        check_digit += int(isbn[-1]) * 10
    elif isbn[-1] == "X":
        check_digit += 100
    else:
        return False

    return check_digit % 11 == 0


print(valid_ISBN10("1112223339"))