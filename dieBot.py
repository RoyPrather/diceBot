import os 
import discord
import random

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

def isPlusInIndex(x,m):
    try:
        if m.content[x] == "+":
            return True
        else:
            return False
    except IndexError:
        return False

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

async def rollStats(msg):
    list = [None] * 4
    for i in range(4):
        list[i] = rollDice(1,6,0)
    await msg.send(str(list[0])+" "+str(list[1])+" "+str(list[2])+" "+str(list[3]))
    list.sort(reverse = True)
    acc = 0
    for i in range(3):
        acc += list[1]
    await msg.send(str(acc))

async def rollAllStats(msg):
    for i in range(6):
        rollStats(msg)


@client.event
async def on_ready():
    print(f'{client.user} Connected!')

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
#----------------------------Roll Stats------------------------------
    if (msg.content[:9] == "rollstats"):
        rollStats(msg)

    if (msg.content[:12] == "rollallstats"):
        rollAllStats(msg)

#-----------------------------99d99+99-------------------------------- 
   #is the first index a number 
    if isint(msg.content[0]):
        num = int(msg.content[0])
        #is the second index a number
        if isint(msg.content[1]):
            num = int(msg.content[:2])
            #is the third index a d
            if msg.content[2] == 'd':
                #is the fouth and fith index a number the sixth index a + sign
                if isint(msg.content[3:5]) and isPlusInIndex(5,msg):
                    #is there a two digit number fallowing the + sign
                    if isint(msg.content[6:8]):
                        await msg.channel.send(str(rollDice(num,msg.content[3:5],msg.content[6:8])))
                    #is there a one digit number fallowing the + sign
                    elif isint(msg.content[6]):
                        await msg.channel.send(str(rollDice(num,msg.content[3:5],msg.content[6])))
                #is the forth index a number and is the fith index a + sign
                elif isint(msg.content[3]) and isPlusInIndex(4,msg):
                    #is there a two digit number fallowing the + sign
                    if isint(msg.content[5:7]):
                        await msg.channel.send(str(rollDice(num,msg.content[3],msg.content[5:7])))
                    #is there a one digit number fallowing the + sign    
                    elif isint(msg.content[5]):
                        await msg.channel.send(str(rollDice(num,msg.content[3],msg.content[5])))
                #is there a two digit number with no + sign
                elif isint(msg.content[3:5]):
                    await msg.channel.send(str(rollDice(num,msg.content[3:5],0)))
                #is there a one digit number with no + sign
                elif isint(msg.content[3]):    
                    await msg.channel.send(str(rollDice(num,msg.content[3],0)))
        
        #roll up to 9 d 100
        elif msg.content[1:5] == 'd100':
            await msg.channel.send(str(rollDice(num,100,0)))
        #is the second index a d    
        elif msg.content[1] == 'd':
            #is the third and forth indexs a number and there is a + sign in the fifth index
            if isint(msg.content[2:4]) and isPlusInIndex(4,msg):
                    #is there a two digit number fallowing the + sign
                    if isint(msg.content[5:7]):
                        await msg.channel.send(str(rollDice(num,msg.content[2:4],msg.content[5:7])))
                    #is there a one digit number fallowingt the + sign
                    elif isint(msg.content[5]):
                        await msg.channel.send(str(rollDice(num,msg.content[2:4],msg.content[5])))
            #is the third index a number and fallowed by a + sign  
            elif isint(msg.content[2]) and isPlusInIndex(3,msg):
                    #is there a two digit number fallowing the + sign
                    if isint(msg.content[4:6]):
                        await msg.channel.send(str(rollDice(num,msg.content[2],msg.content[4:6])))
                    #is there a one digit number fallowing the + sign
                    elif isint(msg.content[4]):
                        await msg.channel.send(str(rollDice(num,msg.content[2],msg.content[4])))
            #is there a two digit number with no + sign
            elif isint(msg.content[2:4]):
                await msg.channel.send(str(rollDice(num,msg.content[2:4],0)))
            #is there a one digit number with no + sign 
            elif isint(msg.content[2]):    
                await msg.channel.send(str(rollDice(num,msg.content[2],0)))

client.run(TOKEN)
