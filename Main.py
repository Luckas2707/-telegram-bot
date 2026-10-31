import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Olá! 👋\n\n"
        "Bem-vindo ao nosso VIP.\n"
        "Em breve você poderá conhecer os planos "
        "e realizar sua assinatura por aqui."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Use /start para iniciar o bot."
    )


def main():
    if not TOKEN:
        raise RuntimeError("Configure a variável TELEGRAM_BOT_TOKEN")

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("Bot iniciado!")
    app.run_polling()


if __name__ == "__main__":
    main()
