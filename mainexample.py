#Import class libaries to work with discord

import random
import os 
import discord 
#Imports requests from AWS
from ec2_metadata import ec2_metadata
print(ec2_metadata.region)
print(ec2_metadata.instance_id)

#Call load dotenv
load_dotenv()

#creating of object from discord class
client = discord.Bot()
token = str(os.getenv("TOKEN"))

#Event client initiates function when the client event connects to discord.
#string gets turned into argument parameter due to brackets
#create output to the terminal window formatting a string.


@client.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))

 #Event driven by client sending info it needed.
 #Creating 3 objects first ouputting a message.
@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)
 #This is the output that is formatted(f) by bracket.
    print(f'Message {user_message} by {username} on {channel}')


#If el loops that serve to run statements and apply the logic per the answer given by me.

    if message.author == client.user:
        return
    
    if channel == "monte":
        if user.message.lower() == "gator?" or user_message.lower() == "gator":
            await message.channel.send(f"nation!"){username} Your EC2 Data: {ec2_metadata.region}")
            return
        
        elif user_message.lower() == "hello?":
            await message.channel.send(f"hi! {username}")

        elif user_message.lower() == "EC2 Data":
            await message.channel.send("Your instance data is + ec2_metadata")
#Runs the token from the env file 
client.run(token)

