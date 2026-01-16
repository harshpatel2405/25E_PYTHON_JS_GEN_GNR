# 1. Arithmetic
#     + - * / %


# 2. Relational
# > < >= <= == !=
# 3. Logical
# and  , or  , not
# 4. Assignment
# += , -= , *= , /= , %= , //= , **=
# 5. Bitwise
# & , | , ^ , ~ , << , >>

# 6. Membership
# in , not in
# 7. Identity
# is , not is

a = 15
b = 2
print(15 / 2)

print(a // b) # floor division
print(a % b)

print(a**b) # exponent


print(15 < 15)
print(15 > 15)
print(15 >= 15)
print(15 <= 15)
print(15 == 15)
print(15 != 15)

# 128 64 32 16 8 4 2 1   1 1 0 0 1
#              1 1 1 1
#              0 1 1 1
#              1 0 0 0
# 0   0   0  0 0 0 0 1
# 0   0   1  1 1 1 0 0
#              1 1 1 1 - 15
#              0 1 1 1 - 7

a = 15  # (1111)
b = 7
print(a & b)
print(a | b)
print(a ^ b)
print(a << 2)
print(b >> 2)


# 2 | 25
# 2 | 12 - 1
# 2 | 6 - 0
# 2 | 3 - 0
# 2 | 1 - 1
