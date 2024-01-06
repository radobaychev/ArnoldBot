import discord
from discord.ext import commands

class Basic(commands.Cog):

    def __init__(self, client):
        self.client = client

    #EVENTS
    @commands.Cog.listener()
    async def on_member_join(self, member):
        await self.client.get_channel(967752400742011027).send(f'{member.mention} has joined! :partying_face: Enjoy your stay here! :heart:')
        await member.send(f'Wellcome to **{member.guild}**! Enjoy your stay')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        await self.client.get_channel(967752400742011027).send(f'Sad to see you go {member.mention} :cry: :broken_heart:')

    #COMMANDS
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms') 

    @commands.command()
    async def info(self, ctx):
        await ctx.send(ctx.guild)
        await ctx.send(ctx.author)


def setup(client):
    client.add_cog(Basic(client))