def isbn_converter(isbn: str) -> str:
    isbn = isbn[:-1]
    isbn = "978-" + isbn
    isbn_digits = isbn.replace("-","")

    check_digit = 0

    for i, digit in enumerate(isbn_digits):
        if i%2 == 0:
            check_digit += int(digit)
        elif i%2 == 1:
            check_digit += int(digit)*3

    check_digit = check_digit % 10 
    if check_digit == 0:
        isbn = isbn + "0"
    else:
        isbn = isbn + str(10 - check_digit)
    
    return isbn

isbn_converter("1-85326-158-0")