def AND(a, b):
    return a and b


def OR(a, b):
    return a or b


def NOT(a):
    return not a


def XOR(a, b):
    return a != b


def half_adder(a, b):
    sum_bit = XOR(a, b)
    carry_bit = AND(a, b)
    return sum_bit, carry_bit


def full_adder(a, b, c):
    sum1, carry1 = half_adder(a, b)
    sum2, carry2 = half_adder(sum1, c)
    carry_out = OR(carry1, carry2)
    return sum2, carry_out


print(AND(1, 0))
print(OR(1, 0))
print(XOR(1, 0))
print(NOT(1))
print(half_adder(1, 1))
print(full_adder(1, 1, 1))
