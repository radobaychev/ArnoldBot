import discord
from discord.ext import commands
import random

class Minigames(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    #COMMANDS
    @commands.command(aliases=['8ball', 'eightball'])
    async def _8ball(self, ctx, *, question):
        resposnes = ['It is certain', 
                    'It is decidedly so',
                    'Without a doubt', 
                    'Yes – definitely', 
                    'You may rely on it', 
                    'As I see it, yes', 
                    'Most likely', 
                    'Outlook good',
                    'Yes', 
                    'Yes Signs point to yes', 
                    'Reply hazy, try again', 
                    'Ask again later', 
                    'Better not tell you now', 
                    'Cannot predict now', 
                    'Concentrate and ask again', 
                    'Dont count on it', 
                    'My reply is no', 
                    'My sources say no', 
                    'Outlook not so good', 
                    'Very doubtful',]
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(resposnes)}')




    @commands.command()
    async def rps (self, ctx, message):
        rpsGame = ['rock', 'paper', 'scissors']
        
        user_choice = message.lower()
        comp_choice = random.choice(rpsGame)
        if user_choice not in rpsGame:
            await ctx.send('That is not a valid choice! Rock, paper or scissors?')
        else:
         if user_choice == 'rock':
            if comp_choice == 'rock':
                await ctx.send(f'Well, that was weird. We tied.\nYour choice: {user_choice}\nMy choice: {comp_choice}')
            elif comp_choice == 'paper':
                await ctx.send(f'Nice try, but I won that time!!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
            elif comp_choice == 'scissors':
                await ctx.send(f"Aw, you beat me. It won't happen again!\nYour choice: {user_choice}\nMy choice: {comp_choice}")

         elif user_choice == 'paper':
            if comp_choice == 'rock':
                await ctx.send(f'The pen beats the sword? More like the paper beats the rock!!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
            elif comp_choice == 'paper':
                await ctx.send(f'Oh, wacky. We just tied. I call a rematch!!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
            elif comp_choice == 'scissors':
                await ctx.send(f"Aw man, you actually managed to beat me.\nYour choice: {user_choice}\nMy choice: {comp_choice}")

         elif user_choice == 'scissors':
            if comp_choice == 'rock':
             await ctx.send(f'HAHA!! I JUST CRUSHED YOU!! I rock!!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
            elif comp_choice == 'paper':
                await ctx.send(f'Bruh. >: |\nYour choice: {user_choice}\nMy choice: {comp_choice}')
            elif comp_choice == 'scissors':
                await ctx.send(f"Oh well, we tied.\nYour choice: {user_choice}\nMy choice: {comp_choice}")



def setup(client):
    client.add_cog(Minigames(client))