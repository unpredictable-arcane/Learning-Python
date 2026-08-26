import sys
from fractions import Fraction
from decimal import Decimal

ideal_temp = 91.56
current_temp = 99.49

print(f"Ideal temp { ideal_temp }")
print(f"Current temp { current_temp }")
print(f"Difference temp { ideal_temp - current_temp }")
print(sys.float_info)