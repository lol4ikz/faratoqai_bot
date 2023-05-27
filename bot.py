import os
import logging
import telegram
from telegram import ForceReply, Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TELGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.text in ("Kalaisyn Fara?", "Калайсын Фара?"):
        user = update.effective_user
        await update.message.reply_html(
            rf"Jaksy alhamdulillah {user.mention_html()}!",
            reply_markup=ForceReply(selective=True),
        )

if __name__ == '__main__':
    application = ApplicationBuilder().token(TELGRAM_BOT_TOKEN).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    application.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND, echo))

    application.run_polling()
