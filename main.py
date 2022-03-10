import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, KeyboardButton

from prayertime import times
from region import region_name, cities

API_TOKEN = '5237281522:AAHm6bHs3Oq3GEstDTWXaeuu-_BTuWYCG_Q'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
count = 0
buttons = ReplyKeyboardMarkup()
for btn in region_name:
  if count<3:
    buttons.insert(KeyboardButton(btn))
  elif 3<=count<6:
    buttons.insert(KeyboardButton(btn))
  elif 6<=count<9:
    buttons.insert(KeyboardButton(btn))
  elif 9<=count<12:
    buttons.insert(KeyboardButton(btn))
  elif 12<=count<15:
    buttons.insert(KeyboardButton(btn))
  else:
    buttons.add(KeyboardButton(btn))
  count+=1


@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
  user_name = msg.from_user.first_name
  await msg.answer(f"Assalomu alaykum va rahmatullohi va barakotuh  {user_name}")
  await msg.answer(f"O'z shahringizni tanlang 👇", reply_markup=buttons)
  


@dp.message_handler()
async def send_message(msg: types.Message):
  try:
    index = region_name.index(msg.text)
    time = times(cities[index])
    text = msg.text
    await msg.answer(
      f"/*/*//{text}dagi namoz vaqtlari//*/*/ \n\n🕒 Tong: {time['Imsak']}\n🕔 Bomdod: {time['Fajr']}\n🕔 Quyosh chiqishi: {time['Sunrise']}\n🕐 Peshin: {time['Dhuhr']}\n🕓 Asr: {time['Asr']}\n🕔 Quyosh botishi: {time['Sunset']}\n🕕 Shom: {time['Maghrib']}\n🕢 Xuftom: {time['Isha']}\n🕛 Yarim tun: {time['Midnight']}\n"
    )
  except:
    await msg.answer(f"{msg.from_user.first_name}  Xato so'z kiritdingiz!\nIltimos tugmalardan birini tanlang! 👇")



if __name__ == '__main__':
  executor.start_polling(dp,skip_updates=True)