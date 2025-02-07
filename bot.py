import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("¡Hola! Soy un bot de Telegram. ¿En qué puedo ayudarte?")

async def echo(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(f"Me dijiste: {update.message.text}")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Iniciar el bot
    print("Bot en ejecución...")
    app.run_polling()

if __name__ == '__main__':
    main()
