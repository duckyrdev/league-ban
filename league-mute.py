import discord

client = discord.Client()

@client.event
async def on_member_update(before, after):
    # Check if the member's activity is playing League of Legends
    if str(after.activity) == "League of Legends":
        # Get the "Muted" role
        muted_role = discord.utils.get(after.guild.roles, name="Muted")
        
        # Add the "Muted" role to the member
        await after.add_roles(muted_role, reason="Playing League of Legends")

        
