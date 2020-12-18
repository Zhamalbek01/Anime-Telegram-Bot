#!/usr/bin/python
# -*- coding: utf-8 -*-

import telebot
from telebot import types

bot = telebot.TeleBot('1480009927:AAFtUUu5AgNJtR0hK-HUMrQCktZFdp2s3VQ')

@bot.message_handler(commands=['website'])
def open_website(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton("Перейти на сайт", url="https://yummyanime.club/"))
	bot.send_message(message.chat.id,
			"Отличный выбор, нажмите на кнопку ниже и начинайте смотреть аниме прямо сейчас",
			parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['start'])
def start(message):
    sti = open('static/sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Каталог аниме')
    btn2 = types.KeyboardButton('Связь с разработчиком')
    btn3 = types.KeyboardButton("Что такое аниме?")
    markup.add(btn1, btn2, btn3)
    send_mess = f"<b>Привет {message.from_user.first_name} {message.from_user.last_name}</b>!\nЕсли хотите смотреть аниме нажми на кнопку или напиши мне название"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=["text"])
def mess(message):
    s_mess = ""
    if message.text == "Каталог аниме":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        url_btn1 = types.InlineKeyboardButton(text="Топ - 100", url="https://yummyanime.club/top")
        url_btn2 = types.InlineKeyboardButton(text="Наруто: Ураганные хроники", url="https://yummyanime.club/catalog/item/naruto-uragannye-hroniki")
        url_btn3 = types.InlineKeyboardButton(text="Хантер Х Хантер", url="https://yummyanime.club/catalog/item/hanter-h-hanter")
        url_btn4 = types.InlineKeyboardButton(text="Тетрадь Смерти", url="https://yummyanime.club/catalog/item/tetrad-smerti")
        url_btn5 = types.InlineKeyboardButton(text="Семь смертных грехов", url="https://yummyanime.club/catalog/item/sem-smertnyh-grehov")
        url_btn6 = types.InlineKeyboardButton(text="Ванпанчмен", url="https://yummyanime.club/catalog/item/vanpanchmen")
        keyboard.add(url_btn1, url_btn2, url_btn3, url_btn4, url_btn5, url_btn6)
        bot.send_message(message.chat.id, "Каталог Аниме", parse_mode="html", reply_markup=keyboard)
    elif message.text == "Связь с разработчиком":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Связь с разработчиком", url="https://web.telegram.org/#/im?p=u594125416_11827481147258597021"))
        bot.send_message(message.chat.id, "Мой Телеграм Канал", parse_mode="html", reply_markup=markup)
    elif message.text == 'Что такое аниме?':
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("Виды и жанры аниме", callback_data='genre')
        markup.add(item1)
        s_mess = "Аниме́ — японская анимация. В отличие от мультфильмов других стран, предназначенных в основном для просмотра детьми, бо́льшая часть выпускаемого аниме рассчитана на подростковую и взрослую аудитории, и во многом за счёт этого имеет высокую популярность в мире."
        bot.send_message(message.chat.id, s_mess, parse_mode='html', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')

@bot.callback_query_handler(func=lambda call: True)
def cellback_inline(call):
    try:
        if call.message:
            if call.data == 'genre':
                mess = 'Виды и жанры аниме\n\nКодомо-аниме - аниме, предназначенное для детей.\nСёнэн-аниме - аниме, предназначенное для старших мальчиков и юношей (с 12 до 16-18 лет).\nСёдзё-аниме - аниме, предназначенное для старших девочек и девушек (с 12 до 16-18 лет).\nСэйнэн-аниме - аниме, предназначенное для молодых мужчин.\nДзё-аниме - аниме, предназначенное для молодых женщин.\nТВ-сериал - сериальное аниме, предназначенное для показа по телевидению.\nТВ-фильм - несериальное аниме, предназначенное для показа по телевидению.'
                bot.send_message(call.message.chat.id, mess)
    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)

