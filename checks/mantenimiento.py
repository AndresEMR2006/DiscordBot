

@bot.check
async def mantenimiento(ctx):
    if MANTENIMIENTO:
        return ctx.author.guild_permissions.administrator
    return True