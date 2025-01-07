def my_sum(*args):
    total_sum = 0
    for i_elem in args:
        if isinstance(i_elem, int):
            total_sum += i_elem
        elif isinstance(i_elem, (list, tuple)):
            for x in i_elem:
                total_sum += my_sum(x)
    return total_sum

print(my_sum([[1, 2, [3]], [1], 3]))
print(my_sum(1, 2, 3, 4, 5))