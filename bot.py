import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Logging setup to track bot status in the console
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    level=logging.INFO
)

# --- CONFIGURATION ---
# Your official Bot Token
TOKEN = '8696533472:AAG7BuPoSNMfYwZbFzntXZsNIW79MwwX41M'

# Your GitHub Pages URL (where index.html is hosted)
MINI_APP_URL = 'https://inayatalikalhoro.github.io/YTallvideodownloaderbot/' 

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Sends a welcome message when the command /start is issued."""
    await update.message.reply_text(
        "👋 Welcome to All Video Downloader!\n\n"
        "I can help you download videos from various platforms. "
        "Just send me any video link (YouTube, TikTok, Facebook, etc.) to get started."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Processes the video link sent by the user."""
    user_url = update.message.text
    
    if user_url.startswith("http"):
        # Inline button that opens the Telegram Mini App (with your Ads)
        keyboard = [
            [InlineKeyboardButton("📥 Download Video (Unlock)", web_app=WebAppInfo(url=MINI_APP_URL))]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(
            "🎥 Video link received! Click the button below, "
            "watch a short ad to support us, and get your download link:",
            reply_markup=reply_markup
        )
    else:
        await update.message.reply_text("❌ Invalid link. Please send a valid URL starting with https://")

def main():
    """Starts the bot."""
    # Building the application
    app = Application.builder().token(TOKEN).build()
    
    # Adding command and message handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("Bot is starting... (English Version)")
    print("Check your Telegram bot now.")
    
    # Using poll_interval to reduce pressure on PythonAnywhere's free proxy
    app.run_polling(poll_interval=2.0)

if __name__ == '__main__':
    main()
