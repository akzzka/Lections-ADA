p = 1
while p > 0: 
    a = int(input('Введите число: '))
    b = int(input('Введи второе число: '))
    c = input('Выберите операцию "+, -, *, /, %, //": ')
    if c == '+':
        print('Ответ: ',a+b)
    elif c == '-':
        print('Ответ: ',a-b)
    elif c == '*':
        print('Ответ: ',a*b)
    elif c == '/':
        print('Ответ: ',a/b) 
    elif c == '%':
        print('Ответ: ', a%b)
    elif c == '//':
        print('Ответ: ', a//b)
    else: print('Данной операции нет в системе!'.upper().center(50))
    i = input('Вы хотите продолжить (yes/no) ?: ') 
    if i == 'yes': p+=1
    elif i == 'no': 
        print('До свидания!'.center(50))
        break   
    else: 
        print('Вы ввели неправильный символ!'.center(50))
        p -= 1