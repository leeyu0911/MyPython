def list_mether_of_sum(month=4):
    list_of_expend = [None] * month
    for i in range(0, month):
        list_of_expend[i] = int(input(f'請輸入第{i+1}個月的支出金額：'))
    print(f'支出最多的金額為:{max(list_of_expend)}')
    print(f'支出最少的金額為:{min(list_of_expend)}')
    print(f'支出總額為:{sum(list_of_expend)}')
    print(f'支出金額由小到大排序為{sorted(list_of_expend)}')

def dict_mether_of_sum(month=4):
    dict_of_expend = dict()
    max_expend = 0
    min_expend = 0
    sum_expend = 0

    # 使用者輸入每個月支出金額
    for i in range(month):
        dict_of_expend[i+1] = int(input(f'請輸入第{i+1}個月的支出金額：')) 

    # 遍歷取得字典中最大最小值以及加總
    min_expend = dict_of_expend[1]
    for i in range(1, month+1):
        if int(dict_of_expend[i]) > max_expend:
            max_expend = dict_of_expend[i]
        if int(dict_of_expend[i]) < min_expend:
            min_expend = dict_of_expend[i]
        sum_expend += dict_of_expend[i]
    print(f'支出最多的金額為:{max_expend}')
    print(f'支出最少的金額為:{min_expend}')
    print(f'支出總額為:{sum_expend}')
    print(f'支出金額由小到大排序為{sorted(dict_of_expend.values())}')



    



if __name__ == '__main__':
    dict_mether_of_sum()