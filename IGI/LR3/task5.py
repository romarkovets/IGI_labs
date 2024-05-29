






def task5(list):
    sum = list.sum()
    mult = 1
    for i in range(len(list)):
        if i % 2 == 0 and list[i] % 2 == 0:
            mult *= abs(list[i])

    left = right = -1
    for i in range(len(list)):
        if list[i] != 0:
            left = i
            break

    for i in reversed(range(len(list))):
        if list[i] != 0:
            right = i
            break

    if left == -1:
        sum = 0
    elif left == right:
        sum -= list[left]
    else:
        sum -= list[right] + list[left]

    return mult, sum