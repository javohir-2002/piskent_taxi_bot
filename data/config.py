from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")

GROUP_ID = env.str("GROUP_ID")
CHANNEL_ID = env.str("CHANNEL_ID")
ADMINS = env.list("ADMINS")
IP = env.str("ip")
