def index_search(list_value, value):
    left = 0
    right = len(list_value) - 1
    while left <= right:
        mid = (left + right) // 2
        if list_value[left] == value:
            return left
        if list_value[mid] == value:
            return mid
        if list_value[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return left


def main():
    with open("input.txt", "r") as file_in:
        list_value = [int(x) for x in file_in.readline().split()]
        value = int(file_in.readline())
        result = index_search(list_value, value)
    with open("output.txt", "w") as file_out:
        file_out.write(str(result))


if __name__ == '__main__':
    main()

# list_value = [5, 5, 5, 5]
# value = 5
# if __name__ == '__main__':
#     print(index_search(list_value, value))
