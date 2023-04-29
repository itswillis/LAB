''' 
check digit = (d1 * 1 + d2 * 2 ) % 9
d1 is the first digit
d2 is the second digit
'''

class SecretCode:
    def __init__(self, code = 12):
        self.code = code
        
    def get_code(self):
        return self.code

    def get_check_digit(self):
        code_str = str(self.code)
        check_digit = int(code_str[0] * 1 + code_str[1] * 2 ) % 9
        return check_digit
    
    def __str__(self):
        return "{}{}".format(self.code, self.get_check_digit())

code1 = SecretCode("34")
print(code1.get_check_digit())
print(code1)
code2 = SecretCode()
print(code2)
code3 = SecretCode("45")
print(code3)