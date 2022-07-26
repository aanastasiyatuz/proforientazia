# https://replit.com/



"""==========Типы данных=========="""
# Числа и строки

5 # это число
6.3 # это число

hello world # без кавычек будет восприниматься как инструкция
'hello world' # это строка в одинарных кавычках
"hello world" # это строка в двойных кавычках

'5' # это строка, хоть и хранит в себе символ числа



"""==========Переменные=========="""
# переменная - имя, которое мы даем каким-то данным или кусочку кода, 
# чтобы обращаясь по имени мы могли получить эти данные или использовать тот кусочек кода

number = 5
# мы создали переменную с названием number и положили значение число 5

string = 'hello world'
# мы создали переменную с названием string и положили в значение строку 'hello world'



"""==========Операции=========="""
# с числами мы можем проводить все арифметические операции

5 + 5 # сложение
10 - 8 # вычитание
2 * 3 # умножение
12 / 4 # деление
3 ** 2 # возведение в степень


# со строками мы также можем проводить определенные манипуляции

string = "HellO WOrld"
string.lower() # привести в нижний регистр ('hello world')
string.upper() # привести в верхний регистр ('HELLO WORLD')
string.title() # привести каждое слово в нижний регистр, но с заглавной первой буквой



"""==========Вывод данных=========="""
# для вывода данных в терминал мы можем использовать функцию print
print(5)
print(5,6,7,8,9)
print('hello world')
print('makers', 'bootcamp')



"""==========Сравнение данных=========="""
# для сравнения данных есть специальные операторы 
# (которые вернут True, если сравнение верное, False в обратном случае)

5 == 5 # проверка на равенство (True)
3 == 1 # (False)

3 > 2 # проверка, что первое число больше (True)
1 > 5 # (False)

10 < 8 # проверка, что второе число больше (False)
10 < 10 # (False)

7 != 8 # проверка на неравенство (True)
5 != 5 # (False)

3 >= 2 # проверка, что первое число больше или равно второму (True)
5 >= 5 # (True)
3 >= 6 # (False)

6 <= 2 # проверка, что второе число больше или равно первому (False)
6 <= 13 # (True)
7 <= 7 # (True)

"5" == 5 # False
"5" == str(5) # True

"""==========Условия=========="""
# условия нам нужны для того, чтобы выполнялись или не выполнялись определенные участки кода

# для того, чтобы сделать условие пишем if и само условие 
# на последующих строках все, что относится к выполнению этого условия, будет сдвинуто на один tab

if 5 == 5:
    # выйдет если условие верное
    print("5 равно 5")

# так же мы можем указать, что делать если условие не верное
# для этого после основного условия добавляем else и пишем ниже код (отступая один tab), 
# который будет выполняться если условие не верное

if 5 > 2:
    # выйдет если условие верное
    print("5 больше 2")
else:
    # выйдет если условие не верное
    print("5 не больше 2")



"""==========Функции=========="""
# чтобы положить в переменную кусочек кода, мы можем создать функцию

# создадим функцию my_function
def my_function():
    # внутри пропишем, что она должна будет делать, если мы обратимся к ней
    number = 5
    print(number)

# можем обращаться к ней неограниченное код-во раз, когда нам нужно выполнить функционал, 
# находящийся внутри нее
my_function()
my_function()
my_function()
# в данном случае в терминал 3 раза выйдет число 5, 
# потому что функцию мы вызвали (обратились к ней) 3 раза
