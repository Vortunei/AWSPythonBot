#Gabriel Rojas Discord Bot

#import libraries into S3
import discord
import os
from dotenv import load_dotenv
from ec2_metadata import ec2_metadata 


#Create a discord client
client = discord.Client()


#Gets the token from the env file
load_dotenv()
token = str(os.getenv('TOKEN'))

#Event handler for when bot is online
@client.event #<--Fix
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))

#Event handler for when message is received
@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)
    
    #print user message in terminal for debugging
    print(f'Message {user_message} by {username} on {channel}')

    #Ignores messages from bot itself
    if message.author == client.user:
        return 
    
    #Responds in monte channel only
    if channel == "monte":
        #Responds with nation if user inputs gator
        if user_message.lower() == "gator" or user_message.lower() == "gator":
            await message.channel.send(f"nation! {username} Your EC2 Data: {ec2_metadata.region}")
            return 
        #Responds with hello if user inputs hello world
        elif user_message.lower() == "hello world!":
            await message.channel.send(f'Hello!')
            
        #Responds with ec2 region when user inputs ec2 data 
        elif user_message.lower() == "ec2 data":
            await message.channel.send("Your instance data is" + ec2_metadata.region)
        #Responds with ec2 server information for the user
        elif user_message.lower() == "tell me about my server":
            await message.channel.send("Your instance data is:" + "\nregion: " + ec2_metadata.region + "\navailability zone: " + ec2_metadata.availability_zone + "\npublic_ipv4: " + ec2_metadata.public_ipv4 + "\ninstance type:" + ec2_metadata.instance_type)
        
#Runs the bot
client.run(token)

