import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Logging setup
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# --- CONFIGURATION ---
TOKEN = '8696533472:AAG7BuPoSNMfYwZbFzntXZsNIW79MwwX41M'
# Yahan apna GitHub Pages wala link lazmi dalein
MINI_APP_URL = 'https://inayatalikalhoro.github.io/YTallvideodownloaderbot/' 

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome!\n\nMain video downloader bot hoon. "
        "Bas kisi bhi video ka link bhejein aur main usse download karne mein madad karunga."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_url = update.message.text
    
    if user_url.startswith("http"):
        # Mini App Button
        keyboard = [
            [InlineKeyboardButton("📥 Download Video (Ad)", web_app=WebAppInfo(url=MINI_APP_URL))]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(
            "🎥 Video processed! Click karein aur ad dekh kar link hasil karein:",
            reply_markup=reply_markup
        )
    else:
        await update.message.reply_text("Meherbaani karke valid URL (link) bhejein.")

def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("Bot is starting...")
    app.run_polling()

if __name__ == '__main__':
    main()