letter = int(input('Введите число по горизонтали для первой фигуры: '))
number = int(input('Введите число по вертикали для первой фигуры: '))
letter1 = int(input('Введите число по горизонтали для второй фигуры: '))
number1 = int(input('Введите число по вертикали для второй фигуры: '))
letters = range (1, 9)
letters1 = range (1, 9)
numbers = range (1, 9)
numbers1 = range (1, 9)
k = 0
n = 0
e = 0
f = 0
x = 0
y = 0

if letter not in letters:
    print('Число не подходит, используйте 1-8')
elif number not in numbers:
    print('Число не подходит используйте 1-8')
elif letter1 not in letters1:
    print('Число не подходит используйте 1-8')
elif number1 not in numbers1:
    print('Число не подходит используйте 1-8')    
    
else:
    if letter % 2 == number % 2:
        k = 1
    else:
        k = 2
    if letter1 % 2 == number1% 2:
        n = 1
    else:
        n = 2
    if n == k:
        print('Фигуры на одном цвете')
    else:
        print('Фигуры на разных цветах')
    
piece = input('Введите фигуру: ').lower()

e = abs(letter - number)
f = abs(letter1 - number1)
if piece not in  'слон' and piece not in'ферзь' and piece not in 'ладья' and piece not in'конь':
    print('Проверте правльность введенной фигуры')
else:
    if piece == 'слон':
        if e == f:
            print('Слон угрожает второй фигуре за один ход')
        else:
            print('Слон не угрожает второй фигуре за один ход')
            if k == n:
                for i in range(1, 9):
                    for j in range(1, 9):
                        if (abs(letter - i) == abs(number - j)) and (abs(i - letter1) == abs(j - number1) ):
                            print('Слон угрожает второй фигуре в два хода, сначала нужно сделать ход на поле:' , i , j)
                    
    elif piece == 'ладья':
        if letter == letter1 or number == number1:
            print('Ладья угрожает второй фигуре за один ход')
        else:
            print('Ладья не угрожает второй фигуре за один ход')
                        
            print('Ладья угрожает второй фигуре в два хода, сначала нужно сделать ход на поле:' , letter , number1,'или', letter1, number)
    elif piece == 'конь':
        if e == 1 and f == 2 or e == 2 or f == 1:
            print('Конь угрожает второй фигуре за один ход')
        else:
            print('Конь не угрожает второй фигуре за один ход')    
                
    elif piece == 'ферзь':
        if e == f:
            print('Ферзь угрожает второй фигуре за один ход')
        elif letter == letter1 or number == number1:
            print('Ферзь угрожает второй фигуре за один ход')
        else:
            print('Ферзь не угрожает второй фигуре за один ход')
          
            print('Ферзь угрожает второй фигуре в два хода, сначала нужно сделать ход на поле:' , letter , number1 ,'или', letter1, number )
    elif piece == 'конь':
        if abs(letter - letter1) == 2 and abs(number - number1) == 1:
            print('Конь угрожает второй фигуре за один ход')
        elif abs(letter - letter1) == 1 and abs(number - number1) == 2:
            print('Конь угрожает второй фигуре за один ход')
        else:
            print('Конь не угрожает второй фигуре за один ход')
            
            