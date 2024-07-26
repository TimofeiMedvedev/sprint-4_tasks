def dublicates(element_count, first_array):
    duble = list(dict.fromkeys(first_array))
    defer = element_count - len(duble) 
    duble += ['_']*defer
    return duble


def main():
    with open("input.txt", "r") as file_in:
        element_count = int(file_in.readline())     
        first_array = file_in.readline().split()
        result = dublicates(element_count, first_array)
    # element_count = int(input())
    # first_array = input().split() 
    with open("output.txt", "w") as file_out:
        file_out.write(' '.join(result))          

if __name__ == '__main__':
    main()