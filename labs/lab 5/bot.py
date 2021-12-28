import telebot
from telebot import types
from config import get_path
import config
import dbworker


# Создание бота
bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def cmd_start(message):
    dbworker.set(dbworker.make_key(message.chat.id, config.SENTENCE), '')
    bot.send_message(message.chat.id, 'Сейчас будем решать, что бы выбрать из обуви.')
    dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_FIRST_WORD.value)
    bot.send_message(message.chat.id, 'Вам нужно каждый раз выбирать один вариант из предложенных.')
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    ibtn1 = types.KeyboardButton('Я женщина')
    ibtn2 = types.KeyboardButton('Я мужчина')
    ibtn3 = types.KeyboardButton('Я не определился/определилась')
    markup.add(ibtn1, ibtn2, ibtn3)
    bot.send_message(message.chat.id, 'Выберете один из трех вариантов:', reply_markup=markup)


@bot.message_handler(commands=['reset'])
def cmd_reset(message):
    dbworker.set(dbworker.make_key(message.chat.id, config.SENTENCE), '')
    bot.send_message(message.chat.id, 'Начнем сначала!')
    dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_FIRST_WORD.value)
    bot.send_message(message.chat.id, 'Вам нужно каждый раз выбирать один вариант из предложенных.')
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    ibtn1 = types.KeyboardButton('Я женщина')
    ibtn2 = types.KeyboardButton('Я мужчина')
    ibtn3 = types.KeyboardButton('Я не определился/определилась')
    markup.add(ibtn1, ibtn2, ibtn3)
    bot.send_message(message.chat.id, 'Выберете один из трех вариантов:', reply_markup=markup)


@bot.message_handler(func=lambda message: dbworker.get(dbworker.make_key(message.chat.id, config.CURRENT_STATE)) == config.States.STATE_FIRST_WORD.value)
def first_word(message):
    text = message.text
    if text=="Я женщина":
        dbworker.set(dbworker.make_key(message.chat.id, config.States.STATE_FIRST_WORD), 0)
    elif text=="Я мужчина":
        dbworker.set(dbworker.make_key(message.chat.id, config.States.STATE_FIRST_WORD), 1)
    elif text=="Я не определился/определилась":
        dbworker.set(dbworker.make_key(message.chat.id, config.States.STATE_FIRST_WORD), 2)
    else:
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        ibtn1 = types.KeyboardButton('Я женщина')
        ibtn2 = types.KeyboardButton('Я мужчина')
        ibtn3 = types.KeyboardButton('Я не определился/определилась')
        markup.add(ibtn1, ibtn2, ibtn3)
        bot.send_message(message.chat.id, 'Выберете один из трех вариантов:', reply_markup=markup)
        return
    dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_SECOND_WORD.value)
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    ibtn1 = types.KeyboardButton('Шнурки')
    ibtn2 = types.KeyboardButton('Молния')
    markup.add(ibtn1, ibtn2)
    bot.send_message(message.chat.id, 'Выберете вариант застежки:', reply_markup=markup)


# Обработка второго числа
@bot.message_handler(func=lambda message: dbworker.get(dbworker.make_key(message.chat.id, config.CURRENT_STATE)) == config.States.STATE_SECOND_WORD.value)
def second_word(message):
    text = message.text
    if text=="Молния":
        dbworker.set(dbworker.make_key(message.chat.id, config.States.STATE_SECOND_WORD), 0)
    elif text=="Шнурки":
        dbworker.set(dbworker.make_key(message.chat.id, config.States.STATE_SECOND_WORD), 1)
    else:
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        ibtn1 = types.KeyboardButton('Молния')
        ibtn2 = types.KeyboardButton('Шнурки')
        markup.add(ibtn1, ibtn2)
        bot.send_message(message.chat.id, 'Выберете вариант застежки:', reply_markup=markup)
        return
    dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_THIRD_WORD.value)
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    ibtn1 = types.KeyboardButton('Белый')
    ibtn2 = types.KeyboardButton('Коричневый')
    ibtn3 = types.KeyboardButton('Черный')
    markup.add(ibtn1, ibtn2, ibtn3)
    bot.send_message(message.chat.id, 'Выберете только один из предложенных трех цветов:', reply_markup=markup)


@bot.message_handler(func=lambda message: dbworker.get(dbworker.make_key(message.chat.id, config.CURRENT_STATE)) == config.States.STATE_THIRD_WORD.value)
def third_word(message):
    text = message.text
    if text=="Белый":
        dbworker.set(dbworker.make_key(message.chat.id, config.States.STATE_THIRD_WORD), 0)
    elif text=="Коричневый":
        dbworker.set(dbworker.make_key(message.chat.id, config.States.STATE_THIRD_WORD), 1)
    elif text=="Черный":
        dbworker.set(dbworker.make_key(message.chat.id, config.States.STATE_THIRD_WORD), 2)
    else:
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        ibtn1 = types.KeyboardButton('Белый')
        ibtn2 = types.KeyboardButton('Коричневый')
        ibtn3 = types.KeyboardButton('Черный')
        markup.add(ibtn1, ibtn2, ibtn3)
        bot.send_message(message.chat.id, 'Выберете только один из предложенных трех цветов:', reply_markup=markup)
        return
    dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_SENTENCE.value)
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    ibtn1 = types.KeyboardButton('38')
    ibtn2 = types.KeyboardButton('39')
    ibtn3 = types.KeyboardButton('40')
    ibtn4 = types.KeyboardButton('41')
    markup.add(ibtn1, ibtn2, ibtn3, ibtn4)
    bot.send_message(message.chat.id, 'Ваш размер ноги:', reply_markup=markup)


@bot.message_handler(func=lambda message: dbworker.get(dbworker.make_key(message.chat.id, config.CURRENT_STATE)) == config.States.STATE_SENTENCE.value)
def again(message):
    text = message.text
    gender=dbworker.get(dbworker.make_key(message.chat.id, config.States.STATE_FIRST_WORD))
    type=dbworker.get(dbworker.make_key(message.chat.id, config.States.STATE_SECOND_WORD))
    color=dbworker.get(dbworker.make_key(message.chat.id, config.States.STATE_THIRD_WORD))
    path=get_path(gender,type,color)
    bot.send_message(message.chat.id, f' Итог: размер ноги "{text}"')
    img = open(path, 'rb')
    bot.send_photo(message.chat.id, img)
    bot.send_message(message.chat.id, 'Можем попробовать еще раз!')
    bot.send_message(message.chat.id, 'Вам нужно каждый раз выбирать один вариант из предложенных.')
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    ibtn1 = types.KeyboardButton('Я женщина')
    ibtn2 = types.KeyboardButton('Я мужчина')
    ibtn3 = types.KeyboardButton('Я не определился/определилась')
    markup.add(ibtn1, ibtn2, ibtn3)
    bot.send_message(message.chat.id, 'Выберете один из трех вариантов:', reply_markup=markup)
    dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_FIRST_WORD.value)
        


if __name__ == '__main__':
    #if os.path.exists('db.vdb'): os.remove('db.vdb')
    bot.infinity_polling() #работа без остановок
