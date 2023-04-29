def validate(code):
    if type(code) is not str or len(code) != 4 or not code.isdigit():
        raise ValueError(f"ERROR: '{code}' - Invalid Format!")
    
    d1, d2, d3, check_digit = map(int, code)
    total = d1 * 0 + d2 * 1 + d3 * 2
    if check_digit != total % 9:
        raise ValueError("ERROR: Invalid check digit!")
    
    return code

print(validate('1238'))
print(validate('5672'))
print(validate('4595'))
try:
    print(validate('1234'))
except ValueError as e:
    print(e)
else:
    print("Well done!")

try:
    print(validate('11111111111'))
except ValueError as e:
    print(e)
else:
    print("Well done!")