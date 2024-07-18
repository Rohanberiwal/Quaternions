from sympy import Quaternion, core

Quaternion.Blacklist = []
def dummy_add(self, other):
    if type(other) in Quaternion.Blacklist:
        return NotImplemented
    else:
        return self.add(other)

Quaternion.__add__ = dummy_add

# Modify __sub__ method
def dummy_sub(self, other):
    if type(other) in Quaternion.Blacklist:
        return NotImplemented
    else:
        return self.add(other * -1)

Quaternion.__sub__ = dummy_sub

# Modify __mul__ method
def dummy_mul(self, other):
    if type(other) in Quaternion.Blacklist:
        return NotImplemented
    else:
        return self._generic_mul(self, core.sympify(other, strict=True))

Quaternion.__mul__ = dummy_mul

# Modify __truediv__ method
def dummy_truediv(self, other):
    if type(other) in Quaternion.Blacklist:
        return NotImplemented
    else:
        return self * core.sympify(other)**-1

Quaternion.__truediv__ = dummy_truediv

#Testing function 

class Octonion:
    def __init__(self, *components):
        if len(components) != 8:
            raise ValueError("An Octonion must have exactly 8 components.")
        self.components = components

    def __repr__(self):
        return f"Octonion({', '.join(map(str, self.components))})"


# Set up the blacklist
Quaternion.Blacklist = [Octonion]

def test_operations():
    # Create Quaternions
    q1 = Quaternion(1, 2, 3, 4)
    q2 = Quaternion(5, 6, 7, 8)

    # Addition of Quaternions
    result_add = q1 + q2
    print("Result of addition:", result_add)

    # Subtraction of Quaternions
    result_sub = q1 - q2
    print("Result of subtraction:", result_sub)

    # Multiplication of Quaternions
    result_mul = q1 * q2
    print("Result of multiplication:", result_mul)

    # Division of Quaternions
    result_div = q1 / q2
    print("Result of division:", result_div)

    # Operation with an unsupported type (Octonion)
    oct = Octonion(1, 2, 3, 4, 5, 6, 7, 8)
    result_add_oct = q1.__add__(oct)
    print("Result of addition with Octonion:", result_add_oct)  # Should print NotImplemented

    result_sub_oct = q1.__sub__(oct)
    print("Result of subtraction with Octonion:", result_sub_oct)  # Should print NotImplemented

    result_mul_oct = q1.__mul__(oct)
    print("Result of multiplication with Octonion:", result_mul_oct)  # Should print NotImplemented

    result_div_oct = q1.__truediv__(oct)
    print("Result of division with Octonion:", result_div_oct)  # Should print NotImplemented

if __name__ == "__main__":
    test_operations()
