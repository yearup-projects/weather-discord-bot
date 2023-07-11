import discord
from discord import Embed
from datetime import datetime


def make_embed(data):
    temp_f = data['current']['temp_f']
    location = data['location']['name']
    region = data['location']['region']
    epoch = data['current']['last_updated_epoch']
    desc = data['current']['condition']['text']
    img_url = f"https:{data['current']['condition']['icon']}"

    embed = Embed(title=f'{temp_f}ºF',
                  description=desc,
                  timestamp=datetime.fromtimestamp(epoch),
                  color=discord.Color.blue())

    embed.set_thumbnail(url=img_url)

    embed.add_field(name='Location',
                    value=f'{location}, {region}',
                    inline=False)

    return embed
