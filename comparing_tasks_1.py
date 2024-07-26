# import time

def new_array(current_array):
    sort_current_array = sorted(current_array)
    list_new = []
    s = 0
    for i in range(len(current_array)):
        index_current = sort_current_array.index(current_array[i])
        s = len(current_array[:index_current])
        list_new.append(s)
    
    return list_new


def main():
    with open("input.txt", "r") as file_in:
        current_array = [int(x)for x in file_in.readline().split()]
    result = new_array(current_array)
    with open("output.txt", "w") as file_out:
        file_out.write(' '.join(str(x) for x in result))

if __name__ == '__main__':
    main()
    # # current_array = [int(x) for x in input().split()]
    # start = time.time()
    # current_array = [6, 5, 4, 8]
    # print(*new_array(current_array))
    # finish = time.time()
    # res = finish - start
    # res_msec = res * 1000
    # print('Время работы в миллисекундах: ', res_msec)