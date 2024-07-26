def find_substring(seq):
    sub = ''
    max_sub = 0
    for liter in seq:
        if liter not in sub:
            sub += liter
            max_sub = max(max_sub, len(sub))
        else:
            index_liter = sub.index(liter)
            sub = sub[index_liter+1:] + liter
    return max_sub


def main():
    with open("input.txt", "r") as file_in:
        seq = file_in.readline().rstrip()
    result = find_substring(seq)
    with open("output.txt", "w") as file_out:
        file_out.write(str(result)) 


if __name__ == '__main__':
    main()

            


