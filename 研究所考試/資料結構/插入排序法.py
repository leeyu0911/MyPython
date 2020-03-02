a = [34, 56, 4, 10, 77, 51, 93, 30, 5, 52]


def insertion_sort(data):
    for i in range(1, len(data)):
        insert = data[i]
        moveitem = i
        while (moveitem > 0) and (data[moveitem-1] > insert):
            data[moveitem] = data[moveitem-1]
            moveitem -= 1
        data[moveitem] = insert
    return data


print(insertion_sort(a))
