import discord
import responses
import os
from dotenv import load_dotenv
from discord.ext import tasks



load_dotenv()

token = os.getenv("DISCORD_TOKEN")



async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)
        

   
def run_discord_bot():
   
   intents = discord.Intents.default()
   intents.message_content = True
   client = discord.Client(intents = intents)
   
    
    
    
   @client.event
   async def on_ready():
        print(f'{client.user} is now running!')
        
        
        
        
   @client.event
   async def on_message(message):
    
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)   
        
        print(f"{username} said: '{user_message}' ({channel})")
        if message.author.bot:
            return
        
        @tasks.loop(seconds=30.0)   
        async def send_message_now(): 
          await send_message(message, user_message, is_private=False)
          
        send_message_now.start()  
        
 
    
    
    
     
            
           
    
       

        
   client.run(token)
    
    