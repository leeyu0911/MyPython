height = None
weight = None


while height is None:
    try:
        height = float(input('請輸入身高(公分): '))
    except:
        print('請輸入數字')
        
while weight is None:
    try:
        weight = float(input('請輸入體重(公斤): '))
    except:
        print('請輸入數字')

        
BMI = round(weight / ((height/100) ** 2), 2)


if BMI > 30:
    print(f'身體狀態:肥胖 BMI:{BMI}')
elif BMI > 25:
    print(f'身體狀態:過重 BMI:{BMI}')
elif BMI > 18.5:
    print(f'身體狀態:正常 BMI:{BMI}')
else:
    print(f'身體狀態:太輕 BMI:{BMI}')

