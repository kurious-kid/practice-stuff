
T = [1,2,3,4]
size_of_T = len(T)
total_wait_time = 0

while (size_of_T != 0):

    for i in range(0, len(T) - 1):
        if (size_of_T == 0):
            break
        if (T[i] == 0):
            continue
        if (T[i] == 1):
            total_wait_time = total_wait_time + size_of_T
            size_of_T = size_of_T - 1
            T[i] = T[i] - 1
        else:
            total_wait_time = total_wait_time + size_of_T
            T[i] = T[i] - 1


print(total_wait_time % (10 ** 9))
