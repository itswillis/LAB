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

code1 = SecretCode("32")
print(code1.get_code())
code2 = SecretCode()
print(code2.get_code())

code1 = SecretCode("95")
print(code1.get_code())
code2 = SecretCode("97")
print(code2.get_code())