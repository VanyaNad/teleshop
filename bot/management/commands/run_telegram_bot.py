from django.core.management.base import BaseCommand
from bot.telegram_bot import setup_bot
from django.conf import settings


class Command(BaseCommand):
    help = "Run the Telegram bot"

    def handle(self, *args, **kwargs):
        updater = setup_bot()
        self.stdout.write(self.style.SUCCESS(settings.BOT_IS_RUNNING))
        updater.start_polling()
        updater.idle()
