def is_correct_bracket_seq(item):
    stack = []
    open_bracket_seq = '({['
    close_braket_seq = ')}]'
    dict_del_seq = {')': '(', '}': '{', ']': '['}
    
    for i in item:
        if i in open_bracket_seq:
            stack.append(i)
        elif i in close_braket_seq:
            if not stack or stack[-1] != dict_del_seq[i]:
                return False
            stack.pop()
    return len(stack) == 0


if __name__ == '__main__':
    # item = input().split()
    # print(is_correct_bracket_seq(item))
    item = ['{', '[', '(', ')', ']', '}']
    print(is_correct_bracket_seq(item))
