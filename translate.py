# Import necessary modules
import telebot  
from telebot import types  
from googletrans import Translator  
from langdetect import detect  

# Instantiate the bot with your token
bot = telebot.TeleBot('токен бота') 

# Instantiate Google Translate's Translator
translator = Translator() 

# Dictionary to hold user's language choice. The key will be the user's chat id and the value will be the chosen language.
user_language = {} 

# Mapping from language names to their respective ISO code that googletrans uses
language_dict = {'english': 'en', 'russian': 'ru', 'french': 'fr', 'spanish': 'es'} 

# Function to handle '/start' command. It sends a keyboard with language options to the user.
@bot.message_handler(commands=['start'])  
def send_welcome(message):  
    # Create inline keyboard
    markup = types.ReplyKeyboardMarkup(row_width=2)  
    itembtn1 = types.KeyboardButton('English')  
    itembtn2 = types.KeyboardButton('Russian')  
    itembtn3 = types.KeyboardButton('Spanish')  
    itembtn4 = types.KeyboardButton('French')  
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)  
    # Send message with inline keyboard
    bot.reply_to(message, "Пожалуйста, выберите язык для перевода:", reply_markup=markup)  

# Function to process incoming messages
@bot.message_handler(func=lambda m: True)  
def translate_message(message):  
    global user_language 
    try:  
        # Detect source language of message
        src = detect(message.text)

        # Check if message is a language selection
        dest_lang = message.text.lower() 
        if dest_lang not in ['english', 'russian', 'french', 'spanish']:  
            # If not a language selection, translate the message
            if message.chat.id in user_language: 
                dest_lang = user_language[message.chat.id] 
            else: 
                dest_lang = 'en' # Default language 
            translated_text = translator.translate(message.text, src=src, dest=language_dict[dest_lang]).text  
            bot.reply_to(message, translated_text)  
        else:  
            # If it's a language selection, update the user's language preference
            user_language[message.chat.id] = dest_lang  
            bot.reply_to(message, f"Язык был установлен на {dest_lang.capitalize()}")  
    except Exception as e:  
        # Print the exception and send error message to the user
        print(str(e)) 
        bot.reply_to(message, "Упс, произошла ошибка при переводе. Пожалуйста, попробуйте еще раз.")  

# Run bot
if __name__ == "__main__":  
    bot.polling(none_stop=True)
