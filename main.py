import os
import telebot
from datetime import datetime

token = "507470053:AAGjEdZI0J2M55Mr7nUQVrqc7496ZuMDGM0"
bot = telebot.TeleBot(token)
print("Bot started!")


def log(message, answer):
    print("\n=============")
    print(datetime.now())
    print("Message from {0} {1} (id={2}) \nText: {3}".format(message.from_user.first_name,
                                                             message.from_user.last_name,
                                                             str(message.from_user.id),
                                                             message.text))
    print(answer)


@bot.message_handler(commands=['start'])
def handle_text(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row("/start", "/stop")
    user_markup.row("меню", "акции", "помощь")
    bot.send_message(message.from_user.id,
                     "Добро пожаловать\nВыберите интересующий Вас пункт меню", reply_markup=user_markup)


@bot.message_handler(commands=['stop'])
def handle_text(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, ". . .", reply_markup=hide_markup)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if(message.text == 'меню'):
        user_markup = telebot.types.ReplyKeyboardMarkup(True)
        user_markup.row("/start", "/stop")
        user_markup.row("мясные блюда", "блюда из рыбы")
        user_markup.row("сэндвичи", "десерты", "напитки")
        bot.send_message(message.from_user.id, "Меню", reply_markup=user_markup)
    elif message.text == 'акции':
        answer = "акций нет, но вы держитесь\nвам всего доброго, хорошего настроения и здоровья"
        bot.send_message(message.chat.id, answer)
        log(message, answer)
    elif message.text == 'помощь':
        answer = "хелпа в гугле, ищите в яндексе, маил-ответы помогут!"
        bot.send_message(message.chat.id, answer)
        log(message, answer)
    elif message.text == 'мясные блюда':
        answer = "http://coub.com/view/awj6j"
        bot.send_message(message.chat.id, answer)
        log(message, answer)
    elif message.text == 'блюда из рыбы':
        answer = "https://coub.com/view/113r6t"
        bot.send_message(message.chat.id, answer)
        log(message, answer)
    elif message.text == 'напитки':
        answer = open("C:/Users/user/Documents/projects/test_bot/files/menu/9_nama.gif", "rb")
        bot.send_chat_action(message.from_user.id, 'upload_document')
        bot.send_document(message.chat.id, answer)
        log(message, answer)
        answer.close()


bot.polling(none_stop=True)
