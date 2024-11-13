class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        if b >= 0:
            for i in range(b):
                result = self.add(result, a)
            return result
        else:
            for i in range(abs(b)):
                result = self.add(result, a)
            return -result

    def divide(self, a, b):
        result = 0
        if a >= 0: 
            if b > 0: #(a,b)
                while a >= b:
                    a = self.subtract(a, b)
                    result += 1
                return result
            elif b == 0: #(a,0)
                print("Error")
            else: #(a,-b)
                while a >= b:
                    b = abs(b)
                    a = self.subtract(a, b)
                    result += 1
                return -result
        elif (a < 0): 
            if b > 0: #(-a,b)
                a = abs(a)
                while a >= b:
                    a = self.subtract(a, b)
                    result += 1
            elif b == 0: #(-a,0)
                print("Error")
            else: #(-a,-b)
                a = abs(a)
                b = abs(b)
                while a >= b:
                    a = self.subtract(a, b)
                    result += 1
                return result
    
    def modulo(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Modulo by zero is undefined")
        abs_a = a
        if abs_a < 0:
            abs_a = -abs_a
        abs_b = b
        if abs_b < 0:
            abs_b = -abs_b
    # Perform modulo through subtraction
        result = abs_a
        while result >= abs_b:
            result = result - abs_b
    # Handle the case when both a and b are negative
        if a < 0 and b < 0:
            return -result
    # Handle the case when only a is negative
        if a < 0 and b > 0:
            if result != 0:
                return b - result
            return 0
        
    # Handle the case when only b is negative
        if a > 0 and b < 0:
            if result != 0:
                return b + result
            return 0
        
    # Both positive case
        return result



        

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))