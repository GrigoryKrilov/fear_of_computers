import random
numbers_orders = random.randint(1,99)
print(numbers_orders)

def sale (a):
    if a > 2:
            a = a - 1
            a_float = float(a)
            total_cost = a_float * 2.95 + 10.95
            return total_cost
    else:
            a_float_2 = float(numbers_orders)
            total_cost_2 = a_float_2 * 10.95
            return total_cost_2 


print(sale(numbers_orders))
