def mountains(mountain):
    top_mountain = max(mountain)
    index_top = mountain.index(top_mountain)
    length = len(mountain)

    if index_top == 0 or index_top == length - 1:
        return False
 
    for index in range(1, index_top):
        if mountain[index] <= mountain[index-1]:
            return False
    
    for i in range(index_top+1, length):
        if mountain[i] >= mountain[i-1]:
            return False
    return True
    
def main():
    with open("input.txt", "r") as file_in:
        mountain = [int(x) for x in file_in.readline().split()] 
        result = mountains(mountain)
    with open("output.txt", "w") as file_out:
        file_out.write(str(result))


if __name__ == '__main__':
    main()
