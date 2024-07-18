
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


        


if __name__ == '__main__':
    seq = input()
    # seq = 'abcabcbb'
    print(find_substring(seq))

            


