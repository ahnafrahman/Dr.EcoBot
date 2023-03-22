import discord
from discord.ext import commands
from config import Token, API_KEY
import aiohttp

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("Dr. EcoBot has connected to Discord!")


@bot.command()
async def gpt(ctx: commands.Context, *, prompt: str):
    async with aiohttp.ClientSession() as session:
        payload = {
            "model": "text-davinci-003",
            "prompt": prompt,
            "temperature": 0.5,
            "max_tokens": 2000,
            "presence_penalty": 0,
            "frequency_penalty": 0,
            "best_of": 1,
        }
        headers = {
            "Authorization": f"Bearer {API_KEY}"
        }
        async with session.post("https://api.openai.com/v1/completions", json=payload, headers=headers) as resp:
            response = await resp.json()
            text_resp = response["choices"][0]["text"]
            embed = discord.Embed(
                title="Dr. Ecobot's Response:", description=f"```\n{text_resp}\n```")
            await ctx.reply(embed=embed)

bot.run(Token)

# import discord

# intents = discord.Intents.default()
# intents.message_content = True
# token = ''

# client = discord.Client(intents=intents)


# @client.event
# async def on_ready():
#     print("Dr. Ecobot has logged in as " + client)


# @client.event
# async def on_message(message):
#     username = str(message.author).split('#')[0]
#     user_message = str(message.content)
#     channel = str(message.channel.name)

#     print(username + "said" + user_message.lower() + "in" + channel)
#     # when user types anything into discord server, it says "this user said" in this discord channel

# client.run(token)
