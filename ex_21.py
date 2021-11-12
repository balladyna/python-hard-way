def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACKING {a} - {b}")
    return a - b
    
def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b
    
def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b
    
print ("Let's do some math with just functions!")

age = add(20, 5)
height = subtract(180, 4)
weight = multiply(999, 52)
iq = divide(250, 3)

print(f"Age: {age}, height: {height}, weight: {weight}. IQ: {iq}")

print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, age))))

print("That becomes", what, "Can you do it by hand?")
