import discord
from discord.ext import commands
import random

class chat(commands.Cog):

    def __init__(self, client):
        self.client = client

    #COMMANDS
    @commands.Cog.listener()
    async def on_message(self, message,):
        
            username = str(message.author).split('#')[0]
            user_message = str(message.content)
            channel = str(message.channel)
            print(f'{username}: {user_message} ({channel})')

            
            if channel == 'bot-chat':
                if user_message.lower() == 'hello':
                    await message.channel.send(f'Hello {username}!')
                    return
                elif user_message.lower() == 'how are you':
                    await message.channel.send(f'Always good to go! And you {username}?')
                    return
                elif user_message.lower() == 'bye':
                    await message.channel.send(f'See you soon {username}!')
                    return
                elif user_message.lower() == '!random':
                    response = f'Your random number is: {random.randrange(1000000)}'
                    await message.channel.send(response)
                    return     


            if user_message.lower() == '!anywhere':
                await message.channel.send('This can be used anywhere!')
                return    
            


def setup(client):
    client.add_cog(chat(client))