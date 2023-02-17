import discord

client = discord.Client()

@client.event
async def on_member_update(before, after):
    # Check if the member's activity is playing League of Legends
    if str(after.activity) == "League of Legends":
        # Add the "Muted" role to the member
        await after.ban(reason="Playing League of Legends")
