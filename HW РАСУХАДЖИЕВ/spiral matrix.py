size_matrix = int(input())
list_db = [[0 for x in range (size_matrix)] for y in range(size_matrix)]

n = 1
low = 0
high = size_matrix-1
count = int((size_matrix+1)/2)
for i in range(count):
    for j in range(low,high+1):
        list_db[i][j]=n
        n=n+1
    for j in range(low+1,high+1):
        list_db[j][high]=n
        n=n+1
    for j in range(high-1,low-1,-1):
        list_db[high][j]=n
        n=n+1
    for j in range(high-1,low,-1):
        list_db[j][low]=n
        n=n+1
    low=low+1
    high=high-1

for i in range(size_matrix):
    for j in range(size_matrix):
        print(list_db[i][j], end="\t")
    print()
