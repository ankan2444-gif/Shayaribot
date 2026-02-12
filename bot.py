import requests
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)

BOT_TOKEN = "8564296670:AAEn_1e6wVpbRZ6K8YsiYPeovXOTsUgV2XI"
API_URL = "https://fast-dev-apis.vercel.app/shayari"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌸 Welcome to Shayari Bot 🌸\n\n"
        "👉 /shayari likho aur ek nayi shayari pao 💖"
    )


async def shayari(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        response = requests.get(API_URL, timeout=10)
        data = response.json()

        # Shayari extract (safe way)
        shayari_text = (
            data.get("shayari")
            or data.get("data")
            or data.get("quote")
            or "❌ Shayari nahi mil payi"
        )

        await update.message.reply_text(
            f"✨ Shayari ✨\n\n{shayari_text}"
        )

    except Exception as e:
        await update.message.reply_text(
            "⚠️ API error aa gaya, baad me try karo."
        )


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("shayari", shayari))

    print("✅ Shayari Bot Running...")
    app.run_polling()


if __name__ == "__main__":
    main()