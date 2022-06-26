from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("5507826675:AAEmWM8ucYmX9g6zUNTuOA6OMBmKOwhfhn4",
				use_context=True)


def start(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Hello sir, Welcome to the Rocking_Programming_Youtube_Channel Bot.Please write\
		/help to see the commands_available.")

def help(update: Update, context: CallbackContext):
	update.message.reply_text("""Available Commands :-
	/youtube - To get the youtube Channel  URL
	/gmail - To get gmail URL
	/LatestVideo - New Video [Latest_video] Rocking_Programming_Youtube Channel
    /Payment_Info - Please Support Us !
    /Feedback_Form - Feedback Form for Customer Support
    
    """)


def gmail_url(update: Update, context: CallbackContext):
	update.message.reply_text(
		"manubhardwaj881990@gmail.com")


def youtube_url(update: Update, context: CallbackContext):
	update.message.reply_text("https://www.youtube.com/channel/UCcO4kRJAupUsPzfD6zGYVCg")


def Feedback_url(update: Update, context: CallbackContext):
	update.message.reply_text(
		"https://forms.gle/m3R9yDMiHrs7YKKc6")

def Latest_Video(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Latest_Video => https://www.youtube.com/watch?v=VYbB2xBB2_4&t=4s")
def Payment_Details(update: Update, context: CallbackContext):
	update.message.reply_text(
		"https://drive.google.com/file/d/1TuBGNHV8D97zh-VrbFR0_gOJ8KqxxZdR/view?usp=sharing \ UPI ID gtspay@apl")
    

def unknown(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry '%s' is not a valid command" % update.message.text)


def unknown_text(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry I can't recognize you , you said '%s'" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('Feedback_Form', Feedback_url))
updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url))
updater.dispatcher.add_handler(CommandHandler('LatestVideo', Latest_Video))
updater.dispatcher.add_handler(CommandHandler('Payment_Info', Payment_Details))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
	Filters.command, unknown)) # Filters out unknown commands

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
