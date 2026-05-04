import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Logging setup
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# --- CONFIGURATION ---
TOKEN = '8696533472:AAG7BuPoSNMfYwZbFzntXZsNIW79MwwX41M'
MINI_APP_URL = 'https://inayatalikalhoro.github.io/YTallvideodownloaderbot/' 

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to All Video Downloader!\n\n"
        "I can help you download videos. "
        "Just send me any video link (YouTube, TikTok, FB, etc.) to get started."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_url = update.message.text
    
    if user_url.startswith("http"):
        keyboard = [
            [InlineKeyboardButton("📥 Download Video (Ad)", web_app=WebAppInfo(url=MINI_APP_URL))]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(
            "🎥 Video processed! Click the button below, "
            "watch a short ad, and get your download link:",
            reply_markup=reply_markup
        )
    else:
        await update.message.reply_text("Please send a valid video URL (starting with https://)")

def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("Bot is starting... Press Ctrl+C to stop.")
    app.run_polling()

if __name__ == '__main__':
    main()
