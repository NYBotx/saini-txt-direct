#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "24720215"))
API_HASH = environ.get("API_HASH", "c0d3395590fecba19985f95d6300785e")
BOT_TOKEN = environ.get("BOT_TOKEN", "7735683292:AAFhYEPnSBL63JFHx_Wpn1wNcfLIL69A6WA")
OWNER = int(environ.get("OWNER", "7910994767"))
CREDIT = "𝄟⃝‌🐬🇳‌ɪᴋʜɪʟ𝄟⃝🐬"
AUTH_USER = os.environ.get('AUTH_USERS', '7910994767').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
