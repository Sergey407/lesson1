def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()
print_params(5)
print_params(3, 8, 'zero')
print_params(b = 25, c = [1,2,3])

values_lis = [7, 'pen', (1, 2)]
values_dict = {'a': 1, 'b': 'строка', 'c': True}

print_params(*values_lis)
print_params(**values_dict)

values_list_2 = [13,'gold']

print_params(*values_list_2, 42)