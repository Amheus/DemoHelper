import os

import logging

from discord.ext import commands
from discord.ext.commands import Context, DefaultHelpCommand
from dotenv import load_dotenv

# set logging level todo get this from .env file
logging.basicConfig(level=logging.INFO)

# load the private discord token from .env file.
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


class General(commands.Cog):
    """
    General commands for everyone.
    """

    @commands.command()
    async def source(self, ctx: Context):
        """
        Link to the sourcecode.
        """
        await ctx.send('https://github.com/IdrisTheDragon/demoHelperBot')


# Initialise the Bot object with an accesible help Command object
helpCommand = DefaultHelpCommand()
bot = commands.Bot(
    command_prefix='!',
    help_command=helpCommand,
    description='DemoHelper is a queue system for online practicals.\n Students can add themselves to the queue.\n '
                'When a demonstrator is free to help, they can call the next command to get the next waiting student. '
)

# Setup the General cog with the help command
generalCog = General()
bot.add_cog(generalCog)
helpCommand.cog = generalCog


# load other cogs
bot.load_extension("cogs.demoHelper")


@bot.event
async def on_ready():
    """
    Do something when the bot is ready to use.
    """
    print(f'{bot.user.name} has connected to Discord!')


@bot.event
async def on_command_error(ctx, error):
    """
    Handle the Error message in a nice way.
    """
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')
    elif isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send('You are missing a required argument.')
    elif isinstance(error, commands.errors.CommandNotFound):
        await ctx.send('Pardon, I didn\'t quite get that.')
    else:
        await ctx.send('Something went wrong, please contact the Admin.')
        logging.error(error)

# Start the bot
bot.run(TOKEN)
