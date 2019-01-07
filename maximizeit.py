import itertools as itool

# get k and m values
k, m = list(map(int, input().split(" ")))

# generate a list of lists
nums = [[] for i in range(k)]
for i in range(k):
    nums[i] = list(map(int, input().split(" ")))
    nums[i].pop(0)  # removes first element from each list (it's unnecessary)

# generate a list of lists containing all possible element combinations
testers = list(map(list, itool.product(*nums)))

# determine the highest possible moded list
maxmod = 0
for i in range(len(testers)):
    t_square = [i ** 2 for i in testers[i]]
    t_sum = sum(t_square)
    t_mod = t_sum % m
    if t_mod > maxmod:
        maxmod = t_mod

# viola
print(maxmod)
