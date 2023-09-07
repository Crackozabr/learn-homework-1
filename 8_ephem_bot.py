"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
from datetime import datetime
import settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}
"""
  Для того, чтобы пользователю не пришлось вспоминать, 
  дадим ему знать, какие планеты знает библиотека ephem:
  ephem._libastro.builtin_planets()

  Интересуют первые 10 кортежей списка: 8 планет, Луна, Солнце
  И то, что в кортеже на втором месте 'Planet'
  [(0, 'Planet', 'Mercury'),
  (1, 'Planet', 'Venus'),
  (2, 'Planet', 'Mars'),
  (3, 'Planet', 'Jupiter'),
  (4, 'Planet', 'Saturn'),
  (5, 'Planet', 'Uranus'),
  (6, 'Planet', 'Neptune'),
  (7, 'Planet', 'Pluto'),
  (8, 'Planet', 'Sun'),
  (9, 'Planet', 'Moon'),
  (10, 'PlanetMoon', 'Phobos'),
  Добавим пользователю подсказку при вызове /start со списком планет
"""


def greet_user(update, context):
    
    list_of_planets = ephem._libastro.builtin_planets()
    planet_list = []
    for planets in list_of_planets:
        if planets[1] == 'Planet':
            planet_list.append(planets[2])
    print(planet_list)
    text = "Этот бот может определить " \
    "в каком созвездии сегодня " \
    "находится указанная планета\n\n" \
    "Нужно отправить боту команду /planet c указанием названии планеты.\n" \
    "Например так '/planet Mars'\n" \
    "Планеты (и не только), которые известны боту:\n"
    text += ", ".join(planet_list)
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def define_constellation(update, context):
    planet = update.message.text.split()[1]
    class_name = getattr(ephem, planet)
    class_call = class_name()
    class_call.compute(datetime.today().strftime('%Y/%m/%d'))
    text = f'Планета {planet} сегодня в созвездии {ephem.constellation(class_call)[1]}'
    print(text)
    update.message.reply_text(text)



def main():
    # mybot = Updater("КЛЮЧ, КОТОРЫЙ НАМ ВЫДАЛ BotFather", request_kwargs=PROXY, use_context=True)
    mybot = Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", define_constellation))

    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
