import telebot
from telebot import types
import datetime

bot = telebot.TeleBot('8155961778:AAErdMoHYfj3bTjwl9NAoZHfNBP7R1bNrEw')

weekdays = datetime.date.today().isoweekday()
weekyears = datetime.date.today().strftime("%U")
lastweekyears = int(str(weekyears)[-1])
if lastweekyears % 2 == 0:
    week=2   #под
else:
    week=1   #над
    
Manday1groupup = '1⃣(Лек.) Метрология\n1-422\n(Столяров А.И.)\n\n2⃣(П.з.) Управление качеством\n1-304а\n(Герасимова О.В.)\n\n3⃣(Лек.) Управление качеством\n1-304а\n(Герасимова О.В.)\n\n4⃣Физкультура\n\n5⃣(Л.р) МТиТ\n1-2\n(Прусенко И.Н.)'                  
Manday1groupdown = '3⃣(Лек.) Управление качеством\n1-304а\n(Герасимова О.В.)\n\n4⃣Физкультура\n\n5⃣(Л.р) МТиТ\n1-2\n(Прусенко И.Н.)'
Manday2groupup = '1⃣(Лек.) Метрология\n1-422\n(Столяров А.И.)\n\n2⃣(П.з.) Управление качеством \n1-304а\n(Герасимова О.В.)\n\n3⃣(Лек.) Управление качеством \n1-304а\n(Герасимова О.В.)\n\n4⃣Физкультура'
Manday2groupdown = '3⃣(Лек.) Управление качеством\n1-304а\n(Герасимова О.В.\n\n4⃣Физкультура'
                                        
Tuesday1groupup = '1⃣(П.з.) Прикладная Механика\n1.429\nКонцевой И.А.\n\n2⃣(Лек.) Прикладная Механика\n1.429\nКонцевой И.А.\n\n3⃣(П.з.) Метрология\n1-429\nСтоляров А.И'
Tuesday1groupdown = '2⃣(Лек.) Прикладная Механика\n1.429\nКонцевой И.А.\n\n3⃣(П.з.) Метрология\n1-429\nСтоляров А.И'
Tuesday2groupup = '1⃣(П.з.) Прикладная Механика\n1.429\nКонцевой И.А.\n\n2⃣(Лек.) Прикладная Механика\n1.429\nКонцевой И.А.\n\n3⃣(П.з.) Метрология\n1-429\nСтоляров А.И'
Tuesday2groupdown = '2⃣(Лек.) Прикладная Механика\n1.429\nКонцевой И.А.\n\n3⃣(П.з.) Метрология\n1-429\nСтоляров А.И'

Wednesday1groupup = '1⃣(П.з.)ОУИС\n1-308\n(Русая Л.Н.)\n\n2⃣(лек.)История\n1-212\n(Грищенко И.А.)\n\n3⃣(лек.) ЭТЭ\n2-13\nШабловский Я.О.\n\n4⃣Физкультура'
Wednesday1groupdown = '1⃣(П.з.) ЭТЭ\n2-13\nШабловский Я.О.\n\n2⃣(лек.)История\n1-212\n(Грищенко И.А.)\n\n3⃣(лек.)История\n1-212\n(Грищенко И.А.)\n\n4⃣Физкультура'
Wednesday2groupup  = '1⃣(П.з.)ОУИС\n1-308\n(Русая Л.Н.)\n\n2⃣(лек.)История\n1-212\n(Грищенко И.А.)\n\n3⃣(лек.) ЭТЭ\n2-13\nШабловский Я.О.\n\n4⃣Физкультура'
Wednesday2groupdown = '1⃣(П.з.) ЭТЭ\n2-13\nШабловский Я.О.\n\n2⃣(лек.)История\n1-212\n(Грищенко И.А.)\n\n3⃣(лек.)Исто6рия\n1-212\n(Грищенко И.А.)\n\n4⃣Физкультура'

Thursday1groupup = '1⃣(Лек.) ЭТЭ\n2.13\n(Шабловский Я.О.)\n\n2⃣(лек.) ОУИС\n1-422\n(Русая Л.Н)\n\n3⃣(л.р.) ЭТЭ\n2-404\n(Шабловский Я.О.)\n\n4⃣(лек.) Охрана Труда\nТ-2\n(Герасимова О.В.)'
Thursday1groupdown = '1⃣(Лек.) ЭТЭ\n2.13\n(Шабловский Я.О.)\n\n2⃣(лек.) ОУИС\n1-422\n(Русая Л.Н)\n\n3⃣(л.р.) Охрана Труда\nТ-2\n(Герасимова О.В.)\n\n4⃣(лек.) Охрана Труда\nТ-2\n(Герасимова О.В.)'
Thursday2groupup = '1⃣(Лек.) ЭТЭ\n2.13\n(Шабловский Я.О.)\n\n2⃣(лек.) ОУИС\n1-422\n(Русая Л.Н)\n\n3⃣(л.р.) Охрана Труда\nТ-2\n(Герасимова О.В.)\n\n4⃣(лек.) Охрана Труда\nТ-2\n(Герасимова О.В.)'
Thursday2groupdown = '1⃣(Лек.) ЭТЭ\n2.13\n(Шабловский Я.О.)\n\n2⃣(лек.) ОУИС\n1-422\n(Русая Л.Н)\n\n3⃣(л.р.) ЭТЭ\n2-404\n(Шабловский Я.О.)\n\n4⃣(лек.) Охрана Труда\nТ-2\n(Герасимова О.В.)'

Friday1groupup = '1⃣(Л.р.) САПРТПиО\n1-304\nПрусенко И.Н.\n\n2⃣(Лек.) МТиТ\n1-305\nПрусенко И.Н.\n\n3⃣(П.з) МТиТ\n1-304а\nПрусенко И.Н.'
Friday1groupdown = '1⃣(Л.р.) САПРТПиО\n1-304\nПрусенко И.Н.\n\n2⃣(Лек.) МТиТ\n1-305\nПрусенко И.Н.\n\n3⃣(Лек.) САПРТПиО\n1-304\nПрусенко И.Н.'
Friday2groupup = '2⃣(Лек.) МТиТ\n1-305\nПрусенко И.Н.\n\n3⃣(П.з) МТиТ\n1-304а\nПрусенко И.Н.\n\n4⃣(Л.р.) САПРТПиО\n1-304\nПрусенко И.Н.'
Friday2groupdown = '2⃣(Лек.) МТиТ\n1-305\nПрусенко И.Н.\n\n3⃣(Лек.) САПРТПиО\n1-304\nПрусенко И.Н.\n\n4⃣(Л.р.) САПРТПиО\n1-304\nПрусенко И.Н.'



@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Из 1 группы')
    btn2 = types.KeyboardButton('Из 2 группы')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "👋 Привет! Из какой ты группы?", reply_markup=markup)
  

@bot.message_handler(func=lambda message: message.text == 'Из 1 группы')
def group1(message):
    global group
    group = 1
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
    btn1 = types.KeyboardButton('ПН')
    btn2 = types.KeyboardButton('ВТ')
    btn3 = types.KeyboardButton('СР')
    btn4 = types.KeyboardButton('ЧТ')
    btn5 = types.KeyboardButton('ПТ')
    btn6 = types.KeyboardButton('Назад')
    btn7 = types.KeyboardButton('Сегодня')
    btn8 = types.KeyboardButton('Завтра')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
    bot.send_message(message.from_user.id, 'Выберите день недели:', reply_markup=markup) #ответ бота
    
@bot.message_handler(func=lambda message: message.text == 'Из 2 группы')
def group2(message):
    global group
    group = 2
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
    btn1 = types.KeyboardButton('ПН')
    btn2 = types.KeyboardButton('ВТ')
    btn3 = types.KeyboardButton('СР')
    btn4 = types.KeyboardButton('ЧТ')
    btn5 = types.KeyboardButton('ПТ')
    btn6 = types.KeyboardButton('Назад')
    btn7 = types.KeyboardButton('Сегодня')
    btn8 = types.KeyboardButton('Завтра')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
    bot.send_message(message.from_user.id, 'Выберите день недели:', reply_markup=markup) #ответ бота
    
@bot.message_handler(func=lambda message: message.text == 'ПН')
def Manday(message):    
    if group == 2 and week== 1:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('ПН')
        btn2 = types.KeyboardButton('ВТ')
        btn3 = types.KeyboardButton('СР')
        btn4 = types.KeyboardButton('ЧТ')
        btn5 = types.KeyboardButton('ПТ')
        btn6 = types.KeyboardButton('Назад')
        btn7 = types.KeyboardButton('Cегодня')
        btn8 = types.KeyboardButton('Завтра')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.from_user.id, Manday2groupup, reply_markup=markup) #ответ бота

    elif group == 1 and week== 1:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('ПН')
        btn2 = types.KeyboardButton('ВТ')
        btn3 = types.KeyboardButton('СР')
        btn4 = types.KeyboardButton('ЧТ')
        btn5 = types.KeyboardButton('ПТ')
        btn6 = types.KeyboardButton('Назад')
        btn7 = types.KeyboardButton('Cегодня')
        btn8 = types.KeyboardButton('Завтра')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.chat.id, Manday1groupup , reply_markup=markup) #ответ бота
        
    elif group == 2 and week== 2:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('ПН')
        btn2 = types.KeyboardButton('ВТ')
        btn3 = types.KeyboardButton('СР')
        btn4 = types.KeyboardButton('ЧТ')
        btn5 = types.KeyboardButton('ПТ')
        btn6 = types.KeyboardButton('Назад')
        btn7 = types.KeyboardButton('Cегодня')
        btn8 = types.KeyboardButton('Завтра')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.from_user.id, Manday2groupdown , reply_markup=markup) #ответ бота

    elif group == 1 and week== 2:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('ПН')
        btn2 = types.KeyboardButton('ВТ')
        btn3 = types.KeyboardButton('СР')
        btn4 = types.KeyboardButton('ЧТ')
        btn5 = types.KeyboardButton('ПТ')
        btn6 = types.KeyboardButton('Назад')
        btn7 = types.KeyboardButton('Cегодня')
        btn8 = types.KeyboardButton('Завтра')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.from_user.id, Manday1groupdown , reply_markup=markup) #ответ бота


        
@bot.message_handler(func=lambda message: message.text == 'ВТ')
def Tuesday(message):    
    if group == 2 and week== 1:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('ПН')
        btn2 = types.KeyboardButton('ВТ')
        btn3 = types.KeyboardButton('СР')
        btn4 = types.KeyboardButton('ЧТ')
        btn5 = types.KeyboardButton('ПТ')
        btn6 = types.KeyboardButton('Назад')
        btn7 = types.KeyboardButton('Cегодня')
        btn8 = types.KeyboardButton('Завтра')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.from_user.id, Tuesday2groupup, reply_markup=markup) #ответ бота

    elif group == 1 and week== 1:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('ПН')
        btn2 = types.KeyboardButton('ВТ')
        btn3 = types.KeyboardButton('СР')
        btn4 = types.KeyboardButton('ЧТ')
        btn5 = types.KeyboardButton('ПТ')
        btn6 = types.KeyboardButton('Назад')
        btn7 = types.KeyboardButton('Cегодня')
        btn8 = types.KeyboardButton('Завтра')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.chat.id, Tuesday1groupup , reply_markup=markup) #ответ бота
        
    elif group == 2 and week== 2:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('ПН')
        btn2 = types.KeyboardButton('ВТ')
        btn3 = types.KeyboardButton('СР')
        btn4 = types.KeyboardButton('ЧТ')
        btn5 = types.KeyboardButton('ПТ')
        btn6 = types.KeyboardButton('Назад')
        btn7 = types.KeyboardButton('Cегодня')
        btn8 = types.KeyboardButton('Завтра')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.from_user.id, Tuesday2groupdown , reply_markup=markup) #ответ бота

    elif group == 1 and week== 2:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('ПН')
        btn2 = types.KeyboardButton('ВТ')
        btn3 = types.KeyboardButton('СР')
        btn4 = types.KeyboardButton('ЧТ')
        btn5 = types.KeyboardButton('ПТ')
        btn6 = types.KeyboardButton('Назад')
        btn7 = types.KeyboardButton('Cегодня')
        btn8 = types.KeyboardButton('Завтра')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.from_user.id, Tuesday1groupdown , reply_markup=markup) #ответ бота

@bot.message_handler(func=lambda message: message.text == 'СР')
def Wednesday(message):    
    if group == 2 and week== 1:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('ПН')
        btn2 = types.KeyboardButton('ВТ')
        btn3 = types.KeyboardButton('СР')
        btn4 = types.KeyboardButton('ЧТ')
        btn5 = types.KeyboardButton('ПТ')
        btn6 = types.KeyboardButton('Назад')
        btn7 = types.KeyboardButton('Cегодня')
        btn8 = types.KeyboardButton('Завтра')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.from_user.id, Wednesday2groupup, reply_markup=markup) #ответ бота

    elif group == 1 and week== 1:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('ПН')
        btn2 = types.KeyboardButton('ВТ')
        btn3 = types.KeyboardButton('СР')
        btn4 = types.KeyboardButton('ЧТ')
        btn5 = types.KeyboardButton('ПТ')
        btn6 = types.KeyboardButton('Назад')
        btn7 = types.KeyboardButton('Cегодня')
        btn8 = types.KeyboardButton('Завтра')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.chat.id, Wednesday1groupup , reply_markup=markup) #ответ бота
        
    elif group == 2 and week== 2:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('ПН')
        btn2 = types.KeyboardButton('ВТ')
        btn3 = types.KeyboardButton('СР')
        btn4 = types.KeyboardButton('ЧТ')
        btn5 = types.KeyboardButton('ПТ')
        btn6 = types.KeyboardButton('Назад')
        btn7 = types.KeyboardButton('Cегодня')
        btn8 = types.KeyboardButton('Завтра')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.from_user.id, Wednesday2groupdown , reply_markup=markup) #ответ бота

    elif group == 1 and week== 2:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('ПН')
        btn2 = types.KeyboardButton('ВТ')
        btn3 = types.KeyboardButton('СР')
        btn4 = types.KeyboardButton('ЧТ')
        btn5 = types.KeyboardButton('ПТ')
        btn6 = types.KeyboardButton('Назад')
        btn7 = types.KeyboardButton('Cегодня')
        btn8 = types.KeyboardButton('Завтра')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.from_user.id, Wednesday1groupdown , reply_markup=markup) #ответ бота

@bot.message_handler(func=lambda message: message.text == 'ЧТ')
def Thursday(message):    
    if group == 2 and week== 1:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('ПН')
        btn2 = types.KeyboardButton('ВТ')
        btn3 = types.KeyboardButton('СР')
        btn4 = types.KeyboardButton('ЧТ')
        btn5 = types.KeyboardButton('ПТ')
        btn6 = types.KeyboardButton('Назад')
        btn7 = types.KeyboardButton('Cегодня')
        btn8 = types.KeyboardButton('Завтра')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.from_user.id, Thursday2groupup, reply_markup=markup) #ответ бота

    elif group == 1 and week== 1:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('ПН')
        btn2 = types.KeyboardButton('ВТ')
        btn3 = types.KeyboardButton('СР')
        btn4 = types.KeyboardButton('ЧТ')
        btn5 = types.KeyboardButton('ПТ')
        btn6 = types.KeyboardButton('Назад')
        btn7 = types.KeyboardButton('Cегодня')
        btn8 = types.KeyboardButton('Завтра')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.chat.id, Thursday1groupup , reply_markup=markup) #ответ бота
        
    elif group == 2 and week== 2:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('ПН')
        btn2 = types.KeyboardButton('ВТ')
        btn3 = types.KeyboardButton('СР')
        btn4 = types.KeyboardButton('ЧТ')
        btn5 = types.KeyboardButton('ПТ')
        btn6 = types.KeyboardButton('Назад')
        btn7 = types.KeyboardButton('Cегодня')
        btn8 = types.KeyboardButton('Завтра')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.from_user.id, Thursday2groupdown , reply_markup=markup) #ответ бота

    elif group == 1 and week== 2:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('ПН')
        btn2 = types.KeyboardButton('ВТ')
        btn3 = types.KeyboardButton('СР')
        btn4 = types.KeyboardButton('ЧТ')
        btn5 = types.KeyboardButton('ПТ')
        btn6 = types.KeyboardButton('Назад')
        btn7 = types.KeyboardButton('Cегодня')
        btn8 = types.KeyboardButton('Завтра')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.from_user.id, Thursday1groupdown , reply_markup=markup) #ответ бота

@bot.message_handler(func=lambda message: message.text == 'ПТ')
def Friday(message):    
    if group == 2 and week== 1:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('ПН')
        btn2 = types.KeyboardButton('ВТ')
        btn3 = types.KeyboardButton('СР')
        btn4 = types.KeyboardButton('ЧТ')
        btn5 = types.KeyboardButton('ПТ')
        btn6 = types.KeyboardButton('Назад')
        btn7 = types.KeyboardButton('Cегодня')
        btn8 = types.KeyboardButton('Завтра')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.from_user.id, Friday2groupup, reply_markup=markup) #ответ бота

    elif group == 1 and week== 1:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('ПН')
        btn2 = types.KeyboardButton('ВТ')
        btn3 = types.KeyboardButton('СР')
        btn4 = types.KeyboardButton('ЧТ')
        btn5 = types.KeyboardButton('ПТ')
        btn6 = types.KeyboardButton('Назад')
        btn7 = types.KeyboardButton('Cегодня')
        btn8 = types.KeyboardButton('Завтра')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.chat.id, Friday1groupup , reply_markup=markup) #ответ бота
        
    elif group == 2 and week== 2:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('ПН')
        btn2 = types.KeyboardButton('ВТ')
        btn3 = types.KeyboardButton('СР')
        btn4 = types.KeyboardButton('ЧТ')
        btn5 = types.KeyboardButton('ПТ')
        btn6 = types.KeyboardButton('Назад')
        btn7 = types.KeyboardButton('Cегодня')
        btn8 = types.KeyboardButton('Завтра')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.from_user.id, Friday2groupdown , reply_markup=markup) #ответ бота

    elif group == 1 and week== 2:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('ПН')
        btn2 = types.KeyboardButton('ВТ')
        btn3 = types.KeyboardButton('СР')
        btn4 = types.KeyboardButton('ЧТ')
        btn5 = types.KeyboardButton('ПТ')
        btn6 = types.KeyboardButton('Назад')
        btn7 = types.KeyboardButton('Cегодня')
        btn8 = types.KeyboardButton('Завтра')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.from_user.id, Friday1groupdown , reply_markup=markup) #ответ бота
        
@bot.message_handler(func=lambda message: message.text == 'Назад')
def back(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Из 1 группы')
    btn2 = types.KeyboardButton('Из 2 группы')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "Из какой ты группы?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Cегодня')
def back(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
    btn1 = types.KeyboardButton('ПН')
    btn2 = types.KeyboardButton('ВТ')
    btn3 = types.KeyboardButton('СР')
    btn4 = types.KeyboardButton('ЧТ')
    btn5 = types.KeyboardButton('ПТ')
    btn6 = types.KeyboardButton('Назад')
    btn7 = types.KeyboardButton('Cегодня')
    btn8 = types.KeyboardButton('Завтра')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
    bot.send_message(message.from_user.id, "В данный момент в разработке", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Завтра')
def back(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
    btn1 = types.KeyboardButton('ПН')
    btn2 = types.KeyboardButton('ВТ')
    btn3 = types.KeyboardButton('СР')
    btn4 = types.KeyboardButton('ЧТ')
    btn5 = types.KeyboardButton('ПТ')
    btn6 = types.KeyboardButton('Назад')
    btn7 = types.KeyboardButton('Cегодня')
    btn8 = types.KeyboardButton('Завтра')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
    bot.send_message(message.from_user.id, "В данный момент в разработке", reply_markup=markup)  

bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть
