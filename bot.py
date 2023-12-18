import telebot
from telebot import types

TOKEN = '6081435766:AAHhe5mz8Os9kW9piTNptza0kh2XdauVt_w'

bot = telebot.TeleBot(TOKEN)





@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.text == 'Отчетность продюсеров':
        markup = types.ReplyKeyboardMarkup()
        bot.send_message(message.chat.id, 'https://docs.google.com/forms/d/e/1FAIpQLSdyOxPKe_9JdpNIvIp9RTms5FWMYm7OvJtuDyKaA1G5pnJBeA/viewform')
        back = types.KeyboardButton('Назад')
        markup.add(back)

        bot.send_message(message.chat.id, 'Заполни форму')

    elif message.text == 'Регламент продюсера':
        markup = types.ReplyKeyboardMarkup()
        file = open('./1.png', 'rb')
        bot.send_photo(message.chat.id, file, reply_markup=markup)
        back = types.KeyboardButton('Назад')
        markup.add(back)

        bot.send_message(message.chat.id, 'Запомни ее наизусть ))')

    elif message.text == 'Адреса склада и офиса':
        markup = types.ReplyKeyboardMarkup()
        item1 = types.KeyboardButton('Склад')
        item2 = types.KeyboardButton('Офис')
        markup.add(item1, item2)
        back = types.KeyboardButton('Назад')
        markup.add(back)

        bot.send_message(message.chat.id, 'Выбери что тебя интересует', reply_markup=markup)

    elif message.text == 'Склад':
        markup = types.ReplyKeyboardMarkup()
        bot.send_message(message.chat.id, '3-й Михалковский переулок, 15')

        bot.send_message(message.chat.id, 'Нажми назад', reply_markup=markup)

    elif message.text == 'Офис':
        markup = types.ReplyKeyboardMarkup()
        bot.send_message(message.chat.id, 'Бутлерова, 17Б')

        bot.send_message(message.chat.id, 'Нажми назад', reply_markup=markup)

    elif message.text == 'Доп материал':
        markup = types.ReplyKeyboardMarkup()
        item1 = types.KeyboardButton('Памятка работы на проектах')
        markup.add(item1)
        #item2 = types.KeyboardButton('Логистика и бюджет')
        #markup.add(item2)
        item3 = types.KeyboardButton('Памятка по заявочному плану')
        markup.add(item3)

        back = types.KeyboardButton('Назад')

        markup.add(back)

        bot.send_message(message.chat.id, 'Выбери что тебя интересует', reply_markup=markup)

    elif message.text == 'Памятка по заявочному плану':
        markup = types.ReplyKeyboardMarkup()
        file = open('./p3.png', 'rb')
        bot.send_photo(message.chat.id, file, reply_markup=markup)

        bot.send_message(message.chat.id, 'Освежил память, нажми назад ))', reply_markup=markup)

    elif message.text == 'Памятка работы на проектах':
        markup = types.ReplyKeyboardMarkup()
        file = open('./122.pdf', 'rb')
        bot.send_document(message.chat.id, file, reply_markup=markup)

        bot.send_message(message.chat.id, 'Нажми назад', reply_markup=markup)


    #elif message.text == 'Логистика и бюджет':
    #    markup = types.ReplyKeyboardMarkup()
    #    file = open('./1233.png', 'rb')
     #   bot.send_photo(message.chat.id, file, reply_markup=markup)

    #    bot.send_message(message.chat.id, 'Нажми назад', reply_markup=markup)





    elif message.text == 'Камерапланы':
        markup = types.ReplyKeyboardMarkup()
        item1 = types.KeyboardButton('ФНЛ. Первая лига')
        markup.add(item1)
        item2 = types.KeyboardButton('ФНЛ. Вторая лига')
        markup.add(item2)
        back = types.KeyboardButton('Назад')
        markup.add(back)

        bot.send_message(message.chat.id, 'Выбери что тебя интересует', reply_markup=markup)

    elif message.text == 'ФНЛ. Первая лига':
        markup = types.ReplyKeyboardMarkup()
        bot.send_message(message.chat.id, 'https://drive.google.com/drive/folders/12pQkVU_q3ppMD4VcI4pnwmdcAieUPGe5?usp=share_link')

        bot.send_message(message.chat.id, 'Если не нашел что искал вернись назад, напиши менеджеру', reply_markup=markup)

    elif message.text == 'ФНЛ. Вторая лига':
        markup = types.ReplyKeyboardMarkup()
        bot.send_message(message.chat.id, 'https://drive.google.com/drive/u/0/folders/1Y19FuTLV2teJk_F4ltfc4CvY83no3S49')

        bot.send_message(message.chat.id, 'Если не нашел что искал вернись назад, напиши менеджеру', reply_markup=markup)


    elif message.text == 'Обратная связь':
        markup = types.ReplyKeyboardMarkup()
        bot.send_message(message.chat.id, 'https://t.me/Maks_Gushin')

        bot.send_message(message.chat.id, 'Свяжись с ним, надеюсь он поможет ))', reply_markup=markup)

    elif message.text == 'Саппорт':
        markup = types.ReplyKeyboardMarkup()
        bot.send_message(message.chat.id, 'https://t.me/Vsporte_Support')

        bot.send_message(message.chat.id, 'Пиши им, всегда на связи ))', reply_markup=markup)


    elif message.text == 'Компенсация':

        markup = types.ReplyKeyboardMarkup()
        bot.send_message(message.chat.id, 'https://docs.google.com/forms/d/e/1FAIpQLSfznc49oGRoRfPUp8JA5wgL7nT_keQquv7TrCY_0gJPkEafcA/viewform')

        bot.send_message(message.chat.id, 'Заполни форму', reply_markup=markup)




    elif message.text == 'Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        item1 = types.KeyboardButton('Отчетность продюсеров')
        markup.row(item1)
        item2 = types.KeyboardButton('Регламент продюсера')
        markup.row(item2)
        item3 = types.KeyboardButton('Адреса склада и офиса')
        item4 = types.KeyboardButton('Камерапланы')
        item8 = types.KeyboardButton('Контакты')
        markup.add(item8)
        item5 = types.KeyboardButton('Доп материал')
        item6 = types.KeyboardButton('Обратная связь')
        item7 = types.KeyboardButton('Саппорт')
        markup.row(item6, item7)
        item8 = types.KeyboardButton('Компенсация')
        markup.add(item8)
        markup.row(item3, item4, item5)

        bot.send_message(message.chat.id, 'Выбери то, что тебя  интересует', reply_markup=markup)


   

    


bot.polling(none_stop=True)
