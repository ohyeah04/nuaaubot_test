import telebot

bot = telebot.TeleBot('')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Button1', 'Button2 hello2')

@bot.message_handler(commands=['start'])

def start_message(message):
    bot.send_message(message.chat.id, 'hi there now i will show u menu', reply_markup=keyboard1)

bot.polling()