class utils:
    def add(a, b):
        return a + b

    def sub(a, b):
        return a - b

    def mul(a, b):
        return a * b

    def div(a, b):
        return a / b

    def mod(a, b):
        return a % b

    def lcm(a, b):
        if a < 0 or b < 0: return
        L = a if a > b else b
        while L <= a * b:
            if L % a == 0 and L % b == 0:
                return L
            L += 1

    def hcf(a, b):
        if a < 0 or b < 0: return
        H = a if a < b else b
        while H >= 1:
            if a % H == 0 and b % H == 0:
                return H
            H -= 1

    def extract_from_text(text):
        l = []
        for t in text.split(' '):
            try:
                l.append(float(t))
            except ValueError:
                pass
        return l

    def calculate(x):
        text = x
        check = True
        for word in text.split(' '):
            if word.upper() in operations_list.keys():
                check = False
                try:
                    l = utils.extract_from_text(text)
                    r = operations_list[word.upper()](l[0], l[1])
                    return r
                except:
                    return "Please enter inputs in correct format and try again"
        if (check):
            return "Enter valid input operation."


operations_list = {'ADD': utils.add, 'ADDITION': utils.add, 'SUM': utils.add, 'PLUS': utils.add,
                   'SUB': utils.sub, 'DIFFERENCE': utils.sub, 'MINUS': utils.sub, 'SUBTRACT': utils.sub,
                   'DIFF': utils.sub,
                   'LCM': utils.lcm, 'HCF': utils.hcf, 'PRODUCT': utils.mul, 'MULTIPLICATION': utils.mul,
                   'MULTIPLY': utils.mul, 'DIVISION': utils.div, 'DIV': utils.div, 'DIVIDE': utils.div,
                   'MOD': utils.mod, 'REMAINDER': utils.mod, 'MODULUS': utils.mod}


def main():
    x = input("Enter the operation:")
    if (utils.calculate(x)):
        return print(utils.calculate(x))


main()
