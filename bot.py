import os
from dotenv import load_dotenv
import nextcord
from nextcord.ext import commands
from weather import get_weather_data
from weather_embed import make_embed

load_dotenv()

TOKEN = os.getenv('DISCORD_KEY')
GUILDS = [int(guild) for guild in os.getenv('GUILDS').split(',')]

bot = commands.Bot()


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.slash_command(description='Get the current weather', name='current',
                   guild_ids=GUILDS)
async def get_weather(interaction: nextcord.Interaction, query: str):
    data = await get_weather_data(query)
    print(data)
    embed = make_embed(data)
    await interaction.response.send_message(embed=embed)


if __name__ == '__main__':
    bot.run(TOKEN)
