a0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
print(a0)

a1 = range(10)
print(a1)

a2 = [i for i in a1 if i in a0]
print(a2)

a3 = [a0[s] for s in a0]   # a3 = a0.values
print(a3)

a4 = [1, 2, 3, 4, 5]
print(a4)

a5 = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
print(a5)

a6 = [[0, 0], [1, 1], [2, 4],[3, 9], [4, 16], [5, 25], [6, 36],[7, 49],[8, 64] ,[9,81]]