from config import bot
from telebot.types import Message, CallbackQuery
import keyboards,texts
import wikipediaapi


wiki_wiki = wikipediaapi.Wikipedia(
    user_agent='NeuroLink',
    language='ru'
)


Excluded_commands = ['📝Text AI','🎨Image AI','🔊Voice AI','🧠Smart AI','📝CheckInWiki', '💬FeedBack', '📚Information']
@bot.message_handler(commands=['start'])
def start_message(message: Message):
    bot.send_message(message.chat.id, texts.Welcome_message, reply_markup=keyboards.get_main_keyboard())

@bot.message_handler(func=lambda message :message.text == '📝Text AI')
def text_message(message: Message):
    bot.send_message(message.chat.id, texts.Select_ai_text, reply_markup=keyboards.get_inline_keyboard_text())

@bot.message_handler(func=lambda message :message.text == '🎨Image AI')
def image_message(message: Message):
    bot.send_message(message.chat.id, texts.Select_ai_image, reply_markup=keyboards.get_inline_keyboard_image())

@bot.message_handler(func=lambda message :message.text == '🔊Voice AI')
def voice_message(message: Message):
    bot.send_message(message.chat.id, texts.Select_ai_voice, reply_markup=keyboards.get_inline_keyboard_voice())

@bot.message_handler(func=lambda message :message.text == '🧠Smart AI')
def smart_message(message: Message):
    bot.send_message(message.chat.id, texts.Select_ai_smart, reply_markup=keyboards.get_inline_keyboard_smart())

@bot.message_handler(func=lambda message :message.text == '🌐CheckInWiki')
def text_message(message: Message):
    bot.send_message(message.chat.id, texts.WikiText, reply_markup=keyboards.get_inline_keyboard_wiki())

@bot.message_handler(func=lambda message :message.text == '💬FeedBack')
def feedback_message(message: Message):
    bot.send_message(message.chat.id, texts.Feedback_m)

@bot.message_handler(func=lambda message :message.text == '📚Information')
def information_message(message: Message):
    bot.send_message(message.chat.id, texts.Information)

@bot.message_handler(
    func=lambda message:(
        message.text is not None and
        message.text.split()[0] not in Excluded_commands
), content_types =['text'])
def handle_message(message):
    search_res = wiki_wiki.page(message.text)
    if search_res.exists():
        bot.reply_to(message, search_res.canonicalurl)
    else:
        bot.reply_to(message, 'Страница не найдена')
    


@bot.callback_query_handler(func=lambda call: True)
def handler_inline_buttom_click(call:CallbackQuery):
    data = call.data
    if data == 'test':
        bot.send_message(call.message.chat.id, 'Нажата inline кнопка!')
    bot.answer_callback_query(call.id)
if __name__ == "__main__":
    bot.polling(non_stop=True)