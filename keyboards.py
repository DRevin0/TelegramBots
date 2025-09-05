from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
import wikipediaapi
def get_main_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(

        KeyboardButton('🧠Smart AI'),
        KeyboardButton('🎨Image AI'),
        KeyboardButton('🔊Voice AI'),
        KeyboardButton('📝Text AI'),
        KeyboardButton('📚Information'),
        KeyboardButton('💬FeedBack'),

        KeyboardButton('🌐CheckInWiki')
    )
    return keyboard
def get_inline_keyboard_smart():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton('DeepSeek', url= 'https://chat.deepseek.com/'),
        InlineKeyboardButton('GigaChat', url= 'https://giga.chat/'),
        InlineKeyboardButton('ChatGPT', url= 'https://chatgpt.com/'),
        InlineKeyboardButton('GitHub Models', url= 'https://github.com/marketplace/models')
    )
    return keyboard
def get_inline_keyboard_image():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton('Шедеврум', url= 'https://shedevrum.ai/'),
    )
    return keyboard
def get_inline_keyboard_text():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton('DeepAI', url= 'https://deepai.org/'),
        InlineKeyboardButton('QuillBot', url= 'https://quillbot.com/'),
        InlineKeyboardButton('ChatInfo', url= 'https://chatinfo.ru/'),
    )
    return keyboard
def get_inline_keyboard_voice():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton('Narakeet', url= 'https://www.narakeet.com/'),
        InlineKeyboardButton('Robivox', url= 'https://robivox.ru/'),
        InlineKeyboardButton('TextSpeech', url='https://textspeechmp3.com/')
    )
    return keyboard

def get_inline_keyboard_wiki():
    keyboard = InlineKeyboardMarkup()
    keyboard.add()
    return keyboard
