# - *- coding: utf- 8 - *-
import config

import telebot
from telebot import types

import pyowm

bot = telebot.TeleBot("1115942099:AAHiS44VTAXAyDzfgLBnuRosggEU38x_Jjk")
owm = pyowm.OWM("2332ad963bdf036dda9efdf814f954bf", language = "UA")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = owm.weather_at_place(message.text)
	w = observation.get_weather()
	temp = w.get_temperature('celsius')["temp"]
	wind = w.get_wind()["speed"]


	answer = "В місті/селі " + message.text + " зараз " + w.get_detailed_status() + "\n" + "Швидксть вітру: " + str(wind) +" м/с"+ "\n"
	answer += "Температура в районі " + str(temp) + "°C" + "\n\n"

	if temp < -20:
		answer +="Раджу тобі не виходити на вулицю без потреби, сьогодні дужееее холодно \n Хорошого дня =)"
	elif temp < -10:
		answer +="Сьогодні дуже холодно, раджу тобі дуже добре вдягатися \n Хорошого дня =)"
	elif temp < 0:
		answer +="Сьогодні морозно, раджу вдягти теплу куртку \n Хорошого дня =)"
	elif temp < 10:
		answer +="Сьогодні холодно, вдягнись потепліше \n Хорошого дня =)"
	elif temp < 20:
		answer +="Сьогодні тепленько, але на всякий випадок одягни щось =D \n Хорошого дня =)"
	else: 
		answer +="Сьогодні на дворі супер, можеш одянатися як хочеш \n Хорошого дня =)"

	bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True, interval=0 )