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
    

mountain = [int(x) for x in input().split()]
# mountain = [0, 3, 2, 1]
# mountain = [3, 5, 5]
# mountain = [2, 1, 3, 5, 8]
# mountain = [10, 20, 30, 40, 30, 20, 10]
# mountain = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

if __name__ == '__main__':
    print(mountains(mountain))
