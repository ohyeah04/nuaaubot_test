import telebot

bot = telebot.TeleBot('1252501384:AAGodt4oSf6X6EzvwyZr7ux265dKHve3NOo')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row(['Online Orientation Week 2020'])


@bot.message_handler(commands=['start'])

def start_message(message):
    bot.send_message(message.chat.id, 'hi there now i will show u menu', reply_markup=keyboard1)

bot.polling()