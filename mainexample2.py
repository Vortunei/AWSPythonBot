#Import discord.py which allows access to the discord API.
import discord

#Gets client object from discord.py
bot = discord.client

#Event listener for when bot goes off and online
@bot.event
async def on_ready():
        #Makes a counter to keep track of servers bot is connected to.
        guild_count = 0

        # Makes a loop through the servers bot is associated with.
        for guild in bot.guilds:
                # print the servers id and name.
                print(f"-{guild.id}(name: {guild.name})")

                #Starts a counter.
                guild_count = guild_count +1

        # prints how many servers the bot is in.
        print("MonteBot is in " + str(guild_count) + "guilds.")

# Event listener for when a new message is sent to a channel.
@bot.event
async def on_message(message):
        # checks if the message that was sent is "hello"
        if message.content == "hello":
                # this sends a message back to the channel.
                await message.channel.send("hi!")

#executes the bot with the token.
client.run("TOKEN")   