import re
import discord
from discord.ext import commands
from roll import Roll

# loading the token
file = open('token.txt', 'r')
token = (file.readline())
file.close()

regEx = re.compile("""\((\D*)(\d*)?d(\d+)(\s*(\+|-)\s*(\d+))?\s*(Advantage|advantage|Disadvantage|disadvantage)?\)""")

client = discord.Client()

bot = commands.Bot(command_prefix='>')
@bot.event
async def on_message(message):
    if message.author == bot.user.id:
        return
    matches = regEx.findall(message.content)
    if matches:
        length = len(matches)
        for i in range(len(matches)):
            current = matches[i]
            numrolls = 1
            if current[6]:
                numrolls = 2
                multioutput = ['', '']
                multiroll = [0, 0]
            for j in range(0, numrolls):
                if not current[2]:
                    await message.channel.send('Please specify a number of faces')
                    return
                if current[4] and not current[5]:
                    await message.channel.send('Please specify a modifier value')
                    return

                if current[3]:
                    roll = Roll(current[0], int(current[1]), int(current[2]), current[4], int(current[5]))
                else:
                    roll = Roll(current[0], int(current[1]), int(current[2]), '', 0)

                roll.rolldice()
                roll.sumrolls()
                if roll.is1d20:
                    roll.checknaturals()

                if current[3]:
                    roll.handlemodifiers()
                output = roll.getfinalstring()

                if not current[6]:
                    await message.channel.send(output)
                else:
                    multioutput[j] = output
                    multiroll[j] = roll.gettotal()
            if current[6]:
                if current[6] == 'Advantage' or current[6] == 'advantage':
                    if multiroll[0] > multiroll[1]:
                        output = '**' + multioutput[0] + '**'
                        await message.channel.send(output)
                        await message.channel.send(multioutput[1])
                    elif multiroll[0] < multiroll[1]:
                        output = '**' + multioutput[1] + '**'
                        await message.channel.send(output)
                        await message.channel.send(multioutput[0])
                    else:
                        await message.channel.send(multioutput[0])
                        await message.channel.send(multioutput[1])
                else:
                    if multiroll[0] < multiroll[1]:
                        output = '**' + multioutput[0] + '**'
                        await message.channel.send(output)
                        await message.channel.send(multioutput[1])
                    elif multiroll[0] > multiroll[1]:
                        output = '**' + multioutput[1] + '**'
                        await message.channel.send(output)
                        await message.channel.send(multioutput[0])
                    else:
                        await message.channel.send(multioutput[0])
                        await message.channel.send(multioutput[1])

bot.run(token)
