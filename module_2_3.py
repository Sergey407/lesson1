my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
namber = 0
while namber <= len(my_list):
    if my_list[namber] > 0:
        print(my_list[namber])
        namber = namber + 1
        continue
    elif my_list[namber] == 0:
        namber = namber + 1
        continue
    else:
        break

