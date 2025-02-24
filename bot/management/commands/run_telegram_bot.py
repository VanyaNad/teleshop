import asyncio
from django.core.management.base import BaseCommand
from bot.telegram_bot import setup_bot
from teleshop import settings


class Command(BaseCommand):
    help = "Run the Telegram bot"

    def handle(self, *args, **kwargs):
        app = setup_bot()  # Get bot instance
        self.stdout.write(self.style.SUCCESS(settings.BOT_IS_RUNNING))
        asyncio.run(app.run_polling())