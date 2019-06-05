import logging
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters)
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
level=logging.INFO)

logger = logging.getLogger(__name__)

boto = ChatBot('Chat_Bot')

trainer = ChatterBotCorpusTrainer(boto)
trainer.train("chatterbot.corpus.portuguese")

def start(bot, update):
    update.message.reply_text('Oi')

def help(bot, update):
    update.message.reply_text('Oh!')

def echo(bot, update):
    pergunta = update.message.text
    resposta = boto.get_response(pergunta)
    if float(resposta.confidence) > 0.5:
        update.message.reply_text(str(resposta))
    else:
        update.message.reply_text('Ainda não sei responder esta pergunta')

def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)

def main():
    updater = Updater('770069679:AAEb3EG5cu_UJBYNrzGEK41tiyo-ECRJmbw')
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
