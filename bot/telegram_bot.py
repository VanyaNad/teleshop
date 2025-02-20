from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
from django.conf import settings


async def start(update: Update, _context: CallbackContext) -> None:
    """Handles the /start command"""
    await update.message.reply_text(settings.BOT_WELCOME_MESSAGE)


def setup_bot() -> Application:
    """Sets up the bot with command handlers"""
    app = Application.builder().token(settings.TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    return app
