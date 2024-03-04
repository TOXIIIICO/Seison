from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID","20551716"))
API_HASH = getenv("API_HASH","564355da021dc5739c01f33fb015eaf1")

BOT_TOKEN = getenv("BOT_TOKEN","6222040155:AAEba5H1vEFNFhke5N_grG-DrGspEf4elUA")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://mohamedhelal:mohamedhelal@cluster0.qhhuj2p.mongodb.net/?retryWrites=true&w=majority")

OWNER_ID = int(getenv("OWNER_ID", 6753126490))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/O_A_H2")
