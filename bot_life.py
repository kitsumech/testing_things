#!/usr/local/bin/python3.9

import discord
from discord.ext import commands
import os
import random

client = commands.Bot(command_prefix="!")
token = os.getenv("DISCORD_BOT_TOKEN")

@client.event
async def on_ready() :
  await client.change_presence(status = discord.Status.idle, activity = discord.Game("Whatchu want?"))

@client.command()
  async def ping(ctx) :
    await ctx.send(f"🏓 Pong with {str(round(client.latency, 2))}")

@client.command(name="whoami")
  async def whoami(ctx) :
    await ctx.send(f"You are {ctx.message.author.name}")

@client.command(name="blue")
  async def blue(ctx):
    await ctx.channel.send('https://thumbs.gfycat.com/AromaticZestyArawana-mobile.mp4')

@client.command(name"jcvd")
async def jean_claude(ctx):
response =[
'https://i.giphy.com/media/FBzqZGthkW6KQ/giphy.webp',
'https://media1.tenor.com/images/dfca4ee97f5db1598fae289f11f0c7b1/tenor.gif',
'https://i.giphy.com/media/l41m2FGXBx5GqjOjm/giphy.webp',
]
await ctx.send(random.choice(response))

@client.command()
async def clear(ctx, amount=3) :
    await ctx.channel.purge(limit=amount)


client.run(token)
