import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "3334521")

API_HASH = os.environ.get("API_HASH", "29edd7420d528140c7a04bd47486886f")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

FORCE_SUB = os.environ.get("FORCE_SUB", "ary_backup") 

DB_NAME = os.environ.get("DB_NAME","ary_botz")     

DB_URL = os.environ.get("DB_URL","")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5079629749').split()]

PORT = os.environ.get('PORT', '8080')
