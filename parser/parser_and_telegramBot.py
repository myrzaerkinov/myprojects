import requests
from bs4 import BeautifulSoup as b
import random
import telebot

URL = 'https://www.anekdot.ru/last/good'
API_KEY = '5426927571:AAEaolCYvDp5dt3GHqgWEaGVS_jHgRaN7j8'

# something comment
# something comment 2
# something comment 3

def parser(url):
    """
    Вычисляется является ли парсером
    :param url:
    :return:
    """
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return [c.text for c in anekdots]

list_of_jokes = parser(URL)
random.shuffle(list_of_jokes)



bot = telebot.TeleBot(API_KEY)
@bot.message_handler(commands=['Начать'])

def hello(message):
    bot.send_message(message.chat.id, 'Привет! Чтобы посмеяться введите любую цифру: ')

@bot.message_handler(content_types=['text'])
def joke(message):
    if message.text.lower() in '123456789':
        bot.send_message(message.chat.id, list_of_jokes[0])
        del list_of_jokes[0]
    else:
        bot.send_message(message.chat.id, 'Введите любую цифру: ')

bot.polling()



