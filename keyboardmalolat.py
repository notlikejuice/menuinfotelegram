from pyrogram import Client, filters
from pyrogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup,
                            InlineKeyboardButton)

API_ID = ''  # Wstaw tutaj swoje api_id
API_HASH = ''  # Wstaw tutaj swój api_hash
BOT_TOKEN = ''  # Wstaw tutaj token swojego bota

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_callback_query(filters.create(lambda _, __, query: query.data == 'reply_markup'))
def show_all_buttons(client, callback_query):
    """
    Wywołuje dużą tablicę przycisków po kliknięciu przycisku "POKAŻ WSZYSTKIE PRZYCISKI - 📒".
    """
    client.send_message(callback_query.message.chat.id, "Oto wszystkie przyciski:", reply_markup=start_keyboard)

@app.on_chat_member_updated()
def welcome_new_members(client, chat_member_updated):
    new_member = chat_member_updated.new_chat_member
    if new_member.status == "member":  # Nowy użytkownik dołączył do grupy
        client.send_message(chat_member_updated.chat.id, f"Witaj w grupie, {new_member.user.first_name}!")

@app.on_message(filters.command("start"))
def send_start(_, message):
    welcome_text = """
    Cześć z tej strony Marek.Jestem tworem sztucznej inteligencji. 
    Wszystko tutaj to fikcja.Jeśli jesteś z policji,służb specjalnych lub tudzież 60 ❌.
    Chciałbym poinformować Cię że obrazy na tym kanale są przypadkowe stworzone przez AI.
    Osoby, miejsca czy wpisy to generator losowych słów.
    Kliknij /menu aby sprawdzić czy coś w trawie piszczy.
    """
    app.send_message(message.chat.id, welcome_text)

# Inline Keyboard Markup dla komendy /start
@app.on_message(filters.command("help"))
def send_help(_, message):
    help_text = """
    Bot służy jako tablica ogłoszeniowa. Kliknij w dolny przycisk to ujrzysz ją w całej okazałości.
    """
    help_keyboard = InlineKeyboardMarkup(   
        inline_keyboard=[   
        [InlineKeyboardButton(text="POKAŻ WSZYSTKIE PRZYCISKI - 📒", callback_data='reply_markup'),]
        ]              
    )
    app.send_message(message.chat.id, help_text, reply_markup=help_keyboard)

    
start_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="REGULAMIN - 📒", url="https://telegra.ph/REGULAMIN-04-14"),
         InlineKeyboardButton(text="ZDJĘCIA - 📸", url="https://telegra.ph/ZDJ%C4%98CIA-04-14")],
        [InlineKeyboardButton(text="LEGIT - ✅", url="https://telegra.ph/LEGIT-04-14-2"),
         InlineKeyboardButton(text="MIASTA - 🌇", url="https://telegra.ph/MIASTA-04-14")],
        [InlineKeyboardButton(text="GEOSKRYTKI - 🗺", url="https://telegra.ph/GEOSKRYTKI-04-14"),
         InlineKeyboardButton(text="InPost - ✈️", url="https://telegra.ph/InPost-04-14")],
        [InlineKeyboardButton(text="WSPÓŁPRACA - 1️⃣", url="https://telegra.ph/1WSP%C3%93%C5%81PRACA1-04-14"),
         InlineKeyboardButton(text="WSPÓŁPRACA - 2️⃣", url="https://telegra.ph/2WSP%C3%93%C5%81PRACA2-04-14")],
        [InlineKeyboardButton(text="@ArsenW3nger- 📞", url="https://t.me/@ArseneW3nger")],
        [InlineKeyboardButton(text="@zloto_milczenie- 📞", url="https://t.me/@zloto_milczenie")]
    ]
)


@app.on_message(filters.command("menu"))
def send_menu(_, message):
    """
    Wysyła klawiaturę inline po wpisaniu lub kliknięciu /menu.
    """
    message.reply_text("Wybierz jedną z opcji:", reply_markup=start_keyboard)
    
@app.on_message(filters.command("dev"))
def send_dev(_, message):
    dev_message = """
        Wysyła klawiaturę inline po wpisaniu lub kliknięciu /dev.
        """
    app.send_message(message.chat.id, dev_message)

app.run()  # Uruchamia bota