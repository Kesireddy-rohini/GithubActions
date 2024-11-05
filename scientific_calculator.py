import math

def sin_function(x):
    if not isinstance(x, (int, float)):
        raise ValueError("Input must be numeric.")
    return math.sin(math.radians(x))

def cos_function(x):
    if not isinstance(x, (int, float)):
        raise ValueError("Input must be numeric.")
    return math.cos(math.radians(x))

def tan_function(x):
    if not isinstance(x, (int, float)):
        raise ValueError("Input must be numeric.")
    return math.tan(math.radians(x))

def sqrt_function(x):
    if not isinstance(x, (int, float)):
        raise ValueError("Input must be numeric.")
    if x < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return math.sqrt(x)

def log_function(x):
    if not isinstance(x, (int, float)):
        raise ValueError("Input must be numeric.")
    if x <= 0:
        raise ValueError("Logarithm only defined for positive numbers.")
    return math.log10(x)

def exp_function(x):
    if not isinstance(x, (int, float)):
        raise ValueError("Input must be numeric.")
    return math.exp(x)

def asin_function(x):
    if not isinstance(x, (int, float)):
        raise ValueError("Input must be numeric.")
    if x < -1 or x > 1:
        raise ValueError("asin is only defined for values between -1 and 1.")
    return math.degrees(math.asin(x))

def acos_function(x):
    if not isinstance(x, (int, float)):
        raise ValueError("Input must be numeric.")
    if x < -1 or x > 1:
        raise ValueError("acos is only defined for values between -1 and 1.")
    return math.degrees(math.acos(x))

def atan_function(x):
    if not isinstance(x, (int, float)):
        raise ValueError("Input must be numeric.")
    return math.degrees(math.atan(x))

def sinh_function(x):
    if not isinstance(x, (int, float)):
        raise ValueError("Input must be numeric.")
    return math.sinh(x)

def cosh_function(x):
    if not isinstance(x, (int, float)):
        raise ValueError("Input must be numeric.")
    return math.cosh(x)

def tanh_function(x):
    if not isinstance(x, (int, float)):
        raise ValueError("Input must be numeric.")
    return math.tanh(x)
