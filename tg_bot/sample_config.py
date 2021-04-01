if not __name__.endswith("sample_config"):
    import sys
    print("The README is there to be read. Extend this sample config to a config file, don't just rename and change "
          "values here. Doing that WILL backfire on you.\nBot quitting.", file=sys.stderr)
    quit(1)


# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "YOUR KEY HERE"
    OWNER_ID = "YOUR OWNER ID" 
    OWNER_USERNAME = "akhilbaiju"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'sqldbtype://username:pw@hostname:port/db_name'  
    MESSAGE_DUMP = None 
    LOAD = []
    NO_LOAD = ['translation', 'rss']
    WEBHOOK = False
    URL = None

 
    SUDO_USERS = []  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = []  
    WHITELIST_USERS = []  
    DONATION_LINK = None  
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  
    STRICT_GBAN = False
    WORKERS = 8  
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg' 
    ALLOW_EXCL = False  # Allow ! commands as well as /


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
