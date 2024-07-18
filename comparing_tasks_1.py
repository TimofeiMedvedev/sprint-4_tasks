import time

def new_array(current_array):
    sort_current_array = sorted(current_array)
    list_new = []
    s = 0
    for i in range(len(current_array)):
        index_current = sort_current_array.index(current_array[i])
        s = len(current_array[:index_current])
        list_new.append(s)
    return list_new


 

if __name__ == '__main__':
    # current_array = [int(x) for x in input().split()]
    start = time.time()
    current_array = [6, 5, 4, 8]
    print(*new_array(current_array))
    finish = time.time()
    res = finish - start
    res_msec = res * 1000
    print('Время работы в миллисекундах: ', res_msec)