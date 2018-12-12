import discord
from discord.ext import commands

from datetime import datetime

import asyncio
import json

import random
import math

score_val = {
    "PSAT": { "values": [320, 1520], "thumbnail": "https://i.imgur.com/N4rTVUh.jpg"},
    "IQ": { "values": [50, 160], "thumbnail": "https://i.imgur.com/5KXh7kE.jpg?1"}
}

class scores:
    def __init__(self, client):
        self.client = client

    @commands.command(name='psat', aliases=["PSAT"], pass_context=True)
    async def psat(self, ctx):
        if len(ctx.message.mentions) == 0: await ctx.send("", embed = workflow(ctx.message.author.id, "PSAT"))
        else: await ctx.send("", embed = workflow(ctx.message.mentions[0].id, "PSAT"))

    @commands.command(name='iq', aliases=["IQ"], pass_context=True)
    async def iq(self, ctx):
        if len(ctx.message.mentions) == 0: await ctx.send("", embed = workflow(ctx.message.author.id, "IQ"))
        else: await ctx.send("", embed = workflow(ctx.message.mentions[0].id, "IQ"))


# streamlined <o/
def workflow(user_id, type):
    user_new(user_id, type)
    return gen_embed(user_id, get_score(user_id, type), type)

# check if user is in d a t a b a s e
def user_new(user_id, type):
    with open(f'data/{type}.json') as data_file:
        sets = json.load(data_file)

    # adding new dict if user isn't already there
    if str(user_id) not in list(sets):
        sets[str(user_id)] = score_eq(type)
        with open(f'data/{type}.json', 'w') as file:
            file.write(json.dumps(sets))
    else:
        # user was in!
        return

# special use cases, looking to implement with score_val later
def score_eq(type) :
    if type == "PSAT": return int(math.ceil(random.randint(score_val[type]["values"][0], score_val[type]["values"][1]) / 10.0)) * 10
    else: return random.randint(score_val[type]["values"][0], score_val[type]["values"][1])

# retrieve top secret scores
def get_score(user_id, type):
    with open(f'data/{type}.json') as data_file:
        sets = json.load(data_file)

    # returns score
    return sets[str(user_id)]


def gen_embed(user_id, score, type):

    embed = discord.Embed(title=f'{type} Score',
        description=f'<@{user_id}>\'s {type} score is **{score}**.',
        color=discord.Colour.from_rgb(random.randint(0,255), random.randint(0,255), random.randint(0,255)))

    embed.set_footer(text="Everyone has a score.")
    embed.set_thumbnail(url=score_val[type]["thumbnail"])

    return embed

def setup(client):
    client.add_cog(scores(client))
