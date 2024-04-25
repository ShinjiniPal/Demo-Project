class Utils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def mul(a, b):
        return a * b

    @staticmethod
    def div(a, b):
        if b == 0:
            return "Error: Cannot divide by zero!"
        return a / b

    @staticmethod
    def mod(a, b):
        return a % b

    @staticmethod
    def lcm(a, b):
        if a < 0 or b < 0:
            return "Invalid input"
        L = max(a, b)
        while L <= a * b:
            if L % a == 0 and L % b == 0:
                return L
            L += 1

    @staticmethod
    def hcf(a, b):
        if a <= 0 or b <= 0:
            return "Invalid input"
        H = min(a, b)
        while H >= 1:
            if a % H == 0 and b % H == 0:
                return H
            H -= 1

    @staticmethod
    def extract_from_text(text):
        numbers = []
        for t in text.split(' '):
            try:
                numbers.append(float(t))
            except ValueError:
                pass
        return numbers

    @staticmethod
    def calculate(text):
        operations_list = {
            'ADD': Utils.add,
            'ADDITION': Utils.add,
            'SUM': Utils.add,
            'PLUS': Utils.add,
            'SUB': Utils.sub,
            'DIFFERENCE': Utils.sub,
            'MINUS': Utils.sub,
            'SUBTRACT': Utils.sub,
            'MULT': Utils.mul,
            'PRODUCT': Utils.mul,
            'MULTIPLICATION': Utils.mul,
            'DIV': Utils.div,
            'DIVIDE': Utils.div,
            'MOD': Utils.mod,
            'MODULUS': Utils.mod,
            'LCM': Utils.lcm,
            'HCF': Utils.hcf
        }

        check = True
        for word in text.split(' '):
            if word.upper() in operations_list.keys():
                check = False
                try:
                    inputs = Utils.extract_from_text(text)
                    result = operations_list[word.upper()](inputs[0], inputs[1])
                    return result
                except:
                    return "Please enter inputs in correct format and try again"
        if check:
            return "Enter a valid operation."
