import os
import discord
from replit import db
from keep_alive import keep_alive
my_secret = os.environ['pass']

db["n"] = 10
db["usernames"] = ["Mitchell#8371", "Mitchell#9602", "Mitchell#7649", "Mitchell227#3454", "Mitchell V#9251", "Mitchell#1025", "Mitchellbox#7306", "Mitchell V#8562", "mitch#0333", "mitchell v#5424"]

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  #Self-check redundacy
  if message.author == client.user:
    return
  


  #Checks if author is Dyno and the string starts with "I tink I have seen you before"
  if message.channel.id == 804736189096787979 and message.author.id == 155149108183695360 and "I tink I have seen you before" in message.content:
    msg = message.content

    string = []
    for split in msg.split(" "):
      string.append(split)

    userID = ""

    for char in string[-1]:
      if char != '<' and char != '@' and char != '>':
        userID += char

    username = str(await client.fetch_user(userID))

    if "Mitchell" in username or "Mitch" in username or "mitchell" in username or "mitch" in username:
        usernames = db["usernames"]

        newAccount = True

        for element in usernames:
          if element == username:
            newAccount = False
            break
        
        if newAccount == True:
          usernames.insert(0, username)
          db["usernames"] = usernames
          db["n"] += 1

          await client.get_channel(855219010400026666).send("Mitchell has joined this server with " + str(db["n"]) + " unique accounts")


keep_alive()
#Creates instance of client
client.run(os.getenv('pass'))