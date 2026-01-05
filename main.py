import telebot
from telebot import types
from telebot.types import KeyboardButton
from background import keep_alive

bot = telebot.TeleBot('8385124271:AAH-N_nO3KZdZywCmWqyeCfTT6WdLra07NI')

channel_1='@love_kirov'
channel_2='@l_lotus_s_life'

@bot.message_handler(commands=['start'])
def start(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn=KeyboardButton('Получить ссылку')
    markup.add(btn)
    bot.send_message(message.from_user.id, """Привет! 

Для получения ссылки на предложение постов подпишитесь на эти каналы:


1 - https://t.me/love_kirov 
2 - https://t.me/l_lotus_s_life""", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def check_channel(message):
    if message.text=='Получить ссылку':
        userid=message.from_user.id
        try:
            chat_member1=bot.get_chat_member(channel_1, userid)
            chat_member2=bot.get_chat_member(channel_2, userid)
            if chat_member1.status!='left' and chat_member2.status!='left':
                bot.send_message(message.from_user.id, 'https://t.me/anonaskbot?start=XRBjQDW4C__KL59')
            else:
                bot.send_message(message.from_user.id, 'Похоже, вы не подписаны на канал. Пожалуйста, подпишитесь)))')
        except Exception as e:
            bot.send_message(message.from_user.id, f'Произошла ошибка {e}')

keep_alive()
bot.polling(none_stop=True, interval=0)
