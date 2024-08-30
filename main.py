from logging import fatal
import discord
from discord.ext import commands
from discord import app_commands

import os

port = int(os.getenv("PORT", 5000))
app.run(host='0.0.0.0', port=port)


from dotenv import load_dotenv
import os

# โหลดไฟล์ .env
load_dotenv()

# ใช้ค่าที่โหลดมา
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
DATABASE_URL = os.getenv('DATABASE_URL')

print(f"Discord Token: {DISCORD_TOKEN}")



from myserver import server_on

# สร้าง instance ของ bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents.all())





#///////////////////// BOT Event /////////////////////////
# กำหนดคำสั่งเริ่มต้น คำสั่ง bot พร้อมใช้งานแล้ว
@bot.event
async def on_ready():
    print(f'Bot Online {bot.user.name}')
    synced = await bot.tree.sync()  # ซิงค์คำสั่งไปยัง Discord
    print(f"{len(synced)} command(s) synced")



@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1279026726323880038)
    text = f"Welcome to the Server, {member.mention}!"

    embed = discord.Embed(
        title='Welcome to the server!',
        description=text,
        color=0x6FFFFF  # แก้ไขค่าสีให้ถูกต้องตามรูปแบบ Hex
    )

    # ส่งข้อความไปยังช่องที่ระบุ
    if channel is not None:
        await channel.send(text)
        await channel.send(embed=embed)

    # ส่งข้อความไปยัง DM ของสมาชิกที่เข้าร่วม
    try:
        await member.send(text)
    except discord.errors.Forbidden:
        print(f"Couldn't send DM to {member.name}. They might have DMs disabled.")


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1279026726323880038)
    text = f"{member.name} has left the server. We'll miss you!"

    embed = discord.Embed(
        title='Member Left',
        description=text,
        color=0xFF0000  # ใช้สีแดงเพื่อแสดงว่ามีสมาชิกออกจากเซิร์ฟเวอร์
    )

    # ส่งข้อความไปยังช่องที่ระบุ
    if channel is not None:
        await channel.send(text)
        await channel.send(embed=embed)

    # คุณสามารถเพิ่มโค้ดนี้ได้หากต้องการส่งข้อความ DM ไปยังสมาชิกที่ออกจากเซิร์ฟเวอร์
    try:
        await member.send(f"Sorry to see you go, {member.name}. If you have any feedback, please let us know.")
    except discord.errors.Forbidden:
        print(f"Couldn't send DM to {member.name}. They might have DMs disabled.")

# คำสั่ง  chatbot
@bot.event
async def on_message(message):
    mes = message.content
    if mes == 'hello':
        await message.channel.send("Hello It's me")

    elif mes == 'hi bot':
        await message.channel.send("Hello, " + str(message.author.name))

    await bot.process_commands(message)
    #ทำคำสั่ง event  แล้วไปทำคำสั่ง bot commnad ต่อ


#                   ////////// Commabds //////////
#กำหนดคำสังบอท

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.name}!')

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)


#คำสั่งบอท

@bot.command(name="greet", aliases=["hi", "hey"])
async def greet(ctx):
    await ctx.send(f"Hello, {ctx.author.name}!")

# Slash Command
@bot.tree.command(name='hibot', description='Replies with Hello')
async def hibot(interaction):
    await interaction.response.send_message("Hello, it's me, BOT DISCORD")

@bot.tree.command(name='name')
@app_commands.describe(name = "What's your name?")
async def namecommand(interaction, name : str):
    await interaction.response.send_message(f"Hello {name}")





# Embed

@bot.tree.command(name='help', description='Bot Command')
async def helpcommand(interaction):
    emmced = discord.Embed(title='กลุ่มขี้โม้',
                           description='รายชื่อ',
                           color=0x66FFFF,
                           timestamp= discord.utils.utcnow())


    emmced.add_field(name='zigzozay', value='ขี้โม้ 1', inline=True)
    emmced.add_field(name='winterakuma', value='ขี้โม้ 2', inline=True)
    emmced.add_field(name='vaivit', value='ขี้โม้ 3', inline=False)

    emmced.set_author(name='ZIGZOZAY', url='https://www.tiktok.com/@zigzozay', icon_url='https://cdn.discordapp.com/attachments/1249299398891143220/1278039740494516244/IMG_3111.png?ex=66d2a682&is=66d15502&hm=ac54fa14a6bcea78890e72723e3ec39bb9d2529a3448815829a3c56f1c1ce0b7&')

    #  ใส่รุปเล็ก-ใหญ่
    emmced.set_thumbnail(url='https://cdn.discordapp.com/attachments/1193975755777003643/1269535351274209422/AD_4_PNG.png?ex=66d2b16e&is=66d15fee&hm=9b812c14f50b7aefdc4e3d305fffdddff60e1aea43501b2ab2c98c2747bbc618&')
    emmced.set_image(url='https://cdn.discordapp.com/attachments/656703700663926815/1279102119592591390/06.png?ex=66d3382d&is=66d1e6ad&hm=2b408779408d5615bcfce4a1de3ab4c04d38877fcb466e63f63b81037d731ad8&')




    await interaction.response.send_message(embed = emmced)








server_on()


# ใส่ token ของบอทที่นี่
bot.run(os.getenv('DISCORD_TOKEN'))
