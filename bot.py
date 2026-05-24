from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TELEGRAM_TOKEN = "TU_TOKEN_AQUI"
ADMIN_ID = 8261186165

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

    # Aviso al admin
    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=f"✅ Alguien inició el bot\nChat ID: {chat_id}"
    )

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

    if query.data == "diario":
        texto = "🔆 Acesso diário por R$12,90"

    elif query.data == "vip":
        texto = "💎 Acesso VIP + Ocultos por R$15,93 (10% OFF)"

    elif query.data == "vitalicio":
        texto = "👑 Acesso Vitalício + Ocultos 🔐 por R$27,90 (10% OFF)"

    else:
        texto = "Opção inválida."

    await context.bot.send_photo(
        chat_id=query.message.chat_id,
        photo=open("pagamento.jpeg", "rb"),
        caption=texto
    )

async def recibir_mensaje(update: Update, context: ContextTypes.DEFAULT_TYPE):
    usuario = update.effective_user
    chat_id = update.effective_chat.id
    mensaje = update.message.text

    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=f"""📩 Nuevo mensaje

👤 Usuario: @{usuario.username}
🆔 Chat ID: {chat_id}
💬 Mensaje: {mensaje}

Para responder:
/responder {chat_id} tu mensaje"""
    )

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return

    if len(context.args) < 2:
        await update.message.reply_text(
            "Uso correcto:\n/responder CHAT_ID mensaje"
        )
        return

    chat_id = int(context.args[0])
    mensaje = " ".join(context.args[1:])

    await context.bot.send_message(
        chat_id=chat_id,
        text=mensaje
    )

    await update.message.reply_text("✅ Mensaje enviado.")

async def miid(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Tu ID es: {update.effective_user.id}"
    )

app = Application.builder().token(TELEGRAM_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("responder", responder))
app.add_handler(CommandHandler("miid", miid))

app.add_handler(CallbackQueryHandler(botones_respuesta))

app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, recibir_mensaje)
)

print("Bot encendido...")
app.run_polling()
