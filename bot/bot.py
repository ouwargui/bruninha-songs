import os
from pathlib import Path
from dotenv import load_dotenv

import discord
from discord.ext import commands
from discord.flags import Intents

load_dotenv()

DISCORD_API_KEY = os.environ.get('DISCORD_API_KEY')

class MusicBot(commands.Bot):
    def __init__(self):
        self._cogs = [p.stem for p in Path(".").glob("./bot/cogs/*.py")]
        super().__init__(command_prefix=self.prefix, case_insensitive=True, intents=discord.Intents.all())

    def setup(self):
        print("Iniciando setup...")

        for cog in self._cogs:
            self.load_extension(f"bot.cogs.{cog}")
            print(f"Carregou '{cog}' cog.")

        print("Setup completo!")

    def run(self):
        self.setup()

        print("Iniciando o bot...")
        super().run(DISCORD_API_KEY, reconnect=True)

    async def shutdown(self):
        print("Encerrando a conexão com o Discord...")
        await super().close()

    async def close(self):
        print("Encerrando com interrupção do teclado...")
        await self.shutdown()
    
    async def on_connect(self):
        print(f"Bot conectado (latência: {self.latency*1000:,.0f}ms).")

    async def on_resumed(self):
        print("Bot resumido.")

    async def on_disconnect(self):
        print("Bot desconectado.")

    # async def on_error(self, err, *args, **kwargs):
    #     raise

    # async def on_command_error(self, ctx, exc):
    #     raise getattr(exc, "original", exc)

    async def on_ready(self):
        self.client_id = (await self.application_info()).id
        print("Bot pronto.")

    async def prefix(self, bot, msg):
        return commands.when_mentioned_or("!")(bot, msg)

    async def process_commands(self, msg):
        ctx = await self.get_context(msg, cls=commands.Context)

        if ctx.command is not None:
            await self.invoke(ctx)

    async def on_message(self, msg):
        if not msg.author.bot:
            await self.process_commands(msg)
