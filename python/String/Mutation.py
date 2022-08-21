def mutate_string(string, position, character):
    sli= list(string)
    sli[position] = character
    sts = ''.join(sli)
    return sts

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)