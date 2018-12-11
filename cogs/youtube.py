import discord
from discord.ext import commands

from datetime import datetime

import asyncio
import json

import random
import math

class PSAT:
    def __init__(self, client):
        self.client = client

    @commands.command(name='pewdiepie', aliases=["pewd", "pewds"], pass_context=True)
    async def psat(self, ctx):

        if len(ctx.message.mentions) == 0:
            # send score
            await ctx.send("", embed = workflow(ctx.message.author.id))

        else:
            # take id of the first user
            await ctx.send("", embed = workflow(ctx.message.mentions[0].id))

# streamlined <o/
def workflow(user_id):
    user_new(user_id)
    return gen_embed(user_id, get_score(user_id))

# check if user is in d a t a b a s e
def user_new(user_id):
    with open('data/psat.json') as data_file:
        sets = json.load(data_file)

    # adding new dict if user isn't already there
    if str(user_id) not in list(sets):
        sets[str(user_id)] = int(math.ceil(random.randint(320, 1520) / 10.0)) * 10
        with open('data/psat.json', 'w') as file:
            file.write(json.dumps(sets))
    else:
        # user was in!
        return

# retrieve top secret scores
def get_score(user_id):
    with open('data/psat.json') as data_file:
        sets = json.load(data_file)

    # returns score
    return sets[str(user_id)]

def gen_embed(user_id, score):

    embed = discord.Embed(title='PSAT Score',
        description=f'<@{user_id}>\'s PSAT score is **{score}**.',
        color=discord.Colour.from_rgb(random.randint(0,255), random.randint(0,255), random.randint(0,255)))

    embed.set_footer(text="Everyone has a score.")
    embed.set_thumbnail(url="https://i.imgur.com/N4rTVUh.jpg")

    return embed

def setup(client):
    client.add_cog(PSAT(client))
