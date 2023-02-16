import discord

client = discord.Client()

@client.event
async def on_member_update(before, after):
    if str(after.activity) == "League of Legends":
        await after.ban(reason="Playing League of Legends")
