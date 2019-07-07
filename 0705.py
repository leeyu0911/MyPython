year = None
while year is None:
    try:
        year = float(input('請輸入年份: '))
        if year % 1 != 0:
            print('年份為整數')
            year = None
        else:
            year = int(year)
    except:
        print('請輸入整數')


if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print('Common Year')
