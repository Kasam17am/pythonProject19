def quicksort(alist, start, end):
    '''Sorts the list from indexes start to end - 1 inclusive.'''
    i = start
    j = end
    pivot = alist[(start + end) // 2][4]

    while True:
        while alist[i][4] < pivot:
            i = i + 1
        while alist[j][4] > pivot:
            j = j - 1
        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
            i = i + 1
            j = j - 1
        else:
            break

    if start < j:
        quicksort(alist, start, j)
    if i < end:
        quicksort(alist, i, end)

with open ('students_utf8 (3).csv') as f:
    a=[]
    for line in f:
        a.append(line.strip('\n').split(','))
s=a[0]
s1=[]
for i in range (1,len(a)):
    if a[i][4]==' None':
        a[i][4]=0
    else:
        b=a[i][4]
        a[i][4]=int(b)
    s1.append(a[i])
start = 0
end = len(s1)-1
quicksort(s1, start, end)
print(s1)