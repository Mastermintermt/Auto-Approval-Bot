# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "20919286"))
    API_HASH = getenv("API_HASH", "57b85f72104db3f08f9795b0410eb556")
    BOT_TOKEN = getenv("BOT_TOKEN", "6703431319:AAHxEROYg4Vj156OmoG2IJ4qZ8TjV1TJ1Sk")
    FSUB = getenv("FSUB", "AgsModsOG")
    CHID = int(getenv("CHID", "-1002124243193"))
    SUDO = list(map(int, getenv("SUDO", "6976445947").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://sasikumaris010:sasikumaris010@cluster0.tiplcqn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
