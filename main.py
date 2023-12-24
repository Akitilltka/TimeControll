import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

units = {
    's': 1,
    'm': 60,
    'h': 3600
}

@bot.command()
async def напомни(ctx, reminder, *, notes=None):
    try:
        await ctx.message.add_reaction('👌🏼')
        digits = int(reminder[0])  # Получаем первую цифру из напоминания (например, '1')
        unit = reminder[1:].lower()  # Получаем единицу времени из напоминания (например, 's', 'm', 'h')
        seconds = units[unit]  # Конвертируем единицу времени в секунды
        await ctx.send(f'Напоминание: {notes} . Напомнить мне надо через: {seconds} секунд.')
        await asyncio.sleep(seconds)  # Пауза в указанное количество секунд перед отправкой напоминания
        await ctx.send(f'Дружеское напоминание: {notes}. Я напомнил через {reminder}. {ctx.author.mention}')
        author = ctx.message.author
        await author.send(f'Дружеское напоминание: {notes}. Я напомнил через {reminder}. {ctx.author.mention}')
    except ValueError:
        await ctx.send('Ошибка: Некорректное значение для напоминания. Пожалуйста, введите число.')
    except Exception as e:
        await ctx.send(f'Произошла ошибка. Возможные ошибки: \n 1. Вы забыли добавить единицу времени. Например: 1m - 1 минута, 1s - 1 секунда, 1h - 1 час. \n 2. Возможно, произошла системная ошибка. Обратитесь к разработчику. \n 3. Вы не разрешили боту отправить вам в ЛС сообщение. \n Код ошибки: {e}')

        

@bot.command()
async def хелп(ctx):
    await ctx.message.add_reaction('👌🏼')

    await ctx.send(">напомни (через сколько) (чо напомнить)")





bot.run('MTE4ODA4MTU0NTExOTAyMzEwNA.Gx9-Iz.g5XJBUGQNj9MlDVsasrQ951ejjVsCirtaAAs7s')