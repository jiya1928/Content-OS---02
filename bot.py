from dotenv import load_dotenv
load_dotenv()
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from automation import run_full_cycle
from hunter import hunter_agent
from brain import app_graph
from publisher import publisher

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 CONTENT OS 02 ONLINE\n\nCommands:\n/hunt - Top 5 viral topics\n/generate LinkedIn AI Agents - Instant content\n/post - Last content ko LinkedIn pe daal\n/auto - Full auto cycle chala"
    )

async def hunt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hunting...")
    data = hunter_agent()
    msg = "🔥 TOP 5 TODAY:\n\n"
    for i, t in enumerate(data["topics"], 1):
        msg += f"{i}. {t['topic']} [{t['virality']}/10]\n\n"
    await update.message.reply_text(msg)

async def generate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    topic = " ".join(context.args) if context.args else "AI Agents for Startups"
    await update.message.reply_text(f"Generating for: {topic}")
    result = app_graph.invoke({
        "topic": topic, "platform": "LinkedIn",
        "intent": "", "brand_voice": "", "research_data": "", "strategy": "",
        "hooks": [], "draft": "", "critique": "", "final_content": "",
        "hashtags": [], "score": 0, "iterations": 0, "seo_score": 0
    })
    final = result.get("final_content", "")[:3900]
    await update.message.reply_text(final)
    # Save for posting
    with open("last_generated.txt", "w", encoding="utf-8") as f:
        f.write(final)

async def post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        with open("last_generated.txt", "r", encoding="utf-8") as f:
            content = f.read()
        res = publisher.publish("linkedin", content)
        await update.message.reply_text(f"Done: {res}")
    except:
        await update.message.reply_text("Pehle /generate chala bhai")

async def auto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Full auto cycle start ho raha hai...")
    run_full_cycle()
    await update.message.reply_text("Cycle done. Check linkedin_drafts.txt")

def main():
    if not TELEGRAM_TOKEN:
        print("TELEGRAM_BOT_TOKEN .env me daal")
        return
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("hunt", hunt))
    app.add_handler(CommandHandler("generate", generate))
    app.add_handler(CommandHandler("post", post))
    app.add_handler(CommandHandler("auto", auto))
    print("Telegram Bot Online...")
    app.run_polling()

if __name__ == "__main__":
    main()