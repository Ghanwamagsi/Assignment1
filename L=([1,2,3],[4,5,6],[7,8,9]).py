L=([1,2,3],[4,5,6],[7,8,9])
for i in range(3):
    for j in range(3):
        print(L[i][j], end=' ')
        print()

a = [10,20,30,20,10,50,60,40,80,50,40]
dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)