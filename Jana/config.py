class Config(object):
    LOGGER = True
    API_ID =21189715 
    API_HASH = "988a9111105fd2f0c5e21c2c2449edfd"
    TOKEN = ""  
    OWNER_ID=7225660023
    
    SUPPORT_CHAT = "Friend_Chat_International" 
    START_IMG = "https://files.catbox.moe/tre76f.jpg"
    EVENT_LOGS = (-1002341427688)
    MONGO_DB_URI= ""
   
    DATABASE_URL = ""  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        "8SOSKTRI0KPL"
    )
    TIME_API_KEY = "https://timezonedb.com/api"

    
    BL_CHATS = [] 
    DRAGONS = []
    DEV_USERS = []  
    DEMONS = [] 
    TIGERS = []  
    WOLVES = [] 

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
