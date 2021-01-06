import os 
import discord
import random

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

def isint(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

def rollDice(num,faces,plus):
    acc = 0 
    for i in range(int(num)):
        acc += random.randint(1,int(faces))
    return(acc + int(plus))

@client.event
async def on_ready():
    print(f'{client.user} Connected!')

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return 
    
    if isint(msg.content[0]):
        num = int(msg.content[0])
        if isint(msg.content[1]):
            num = int(msg.content[:2])
            if msg.content[2] == 'd':
                if len(msg.content) > 5:
                    if msg.content[5] == '+':
                        if len(msg.content) > 7 and isint(msg.content[6:8]):
                            await msg.channel.send(str(rollDice(num,msg.content[3:5],msg.content[6:8])))
                        elif isint(msg.content[6]):
                            await msg.channel.send(str(rollDice(num,msg.content[3:5],msg.content[6])))
                    elif isint(msg.content[3]) and msg.content[4] == '+':
                        if len(msg.content) > 6 and isint(msg.content[5:7]):
                            await msg.channel.send(str(rollDice(num,msg.content[3],msg.content[5:7])))
                        elif isint(msg.content[5]):
                            await msg.channel.send(str(rollDice(num,msg.content[3],msg.content[5])))
                    elif isint(msg.content[3]):
                        await msg.channel.send(str(rollDice(num,msg.content[3],0)))
                elif isint(msg.content[3:5]):    
                    await msg.channel.send(str(rollDice(num,msg.content[3:5],0)))
        else:
            if msg.content[1:5] == 'd100':
                await msg.channel.send(str(rollDice(num,100,0)))

            elif msg.content[1] == 'd':
                if len(msg.content) > 4:
                    if msg.content[4] == '+':
                        if len(msg.content) > 6 and isint(msg.content[5:7]):
                            await msg.channel.send(str(rollDice(num,msg.content[2:4],msg.content[5:7])))
                        elif isint(msg.content[5]):
                            await msg.channel.send(str(rollDice(num,msg.content[2:4],msg.content[5])))
                    elif isint(msg.content[2]) and msg.content[3] == '+':
                        if len(msg.content) > 5 and isint(msg.content[4:6]):
                            await msg.channel.send(str(rollDice(num,msg.content[2],msg.content[4:6])))
                        elif isint(msg.content[4]):
                            await msg.channel.send(str(rollDice(num,msg.content[2],msg.content[4])))
                    elif isint(msg.content[2]):
                        await msg.channel.send(str(rollDice(num,msg.content[2],0)))

                elif isint(msg.content[2:4]):    
                    await msg.channel.send(str(rollDice(num,msg.content[2:4],0)))

client.run(TOKEN)
