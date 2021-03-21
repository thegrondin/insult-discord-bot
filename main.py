import discord
import os

import commands
from NameManager import NameManager
from InsultManager import InsultManager
import utils

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    name = NameManager.name_in_message(message.content)
    if (name is not None):
      await message.channel.send(utils.bold(InsultManager.send_insult(name)))

    for command_key in commands.commands:
        if (message.content.startswith(command_key)):
            await message.channel.send(commands.commands[command_key](
                message.content.partition(' ')[2]))


client.run(os.getenv('TOKEN'))
