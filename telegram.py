import telethon
import connect

# Ce programme ecoute le channel telegram

TELEGRAM_API_HASH = ">>ici le API hash récupéré<<"
TELEGRAM_API_ID = 000000 # ici_un_entier_sans_guillemets
TELEGRAM_SCALP_SHORT_ID = 00000000 # demande dans le chan ... 

client = telethon.TelegramClient("ika_scalp_helper", TELEGRAM_API_ID, TELEGRAM_API_HASH)

# See: https://docs.telethon.dev/en/latest/basic/updates.html
@client.on(telethon.events.NewMessage(chats=TELEGRAM_SCALP_SHORT_ID))
async def incoming_msg(event):
    if "BNF" in event.raw_text:
        try:
            a, b, *rest = event.raw_text.split("-")
            pair, *rest = b.split(" ")
            # print("TXT: ", event.raw_text)
            print(f"PAIR: {pair}")
            connect.scalp_helper(pair)
        except Exception as ex:
            print(f"ERR: {ex}")


if __name__ == "__main__":
    print(f"En écoute sur le channel Telegram {TELEGRAM_SCALP_SHORT_ID}")
    print("---")    

    client.start()
    client.run_until_disconnected()
