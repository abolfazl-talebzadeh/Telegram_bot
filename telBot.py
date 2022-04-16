from email.policy import default
from math import floor
from platform import release
from re import A
from select import select
import string
from turtle import update
import Cons as c
from telegram.ext import *
import telegram as t
import responses as R

class TimeSlots:
    taken = False
    def __init__(self, frm, to):
        self.frm = frm
        self.to = to
    def take(self):
        self.take = True
    def release(self):
        self.take = False
    def send_name(self):
        output = str(self.frm)+" تا "+str(self.to)
        return list(output)


def to_time(tm):
    if tm/10 == 0:
        if tm%10 == 50:
            return str(0)+str(0)+":"+str(30)
        else:
            return str(0)+str(0)+":"+str(0)+str(0)
    else:
        if tm%10 == 5:
            return str(floor(tm/10))+":"+str(30)
        else:
            return str(floor(tm/10))+":"+str(0)+str(0)


slots = []
roja = []
mehdi = []

for i in range (150,225, 15):
    roja.append(TimeSlots(frm=to_time(i), to=to_time(i+15)))
    mehdi.append(TimeSlots(frm=to_time(i), to=to_time(i+15)))


def start_command(update: t.Update, context:CallbackContext):
    b = [[t.KeyboardButton("انتخاب مربی")]]
    context.bot.send_message(chat_id=update.effective_chat.id,
     text= "به سامانه رزرواسیون آکادمی تنیس داریوش خوش آمدید!",
     reply_markup = t.ReplyKeyboardMarkup(b, resize_keyboard = True))


def handle_keyboard(update: t.Update, context:CallbackContext):
    match update.message.text:
        case "انتخاب مربی":
            b = [[t.KeyboardButton("رُجا شهاب")], [t.KeyboardButton("مهدی  علی آبادی")]]
            context.bot.send_message(chat_id=update.effective_chat.id,
             text= "لطفا مربی مورد نظر خود را انتخاب نمائید",
              reply_markup = t.ReplyKeyboardMarkup(b, resize_keyboard = True))

        case "رُجا شهاب":
            b = []
            for tm in roja:
                temp = []
                temp.append(t.KeyboardButton(tm.to + " تا " + tm.frm))
                b.append(temp)
            context.bot.send_message(chat_id=update.effective_chat.id,
             text= "لطفا بازه زمانی مورد نظر خود را انتخاب کنید",
              reply_markup = t.ReplyKeyboardMarkup(b, resize_keyboard = True))


def main():

    updater = Updater(c.TOKEN_HEY, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(MessageHandler(Filters.text, handle_keyboard))

    updater.start_polling(3)
    updater.idle()


main()
