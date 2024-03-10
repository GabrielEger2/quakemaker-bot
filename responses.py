import discord

async def get_or_create_voice_channel(guild, channel_name):
    voice_channel = discord.utils.get(guild.channels, name=channel_name, type=discord.ChannelType.voice)
    if not voice_channel:
        voice_channel = await guild.create_voice_channel(channel_name)
    return voice_channel

async def get_response(user_input: str) -> None:
    if user_input.content.startswith("!quake"):
        print("Moving user")
        mentioned_users = user_input.mentions
        if mentioned_users:
            print(f"Mentioned users: {mentioned_users}")
            target_user = mentioned_users[0] 
            guild = user_input.guild
            first_voice_channel = await get_or_create_voice_channel(guild, 'Quake Suffering')

            second_voice_channel = await get_or_create_voice_channel(guild, 'Quake Suffering 2')

            original_voice_channel = target_user.voice.channel if target_user.voice else None
            
            if target_user.voice:
                try:
                    for i in range(4):
                        await target_user.move_to(first_voice_channel)
                        await target_user.move_to(second_voice_channel)
                    await target_user.move_to(original_voice_channel)
                except Exception as e:
                    await user_input.channel.send(f"Error moving the user: {e}")
            else:
                await user_input.channel.send(f"{target_user.mention} is not in a voice channel.")
        else:
            await user_input.channel.send("No user mentioned.")