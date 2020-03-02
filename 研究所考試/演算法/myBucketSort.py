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