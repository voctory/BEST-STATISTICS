import discord
from discord.ext import commands

import asyncio
import json

# load config file
with open('config.json') as data_file:
    data = json.load(data_file)

def get_prefix(bot, message):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

    # Notice how you can use spaces in prefixes. Try to keep them simple though.
    prefixes = ['!']

    # Check to see if we are outside of a guild. e.g DM's etc.
    if not message.guild:
        # Only allow ? to be used in DMs
        return '!'

    # If we are in a guild, we allow for the user to mention us or use any of the prefixes in our list.
    return commands.when_mentioned_or(*prefixes)(bot, message)

# set prefix
client = commands.Bot(command_prefix=get_prefix, description='Quizset.')

# load cogs
extensions = ['cogs.help',
              'cogs.error_handler',
              'cogs.owner',
              'cogs.psat']

# checks for owner perms
def ownerPerms(ctx):
    return ctx.message.author.id in data["owners"]

# triggered when bot is logged in
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='BESTSTATISTICS.XYZ', type=1, url='https://twitch.tv/kraken'))
    print('Bot online.')


# something to do with cogs
if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extension, error))

# login
client.run(data["discord"])
