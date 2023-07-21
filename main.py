from config import API_ID, API_HASH, SESSIONS
from pyrogram import Client, idle


CLIENTS = []

for SESSION in SESSIONS:
    if SESSION:
        client = Client(
            session_name=SESSION,
            api_id=API_ID,
            api_hash=API_HASH,
            plugins=dict(root="CoDeX"),
        )
        CLIENTS.append(client)


if __name__ == "__main__":

    for i, CLIENT in enumerate(CLIENTS):
        try:
            CLIENT.start()
            CLIENT.join_chat("Heart_Connection")
            CLIENT.join_chat("Heart_Connection")
            print(f"---> Client {i+1} has been Started...")
        except Exception as e:
            print(e)

    print("🔥💫𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐃𝐞𝐩𝐥𝐨𝐲𝐞𝐝 𝐔𝐬𝐞𝐫𝐁𝐨𝐭❌ 𝐌𝐘_𝐌𝐀𝐒𝐓𝐄𝐑--⚡🇨Ⓞ𝗗𝜩🇽⚡")
    idle()
