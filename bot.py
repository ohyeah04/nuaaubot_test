import telebot

bot = telebot.TeleBot('1252501384:AAGodt4oSf6X6EzvwyZr7ux265dKHve3NOo')

## main menu
mainmenu = telebot.types.ReplyKeyboardMarkup(True, True)
mainmenu.row('Online Orientation Week 2020')
mainmenu.row('Fall 2020 Online')
mainmenu.row('Important Policies, Procedures and other Information')
mainmenu.row('Meet your advisor!', 'Meet your peer Advisor!')
mainmenu.row('SSH', 'SEDS', 'SMG', 'SOM')
mainmenu.row('UG Academic Calendar', 'UG Academic Handbook')
mainmenu.row('WOrking Hours', 'Contact US')
mainmenu.row('Faculty Rooms', 'Other Contacts', 'FAQs')

## orientation 2020
orientation2020 = telebot.types.ReplyKeyboardMarkup(True, True)
orientation2020.row('Orientation Schedule and Other Info')
orientation2020.row('AAU Orientation Schedule')
orientation2020.row('Registration Dates', 'Registration Tips')
orientation2020.row('Registration Process FAQ')
orientation2020.row('First-Year Checklist')
orientation2020.row('Go Back')

## online fall
onlinesemester = telebot.types.ReplyKeyboardMarkup(True, True)
onlinesemester.row('Online Office of the Registrar Services')
onlinesemester.row('Electives')
onlinesemester.row('Go Back')

## important policies
importantinfo = telebot.types.ReplyKeyboardMarkup(True, True)
importantinfo.row('Good academic standing')
importantinfo.row('Registration Policies', 'Grading System', 'Stipend')
importantinfo.row('Majors, Minors and Internal Transfers', 'Deans List')
importantinfo.row('GPA and CGPA Calculation', 'Change and Appeal of Grade')
importantinfo.row('Leave of Absence', 'Dismissla and Withdrawal')
importantinfo.row('Attendance', 'Degree Completion Requirements')
importantinfo.row('Examination', 'Mid-Semester and Final Gradeds Submission')
importantinfo.row('Transfer redits form Outside University and NUFYP', 'Re-Admission')
importantinfo.row('Go Back')

## meet ur advisor
meeturadvisor = telebot.types.ReplyKeyboardMarkup(True, True)
meeturadvisor.row('Almira Zholamanova')
meeturadvisor.row('Beknur Karagul', 'Aikerim Daurenbayeva')
meeturadvisor.row('Nargiza Aitpayeva', 'Aina Nurtanova')
meeturadvisor.row('Go Back')

## meet ur peeradvisor
meeturpeer = telebot.types.ReplyKeyboardMarkup(True, True)
meeturpeer.row('Lazzat (4-year, Economics)', 'Aliya (4-year PSIR)')
meeturpeer.row('Dana (4-year Economics)', 'Kamila (4-year Sociology)')
meeturpeer.row('Assel (3-year Economics)', 'Dameliya (3-year WLLC)')
meeturpeer.row('Aigerim (3-year Economics', 'Inayat (3-year Biology')
meeturpeer.row('Alen (3-year Math)', 'Maxim (3-year Physics)')
meeturpeer.row('Go Back')

## ssh
ssh = telebot.types.ReplyKeyboardMarkup(True, True)
ssh.row('Mathematics','Economics')
ssh.row('Physics','Policical Science and International Relations')
ssh.row('Biology','Sociology')
ssh.row('Chemistry','Anthropology')
ssh.row('World Languages, Literature and Cultures','History')
ssh.row('Major Declaration Requirements')
ssh.row('Go Back')

## seds
seds = telebot.types.ReplyKeyboardMarkup(True, True)
seds.row('Chemical and Materials Engineering')
seds.row('Civil and Environmental Engineering')
seds.row('Electrical and Computer Engineering')
seds.row('Mechanical and Aerospace Engineering')
seds.row('Computer Science')
seds.row('Robotics and Mechatronics')
seds.row('Go Back')

## smg
smg = telebot.types.ReplyKeyboardMarkup(True, True)
smg.row('Geology')
smg.row('Mining Engineering')
smg.row('Petroleum Engineering')
smg.row('Go Back')

## som
som = telebot.types.ReplyKeyboardMarkup(True, True)
som.row('Nursing')
som.row('Go Back')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'hi there now i will show u menu', reply_markup=mainmenu)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Online Orientation Week 2020':
        bot.send_message(message.chat.id, 'orientation', reply_markup=orientation2020)
    elif message.text == 'Fall 2020 Online':
        bot.send_message(message.chat.id, 'fall is online lol', reply_markup=onlinesemester)
    elif message.text == 'Important Policies, Procedures and other Information':
        bot.send_message(message.chat.id, 'info', reply_markup=importantinfo)
    elif message.text == 'Meet your advisor!':
        bot.send_message(message.chat.id, 'Beknur is the best advisor', reply_markup=meeturadvisor)
    elif message.text == 'Meet your peer Advisor!':
        bot.send_message(message.chat.id, 'hello', reply_markup=meeturpeer)
    elif message.text == 'SSH':
        bot.send_message(message.chat.id, 'this is ssh', reply_markup=ssh)
    elif message.text == 'SEDS':
        bot.send_message(message.chat.id, 'this is seds', reply_markup=seds)
    elif message.text == 'SMG':
        bot.send_message(message.chat.id, 'this is smg', reply_markup=smg)
    elif message.text == 'SOM':
        bot.send_message(message.chat.id, 'this is som', reply_markup=som)
    elif message.text == 'UG Academic Calendar':
        bot.send_message(message.chat.id, 'this is academcalendar')
    elif message.text == 'UG Academic Handbook':
        bot.send_message(message.chat.id, 'this is ug handbook')
    elif message.text == 'WOrking Hours':
        bot.send_message(message.chat.id, 'wokrigng hrs')
    elif message.text == 'Contact US':
        bot.send_message(message.chat.id, 'contacts')
    elif message.text == 'Faculty Rooms':
        bot.send_message(message.chat.id, 'factulty?')
    elif message.text == 'Other Contacts':
        bot.send_message(message.chat.id, 'smth else')
    elif message.text == 'FAQs':
        bot.send_message(message.chat.id, 'questions?')
bot.polling()