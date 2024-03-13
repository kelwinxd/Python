def mutate_string(string, position, character):
    alist = list(string)
    alist[position] = character
    result = ''.join(alist)
    return result

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)