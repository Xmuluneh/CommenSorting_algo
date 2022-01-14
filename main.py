def selectionSort(list):
    for i in range(len(list)):
        passI = i
        for k in range(i + 1, len(list)):
            if list[k] < list[passI]:
                passI = k

        list[i], list[passI] = list[passI], list[i]


def main():
    list = [0, 2, 1, 9, 8, 7, 4, 3, 6, -7]
    selectionSort(list)
    print("The selection sort algo is :", list)
    a = [0, 2, 1, 9, 8, 7, 4, 3, 6, -9]
    insertionSort(a)
    print("The insertion sort algo is : ", a)
    lst = [1, 9, 4.5, 10.6, 5.7, -4.5]
    mulunehSorting(lst)
    print("The so called Mulua algo is ",lst)


def insertionSort(list):
    for i in range(1, len(list)):
        temp = list[i]
        passI = i
        while passI > 0 and list[passI - 1] > temp:
            list[passI] = list[passI - 1]
            passI = passI - 1
        list[passI] = temp


def mulunehSorting(list):
    flag = True
    while flag:
        flag = False
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                list[i + 1], list[i] = list[i], list[i + 1]
                flag = True


main()

