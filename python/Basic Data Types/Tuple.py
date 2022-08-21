integer_list = map(int, input().split())
t_inp = tuple(integer_list)
print(hash(t_inp))