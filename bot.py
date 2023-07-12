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


@bot.slash_command(description='Get the current weather', name='current')
async def get_weather(interaction: nextcord.Interaction, query: str):
    data = await get_weather_data(query)
    embed = make_embed(data)
    is_hidden = embed.title == 'Invalid Request'
    await interaction.response.send_message(embed=embed, ephemeral=is_hidden)


if __name__ == '__main__':
    bot.run(TOKEN)
