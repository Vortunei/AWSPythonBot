import random
import os 
import discord 
from ec2_metadata import ec2_metadata

print(ec2_metadata.region)
print(ec2_metadata.instance_id)

client = discord.Bot()
token = str(os.getenv("TOKEN"))

@client.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))

@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    print(f'Message {user_message} by {username} on {channel}')

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

client.run(token)

