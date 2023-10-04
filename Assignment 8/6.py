# Write a Python class to implement pow(x, n) 

class PowerCalculator:
    def my_pow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        result = 1
        while n:
            if n % 2:
                result *= x
            x *= x
            n //= 2
        return result

# Usage
calculator = PowerCalculator()
print(calculator.my_pow(2, 3))  
