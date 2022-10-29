from big_num import aux_operations
from big_num import numbers

print(aux_operations.add_zeros_right('1112', 3))
a = numbers.Numbers("123", "12")
b = numbers.Numbers("123", "12", False)

print(a.__eq__(b))
print(type(b) is numbers.Numbers)
