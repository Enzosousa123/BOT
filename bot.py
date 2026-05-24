from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TELEGRAM_TOKEN = "8770603181:AAFDbg1posWrZZYJbK_faSVVVatENtCFnnc"

SCRIPT = """🎉 Seja muito bem-vindo(a)! Assista ao vídeo acima e tenha um gostinho do que está por vir! 🔥👆🏻

🔸 Conteúdos organizados por hashtags pra você achar tudo fácil
🔸 Downloads liberados
🔸 Mais de 70 MIL mídias postadas
🔸 Novidades todos os dias – sempre atualizadas
🔐 100% sigiloso e confidencial – sua privacidade é prioridade!

🚨 É confiável?
✔️ Mais de 1.000 membros ativos no VIP
✔️ Suporte disponível 24 horas pra te ajudar no que precisar

Entre agora e tenha acesso ao melhor, de forma segura, organizada e sem limites! 💥
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    # Video 1
    await context.bot.send_video(
        chat_id=chat_id,
        video=open("video1.mp4", "rb")
    )

    # Texto
    await context.bot.send_message(
        chat_id=chat_id,
        text=SCRIPT
    )

    # Video 2
    await context.bot.send_video(
        chat_id=chat_id,
        video=open("video2.mp4", "rb")
    )

    # Botones
    botones = [
        [InlineKeyboardButton("🔆 Diário por R$12,90", callback_data="diario")],
        [InlineKeyboardButton("💎 Acesso VIP + Ocultos por R$15,93 (10% OFF)", callback_data="vip")],
        [InlineKeyboardButton("👑 Vitalício + Ocultos 🔐 por R$27,90 (10% OFF)", callback_data="vitalicio")]
    ]

    await context.bot.send_message(
        chat_id=chat_id,
        text="👇 Selecione uma opção:",
        reply_markup=InlineKeyboardMarkup(botones)
    )

async def botones_respuesta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat.id

    if query.data == "diario":
        await context.bot.send_photo(
            chat_id=chat_id,
            photo=open("pagamento.jpeg", "rb"),
            caption="99f07a5a-a32f-401e-be5a-b225f58231dd"
        )
        await context.bot.send_message(
            chat_id=chat_id,
            text="⚠️ mandar comprovante (se nao sem acesso)"
        )

    elif query.data == "vip":
        await context.bot.send_photo(
            chat_id=chat_id,
            photo=open("pagamento.jpeg", "rb"),
            caption="99f07a5a-a32f-401e-be5a-b225f58231dd"
        )
        await context.bot.send_message(
            chat_id=chat_id,
            text="⚠️ mandar comprovante (se nao sem acesso)"
        )

    elif query.data == "vitalicio":
        await context.bot.send_photo(
            chat_id=chat_id,
            photo=open("pagamento.jpeg", "rb"),
            caption="99f07a5a-a32f-401e-be5a-b225f58231dd"
        )
        await context.bot.send_message(
            chat_id=chat_id,
            text="⚠️ mandar comprovante (se nao sem acesso)"
        )

app = Application.builder().token(TELEGRAM_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(botones_respuesta))

print("Bot encendido...")
app.run_polling()