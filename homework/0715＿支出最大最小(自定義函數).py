def min_max_sum(num_list):
    '''
    input: list or dict
    遍歷判斷最小值、最大值、累加值
    return: tuple(最小值、最大值、累加值)
    時間複雜度 O(n)
    '''
    min_number = num_list[0]
    max_number = num_list[0]
    sum_number = 0
    for i in range(len(num_list)):
        if num_list[i] < min_number:
            min_number = num_list[i]
        if num_list[i] > max_number:
            max_number = num_list[i]
        sum_number += num_list[i]
    return min_number, max_number, sum_number

def my_sort(sort_list):
    '''
    input: list
    創建一個很大的list
    直接將輸入list中各個的值，等同於新list中的位置 
    output: 由小排到大的list(去重複)
    時間複雜度: O(max(list number))
    '''
    if sort_list.__class__ != type(dict()):  # 解決 TypeError: 'dict_values' object is not subscriptable
        sort_list = list(sort_list)
    sorted = [None] * (max(sort_list) + 1)  # 創建輸入list中最大數字個數的list
    f_sorted = []
    for i in range(len(sort_list)):  # 值為多少，該值就是新list中的位置
        sorted[sort_list[i]] = sort_list[i]
    for i in range(len(sorted)):  # 去除多餘的空間
        if sorted[i] is not None:
            f_sorted.append(sorted[i])
    return f_sorted

def my_sort2(sort_list):
    '''
    input: list
    創建一個很大的list
    直接將輸入list中各個的值，等同於新list中的位置
    output: 由小排到大的list
    時間複雜度: O(max(list number))
    '''
    if sort_list.__class__ != type(dict()):  # 解決 TypeError: 'dict_values' object is not subscriptable
        sort_list = list(sort_list)
    sorted = [None] * (max(sort_list) + 1)  # 創建輸入list中最大數字個數的list
    second_list = []  # 將重複的值丟進去
    f_sorted = []
    for i in range(len(sort_list)):  # 值為多少，該值就是新list中的位置
        if sorted[sort_list[i]] != None:
            second_list.append(sort_list[i])
        sorted[sort_list[i]] = sort_list[i]
    for i in range(len(sorted)):  # 去除多餘的空間
        if sorted[i] is not None:
            f_sorted.append(sorted[i])
    for i in second_list:
        f_sorted.insert(f_sorted.index(i), i)
    return f_sorted

def list_mether_of_sum(month=4):
    list_of_expend = [None] * month
    for i in range(0, month):
        list_of_expend[i] = int(input(f'請輸入第{i + 1}個月的支出金額：'))
    min_list_of_expend, max_list_of_expend, sum_list_of_expend = min_max_sum(list_of_expend)
    print(f'支出最多的金額為:{max_list_of_expend}')
    print(f'支出最少的金額為:{min_list_of_expend}')
    print(f'支出總額為:{sum_list_of_expend}')
    print(f'支出金額由小到大排序為{my_sort2(list_of_expend)}')

def dict_mether_of_sum(month=4):
    dict_of_expend = dict()
    for i in range(month):  # 使用者輸入每個月支出金額
        dict_of_expend[i] = int(input(f'請輸入第{i + 1}個月的支出金額：'))
    min_expend, max_expend, sum_expend = min_max_sum(dict_of_expend)
    print(f'支出最多的金額為:{max_expend}')
    print(f'支出最少的金額為:{min_expend}')
    print(f'支出總額為:{sum_expend}')
    print(f'支出金額由小到大排序為{my_sort2(dict_of_expend.values())}')


if __name__ == '__main__':
    import random
    for i in range(10):
        test_list = []  # 創建測試清單
        for i in range(4):
            test_list.append(random.randint(0, 9999))

        # 驗證min_max_sum()函數
        a, b, c = min_max_sum(test_list)
        print((min(test_list), max(test_list), sum(test_list)) == (a, b, c))

        # 驗證my_sort()函數
        print(my_sort2(test_list) == sorted(test_list))

    dict_mether_of_sum()
    list_mether_of_sum()