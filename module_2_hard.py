def get_password(n):
    password = ''
    for i in range(1, n):
        for j in range(2, n):
            if j <= i:
                continue
            if n % (i + j) == 0:
                password = password + (str(i) + str(j))
    return password
for i in range(3, 21):
    result = get_password(i)
    print(f"{i} - {result}")