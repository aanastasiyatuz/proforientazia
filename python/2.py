# импортируем нужные библиотеки для дальнейшего использования
import telebot
from telebot import types
import random  # библиотека со случайными значениями


token = ''
# создаем бота-программу со связью к телеграм-чату через токен (уникальный код доступа к чату)
bot = telebot.TeleBot(token)


# создаем клавиатуру
keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
# создаем кнопки
button1 = types.KeyboardButton('Играть')
button2 = types.KeyboardButton('Нет')
# добавляем кнопки в клавиатуру
keyboard.add(button1, button2)


# создаем функцию start_message, и оборачиваем ее в message_handler, чтобы наш бот понимал, что эта функция нужна для ответа на определенные сообщения от пользователя
@bot.message_handler(commands=['start'])
def start_message(message):
    # через send_message мы отправляем сообщение в чат
    # message.chat.id позволяет нам достать из сообщения адрес, куда отправить сообщение
    # reply_markup позволяет прикрепить к сообщению клавиатуру
    msg = bot.send_message(message.chat.id, f'Привет, {message.chat.first_name}, начнем игру?', reply_markup=keyboard)
    # ждем нажатия кнопки и потом полученное сообщение проверяем в функции check_answer
    bot.register_next_step_handler(msg, check_answer)

# создаем функцию check_answer, чтобы либо начать игру, либо попрощаться с пользователем
def check_answer(message):
    # если нажал на кнопку Играть
    if message.text == 'Играть':
        # с помощью random.choice мы выбираем случайный элемент из последовательности
        # range создает нам последовательность чисел в заданном диапазоне
        random_int = random.choice(range(1, 11))
        # с помощью print мы выводим в терминал какое число выбрала программа и строку 'выбранное число'
        print(random_int, 'выбранное число')
        msg = bot.send_message(message.chat.id, 'Правила игры: нужно угадать число от 1 до 10 за 3 попытки')
        # запускаем функцию game и передаем ей сообщение, кол-во попыток и случайное число
        game(message, attempts, random_int)

    # если нажал нет
    else:
        bot.send_message(message.chat.id, 'окей, до встречи!')


# логика игры


# указываем кол-во попыток
attempts = 3

# создаем функцию game
def game(message, attempts, random_int):
    # отнимаем одну попытку
    attempts = attempts - 1
    msg = bot.send_message(message.chat.id, 'Выбери число')
    # дожидаемся, когда пользователь введет число и передаем сообщение, кол-во попыток и случайное число функции check_number
    bot.register_next_step_handler(msg, check_number, attempts, random_int)

# создаем функцию check_number
def check_number(message, attempts, random_int):
    # если число, введенное пользователем совпадает с загаданным числом
    # важно, что то, что пишет пользователь, приходит в виде строки
    # поэтому мы конвертируем загаданное число в строку через str
    if message.text == str(random_int):
        bot.send_message(message.chat.id, 'Вы победили! Начать с начала /start ?')
    
    # если число, введенное пользователем не совпадает с загаданным числом
    else:
        # если попытки закончились
        if attempts == 0:
            bot.send_message(message.chat.id, 'Извините, у вас закончились попытки')

        # если попытки еще есть
        else:
            msg = bot.send_message(message.chat.id, 'Попробуйте еще раз')
            # запускаем снова функцию game, таким образом продолжая игру
            game(msg, attempts, random_int)

# запускаем программу телеграм-бота
bot.polling()
