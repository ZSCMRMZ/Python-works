ls1 = [5, 4, 2, 1, 3]
ls2 = [9, 5, 4, 3, 2, 1, 6, 2]

def selection_sort(ls,order):
    for i in range(len(ls) - 1):
        min = i
        if order == 1:
            for j in range(i+1, len(ls)):
                if ls[j] < ls[min]:
                    min = j
        if order == 2:
            for j in range(i+1, len(ls)):
                if ls[j] > ls[min]:
                    min = j

        ls[i], ls[min] = ls[min], ls[i]
    return(ls)

print(selection_sort(ls1, 1))
print(selection_sort(ls2, 2))
input()
