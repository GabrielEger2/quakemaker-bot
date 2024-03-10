from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_BOT_TOKEN")

intents: Intents = Intents.default()
intents.message_content = True # NOQA
client: Client = Client(intents=intents)

async def send_response(message: Message, user_message: str) -> None:
    if not user_message:
        print("User message is empty")
        return
    
    try:
        response: str = await get_response(message)
        await message.channel.send(response)
    except Exception as e:
        print(f"Error: {e}")

@client.event
async def on_ready() -> None:
    print(f"{client.user} has connected to Discord!")

@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    
    if not message.content.startswith('!'):
        return
    
    username: str = str(message.author)
    user_message: str = message.content[1:] 
    channel: str = str(message.channel)

    print(f"User: {username} | Message: {user_message} | Channel: {channel}")

    await send_response(message, user_message)

def main() -> None:
    client.run(token=TOKEN)

if __name__ == "__main__":
    main()