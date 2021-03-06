import random
from timeit import default_timer as timer


pole = random.sample(range(5000), 5000)

pole_bubble = pole
pole_insertion = pole
pole_merge = pole
pole_quick = pole
pole_selection = pole

print("Nezoradené pole je: ", pole)

start_bubble = timer()

def bubbleSort(pole_bubble):
    n = len(pole_bubble)

    for i in range(n - 1):

        for j in range(0, n - i - 1):

            if pole_bubble[j] > pole_bubble[j + 1]:
                pole_bubble[j], pole_bubble[j + 1] = pole_bubble[j + 1], pole_bubble[j]

bubbleSort(pole_bubble)

end_bubble = timer()

cas_bubble = end_bubble - start_bubble


start_insertion = timer()

def insertionSort(pole_insertion):
    for i in range(1, len(pole_insertion)):

        key = pole_insertion[i]

        j = i - 1
        while j >= 0 and key < pole_insertion[j]:
            pole_insertion[j + 1] = pole_insertion[j]
            j -= 1
        pole_insertion[j + 1] = key

insertionSort(pole_insertion)

end_insertion = timer()

cas_insertion = end_insertion - start_insertion


start_merge = timer()

def mergeSort(pole_merge):
    if len(pole_merge) > 1:

        mid = len(pole_merge) // 2

        L = pole_merge[:mid]

        R = pole_merge[mid:]

        mergeSort(L)

        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                pole_merge[k] = L[i]
                i += 1
            else:
                pole_merge[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            pole_merge[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            pole_merge[k] = R[j]
            j += 1
            k += 1

mergeSort(pole_merge)

end_merge = timer()

cas_merge = end_merge - start_merge


start_quick = timer()


def partition(pole_quick, l, h):
    i = (l - 1)
    x = pole_quick[h]

    for j in range(l, h):
        if pole_quick[j] <= x:

            i = i + 1
            pole_quick[i], pole_quick[j] = pole_quick[j], pole_quick[i]

    pole_quick[i + 1], pole_quick[h] = pole_quick[h], pole_quick[i + 1]
    return (i + 1)

def quickSortIterative(pole_quick, l, h):

    size = h - l + 1
    stack = [0] * (size)

    top = -1

    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h

    while top >= 0:

        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1

        p = partition(pole_quick, l, h)

        if p - 1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1

        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h

end_quick = timer()

cas_quick = end_quick - start_quick


start_selection = timer()

for i in range(len(pole_selection)):

    min_idx = i
    for j in range(i + 1, len(pole_selection)):
        if pole_selection[min_idx] > pole_selection[j]:
            min_idx = j

    pole_selection[i], pole_selection[min_idx] = pole_selection[min_idx], pole_selection[i]

end_selection = timer()

cas_selection = end_selection - start_selection

print("Zoradene pole: ", pole_bubble)
print("Rýchlosť insertion sortu je: ",cas_insertion, "sek.")
print("Rýchlosť quick sortu je: ",cas_quick, "sek.")
print("Rýchlosť selection sortu je: ",cas_selection, "sek.")
print("Rýchlosť bubble sortu je: ",cas_bubble, "sek.")
print("Rýchlosť merge sortu je: ",cas_merge, "sek.")