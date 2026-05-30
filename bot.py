from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8384208978:AAG5AgV2RpCIckco7xfq3Wg2xO0BEqsVxPs"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Бот распределения промоутеров запущен."
    )

from telegram.request import HTTPXRequest

request = HTTPXRequest(
    proxy_url="socks5://127.0.0.1:9050"
)

app = (
    Application.builder()
    .token(TOKEN)
    .request(request)
    .connect_timeout(30)
    .read_timeout(30)
    .write_timeout(30)
    .build()
)
app.add_handler(CommandHandler("start", start))

print("Бот запущен")
app.run_polling()

