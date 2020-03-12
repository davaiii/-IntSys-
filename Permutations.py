import itertools
n = '1234'
s = [''.join(i) for i in itertools.permutations(n,3)]

print(s)