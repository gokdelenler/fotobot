from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "73251b7458f360ace1c92adaf8d8ac16")
      API_ID = int(getenv("API_ID", 0))      
      BOT_TOKEN = getenv("BOT_TOKEN", "16203874147:AAEh1UW1oEGNyj9dYl5YoR__cYM3m6CySgM")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1001528088004").replace("\n", " ").split(' '))
