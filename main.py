import discord
import os
from discord.ext import commands, tasks
from itertools import cycle



TOKEN = 'USE YOURS'


intents = discord.Intents().default()
intents.members = True
client = commands.Bot(command_prefix= '!', intents=intents)
status = cycle(['I am here to help!',
                '!help',
                'Failure is not an option. Everyone has to succeed.',
                'GET TO THE CHOPPA!',
                'I will be back!'])



@client.event 
async def on_ready():
    change_status.start()
    print('We have logged in as {0.user}'.format(client))
    
@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(next(status)))


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unoad_extension(f'cogs.{extension}')

@client.command()
async def reload (ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}') 

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all the arguments!')


client.run(TOKEN)
